import socket
import client_callbacks
from common_func import encode, decode, set_connection_settings, default_client_settings

sock = socket.socket()
set_connection_settings(default_client_settings, sock.connect)
client_callbacks.on_connected_to_server()

sock.send(encode(input("Что отошлём клиенту?")))
client_callbacks.on_data_sent()

data = sock.recv(1024)
client_callbacks.on_data_get()

sock.close()
client_callbacks.on_connection_closed()

print(decode(data))
