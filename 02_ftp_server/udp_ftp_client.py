

import socket

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
filename = input("Enter the filename: ")

with open(filename,'r') as f:
    for line in f:
        client.sendto(line.encode(),('localhost',9999))
client.sendto(b'EOF',('localhost',9999))
print("file transfer complete")
client.close()
