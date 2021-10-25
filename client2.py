import socket
from byte_converter import encode, decode

sock = socket.socket()
sock.connect(('127.0.0.2', 9090))
sock.send(encode('I am here!'))
data = sock.recv(1024)
sock.close()
print(decode(data))
