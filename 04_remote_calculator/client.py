import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 9999))

num1 = input("Enter first number: ")
operator = input("Enter operator (+, -, *, /, %): ")
num2 = input("Enter second number: ")

message = f"{num1}{operator}{num2}"
client.send(message.encode())

result = client.recv(1024).decode()
print(f"Result: {num1} {operator} {num2} = {result}")

client.close()