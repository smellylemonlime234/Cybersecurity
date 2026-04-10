import socket
import threading
from colorama import Fore, Style

Socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#set IP to your SERVER'S IP
IP = "x.x.x.x"

if Socket.connect_ex((IP,5600)) == 0:
    print("connected")
else:
    print("didn't work")

username = input("Please enter your username: ")
username = Fore.RED + username + Style.RESET_ALL

Socket.sendall(username.encode())
server_username = Socket.recv(1024).decode()
print("You are connected with", server_username)

while True:
    message = input(username+': ')

    if message == "exit":
        Socket.sendall("exit".encode())
        break
    
    Socket.sendall(message.encode())
    print(server_username+': ',end='')
    server_message = Socket.recv(1024).decode()
    print(server_message)

    if server_message == "exit":
        break

print("Ending connection") 
Socket.close()
