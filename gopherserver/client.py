import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 8070)

sock.connect(server_address)

try:
    
  # Send data
  # ' ' used to denoted an empty request. This is due to python interpreting '' as a 0 byte package witch causes server to hang
  message = 'getFileTwo'
  sock.sendall(bytes(message.encode('utf-8')))

  total_response = ''

  while not total_response.endswith('.'):
    data = sock.recv(1024)
    total_response += data.decode('utf-8')

  print(total_response)

finally:
  print("closing socket")
  sock.close()