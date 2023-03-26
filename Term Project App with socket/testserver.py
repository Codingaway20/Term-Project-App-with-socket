import socket

# create a socket object
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#get the hostname of your laptop
host = "192.168.159.1"

port = 4000

# connection to hostname on the port.
clientsocket.connect((host, port))

# send a hello message to the server
clientsocket.sendall('hello server'.encode())

# receive data from the server
data = clientsocket.recv(1024).decode()

clientsocket.close()

print(data)
