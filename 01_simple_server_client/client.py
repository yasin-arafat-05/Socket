
import socket

client = socket.socket()
client.connect(('localhost',9999))

# take a name from clinet:
name = input("Enter your name: ")
client.send(bytes(f'{name}','utf-8'))

# now set the buffersize and print what client sending:
print(client.recv(2048))

# decode for printing in string:
print(client.recv(2048).decode())


