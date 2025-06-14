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