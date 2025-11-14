
import socket

server = socket.socket()
server.bind(("localhost",9999))

# max 3 client:
server.listen(3)
print("Waiting for Connection....")

while True:
    client_socket,client_addr =  server.accept()
    # received from client:
    name = client_socket.recv(2048).decode()
    
    print(f"Connected with address: {client_addr}, client name: {name}")
    
    client_socket.send(bytes("Hi! from Yasin's Server","utf-8"))
    client_socket.close()
    
    