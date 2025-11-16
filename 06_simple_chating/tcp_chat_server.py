import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 9999))
server.listen(1)

print(f"TCP Chat Server waiting on {'localhost'}:{9999}")
conn, addr = server.accept()
print(f"Connected to {addr}\n")

try:
    while True:
        msg = conn.recv(1024).decode()
        if not msg:
            break
        print(f"Client: {msg}")
        
        reply = input("You: ")
        conn.send(reply.encode())
except KeyboardInterrupt:
    print("\nChat ended")

conn.close()
server.close()