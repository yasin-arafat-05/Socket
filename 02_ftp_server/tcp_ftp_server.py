
import socket
server = socket.socket()
server.bind(('localhost',9999))
server.listen(3)
print("server is wating for establish connection .....")

while True:
   client_socket,client_address =  server.accept()
   print(f"received client: {client_socket}")
   with open('received_file.txt','wb') as f:
       data = client_socket.recv(1024)
       if not data:
           break 
       f.write(data)
       client_socket.send(b"ACK")
       print(f"received successfully, send ACK")
       
   print("file transfer complete")
   client_socket.close()
server.close()

