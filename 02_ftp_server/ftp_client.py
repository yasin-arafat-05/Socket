
import socket

client = socket.socket()
client.connect(('localhost',9999))
client.settimeout(5)

filename = input("Enter the file name to send: ")

with open(filename,'rb') as f:
    while True:
        chunk = f.read(100)
        if not chunk:
            break
        ask_received = False
        while not ask_received:
            try:
                client.send(chunk)
                print("send successfully the chunk")
                ack = client.recv(1024)
                if ack==b"ACK":
                    print("ack received.")
                    ask_received=True
            except socket.timeout:
                print("Timeout")
print("file transfer complete")
client.close()
         