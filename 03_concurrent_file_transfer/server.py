import socket
import threading
import time
import os

def handle_client(conn, addr):
    print(f"Thread started for client {addr}")
    
    filename = conn.recv(1024).decode()
    print(f"Client {addr} requested: {filename}")
    
    if os.path.exists(filename):
        conn.send(b'OK')
        with open(filename, 'rb') as f:
            while True:
                data = f.read(1000)
                if not data:
                    break
                conn.send(data)
                time.sleep(0.2)
        print(f"File {filename} sent to {addr}")
    else:
        conn.send(b'ERROR: File not found')
    
    conn.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 9999))
server.listen(5)

print(f"Server listening on {'localhost'}:{9999}")

while True:
    conn, addr = server.accept()
    print(f"Connection from {addr}")
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()
    