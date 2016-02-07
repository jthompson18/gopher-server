import socket
import logging
from GopherProtocolHandler import GopherProtocolHandler

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 8070)
sock.bind(server_address)

GPH = GopherProtocolHandler()

sock.listen(1)
while True:
	connection, client_address = sock.accept()
	try:
		while True:
			data = connection.recv(1024)
			GPH.resolve_gquery(data)
			retData = GPH.get_result_strings()
			connection.sendall(retData)
	finally:
		# Clean up the connection
		connection.close()