import socket
import time
import pickle

data = {1: "Hey", 2: "There"}
msg = pickle.dumps(data)

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1235))
s.listen(5)

while True:
	clientsocket, address = s.accept()
	print(f"Connection form {address} has been established!")

	data = {1: "Hey", 2: "There"}
	msg = pickle.dumps(data)

	msg = bytes(f'{len(msg):<{HEADERSIZE}}', "utf-8") + msg

	clientsocket.send(msg)
