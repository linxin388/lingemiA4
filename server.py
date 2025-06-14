import socket
import threading
import random
import os
import base64

class UDPServer:
    def __init__(self, port):
        self.welcome_port = port
        self.welcome_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.welcome_socket.bind(('', self.welcome_port))
        print(f"Server started on port {self.welcome_port}, waiting for download requests...")


def start(self):
    while True:
        try:
            data, client_address = self.welcome_socket.recvfrom(1024)
            client_request = data.decode().strip()
            parts = client_request.split()

            if len(parts) == 2 and parts[0] == "DOWNLOAD":
                filename = parts[1]
                threading.Thread(target=self.handle_download, args=(filename, client_address)).start()
            else:
                print(f"Invalid request from {client_address}: {client_request}")


