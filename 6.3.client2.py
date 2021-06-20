import socket
import signal
import sys


ClientSocket = socket.socket()
host = '169.254.98.74'
port = 8858


print('Waiting for connection')
try:
	ClientSocket.connect((host, port))
except socket.error as e:
	print (str(e))


Response = ClientSocket.recv(1024)
print (Response.decode("utf-8"))
while True:
	Input = input('Enter the operation and number:')


	if Input == 'exit':
		break
	else:
		ClientSocket.send(str.encode(Input))
		Response = ClientSocket.recv(1024)
		print (Response.decode("utf-8"))


ClientSocket.close()
