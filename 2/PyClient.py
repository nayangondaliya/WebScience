#import socket library
import socket

#create socket using TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#get hostname using socket
host = socket.gethostname()

#setting port to communicate with client
port = 54873

#connect the socket to the port on the server
sock.connect((host, port))

try:
    #recieve message from server and decode it (byte to string)
    print(sock.recv(1024).decode())
finally:
    #closing socket on error or finishing program
    sock.close()
