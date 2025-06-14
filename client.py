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