from email import message
import socket
import sys
import time

new_socket=socket.socket()
host_name=socket.gethostname()
s_ip=socket.gethostbyname(host_name)
port =9090
new_socket.bind((host_name,port))
print(s_ip)
name=input('Name')
new_socket.listen(1)
conn,add=new_socket.accept()
client =(conn.recv(1024)).decode()
print (client+'connected')
conn.send(name.encode())
while True:
    message = input('Me : ')
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    print(client, ':', message)