import socket

HEADER = 64
PORT = 5050
SERVER = "10.0.0.29"
ADDRESS = (SERVER, PORT)
FORMAT = 'utf-8'
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESS)
DISCONNECT_MESSAGE = "!DISCONNECTED"