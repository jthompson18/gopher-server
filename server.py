import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 8070)
sock.bind(server_address)

sock.listen(1)
while True:
	connection, client_address = sock.accept()
	try:
		# Receive the data in small chunks and retransmit it
		while True:
			data = connection.recv(1024)
			if data:
				connection.sendall(data)
			else:
				break
	finally:
		# Clean up the connection
		connection.close()