import socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print(f"Connected to UDP Chat Server\n")

try:
    while True:
        msg = input("You: ")
        client.sendto(msg.encode(), ('localhost', 9999))
        
        reply, _ = client.recvfrom(1000)
        print(f"Server: {reply.decode()}")
except KeyboardInterrupt:
    print("\nChat ended")

client.close()