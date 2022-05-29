#import socket library
import socket

#create socket using TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#get hostname using socket
host = socket.gethostname()

#setting port to communicate with client
port = 54873

#binding host and port of server
sock.bind((host, port))

#listening to one client only
sock.listen(1)

#waiting for connection
print('Waiting...')

#accept connection from client and saves client's information
connection, client_address = sock.accept()

try:
	print('Host ' + host + ' established connection with ' + str(client_address))
	
	#send connection message to connected client
	connection.sendall('Thank you for connecting'.encode())
finally:
	#closing connection on error or finishing program
	connection.close()