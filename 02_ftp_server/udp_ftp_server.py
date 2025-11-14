
import socket

server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(('localhost',9999))
print("udp server is listening ....")

with open("received_file_udp.txt",'w') as f:
    while True:
        data, addr = server.recvfrom(1024)
        if data==b'EOF':
            print("file transfer complete")
            break
        line = data.decode()
        f.write(line)
        print("received")
server.close()