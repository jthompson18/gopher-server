import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 8070)

sock.connect(server_address)

try:
    
  # Send data
  message = 'This is the message.  It will be repeated.'
  sock.sendall(bytes(message.encode('utf-8')))

  # Look for the response
  amount_received = 0
  amount_expected = len(message)
  
  while amount_received < amount_expected:
    data = sock.recv(1024)
    amount_received += len(data)

finally:
  print("closing socket")
  sock.close()