import socket
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDRESS = (SERVER, PORT)
FORMAT = 'utf-8'
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDRESS)
DISCONNECT_MESSAGE = "!DISCONNECTED"
def handle_client(conn, addr) :
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        msg_length = int(msg_length)
        msg = conn.recv(msg_length).decode(FORMAT)
        print(f"[{addr}] {msg}")
        if msg == DISCONNECT_MESSAGE:
            connected = False
        print(f"[{addr}] {msg}")
        conn.close()

def start():
    server.listen()
    print("[LISTENING] Server is listening")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args = (conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS]{threading.activeCount() - 1}")

start()

