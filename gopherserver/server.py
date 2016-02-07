import socket
import logging
from GopherProtocolHandler import GopherProtocolHandler

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 8070)
sock.bind(server_address)



sock.listen(1)
while True:
	connection, client_address = sock.accept()
	try:
		while True:
			GPH = GopherProtocolHandler()
			data = connection.recv(1024)
			if data:
				GPH.resolve_gquery(data.decode("utf-8"))
				retData = GPH.get_result_strings()
				connection.sendall(bytes(retData.encode("utf-8")))
			else:
				break
	finally:
		# Clean up the connection
		connection.close()