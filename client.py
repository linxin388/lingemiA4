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