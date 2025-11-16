import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('localhost', 9999))

print(f"UDP Chat Server waiting on {'localhost'}:{9999}\n")

try:
    while True:
        msg, addr = server.recvfrom(1000)
        print(f"Client: {msg.decode()}")
        
        reply = input("You: ")
        server.sendto(reply.encode(), addr)
except KeyboardInterrupt:
    print("\nChat ended")

server.close()