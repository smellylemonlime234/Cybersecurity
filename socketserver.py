import socket
import threading
from colorama import Fore, Style

Socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("Waiting for client")

#YOU WILL have to change this address to YOUR IP address
#If you want to connect to devices outside of your LAN, you must enable port forwarding on your router at port 5600
IP = "x.x.x.x"

Socket.bind((IP, 5600))
Socket.listen(1)
client, address = Socket.accept()
print("connected")

username = input("Please enter your username: ")
username = Fore.BLUE + username + Style.RESET_ALL

client_username = client.recv(1024).decode()
print("You are connected with", client_username)
client.sendall(username.encode())

while True:
    print("please print the client username...")
    print(client_username+': ',end='')
    client_message = client.recv(1024).decode()
    print(client_message)

    if client_message == "exit":
        break
    
    message = input(username+': ')
    if message == "exit":
        client.sendall("exit".encode())
        break

    client.sendall(message.encode())
    
print("Ending connection")

client.close()    
Socket.close()
