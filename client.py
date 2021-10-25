import socket
from byte_converter import encode, decode

sock = socket.socket()
sock.connect(('localhost', 9090))
sock.send(encode('hello, world!'))
data = sock.recv(1024)
sock.close()
print(decode(data))