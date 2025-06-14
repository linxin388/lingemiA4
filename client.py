import socket
import sys
import os
import base64
import time


class UDPClient:
    def __init__(self, host, port, file_list):
        self.server_host = host
        self.server_port = port
        self.file_list = file_list
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.settimeout(1)  # Initial timeout of 1 second
        self.max_retries = 5

    def download_files(self):
        try:
            with open(self.file_list, 'r') as f:
                files = [line.strip() for line in f.readlines() if line.strip()]

            for filename in files:
                self.download_file(filename)

        except FileNotFoundError:
            print(f"Error: File list '{self.file_list}' not found.")
        except Exception as e:
            print(f"Error reading file list: {e}")

    def download_file(self, filename):
        print(f"\nRequesting file: {filename}")

        # Step 1: Send DOWNLOAD request and get file info
        download_msg = f"DOWNLOAD {filename}"
        response = self.send_and_receive(download_msg, self.server_host, self.server_port)

        if not response:
            print(f"Failed to get response for DOWNLOAD request after {self.max_retries} attempts")
            return

        parts = response.split()

        if parts[0] == "ERR":
            print(f"Server error: {' '.join(parts[2:])}")
            return

        if parts[0] != "OK" or parts[1] != filename:
            print(f"Invalid response from server: {response}")
            return

        # Parse OK response
        file_size = int(parts[3])
        data_port = int(parts[5])
        print(f"Downloading {filename} (size: {file_size} bytes)")

        # Step 2: Download file in chunks
        try:
            with open(filename, 'wb') as file:
                bytes_received = 0
                block_size = 1000  # bytes per request

                while bytes_received < file_size:
                    start = bytes_received
                    end = min(start + block_size - 1, file_size - 1)

                    file_msg = f"FILE {filename} GET START {start} END {end}"
                    response = self.send_and_receive(file_msg, self.server_host, data_port)

                    if not response:
                        print(f"Failed to receive data block {start}-{end} after {self.max_retries} attempts")
                        return

                    # Parse data response
                    resp_parts = response.split()
                    if (len(resp_parts) >= 9 and resp_parts[0] == "FILE" and
                            resp_parts[1] == filename and resp_parts[2] == "OK"):
                        data_start = int(resp_parts[4])
                        data_end = int(resp_parts[6])
                        base64_data = ' '.join(resp_parts[8:])

                        # Decode and write data
                        binary_data = base64.b64decode(base64_data)
                        file.seek(data_start)
                        file.write(binary_data)

                        bytes_received += len(binary_data)
                        print('*', end='', flush=True)