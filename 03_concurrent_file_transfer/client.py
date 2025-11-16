
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 9999))

filename = input("Enter filename to download: ")
client.send(filename.encode())
response = client.recv(1024)

if response == b'OK':
    with open(f'downloaded_{filename}', 'wb') as f:
        while True:
            data = client.recv(1000)
            if not data:
                break
            f.write(data)
    print(f"File downloaded as downloaded_{filename}")
else:
    print(response.decode())
client.close()

