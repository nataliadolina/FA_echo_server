import socket
import client_callbacks
from common_func import encode, decode, set_connection_settings


def try_to_close_client():
    global loaded
    global sock
    string = input("Type stop to close connection")
    if string == "stop":
        sock.close()
        client_callbacks.on_connection_closed()
        loaded = False
    return


loaded = True
sock = socket.socket()
set_connection_settings(sock, from_server=False)
client_callbacks.on_connected_to_server()

while loaded:
    sock.send(encode(input("Что отошлём клиенту?")))
    client_callbacks.on_data_sent()

    data = sock.recv(1024)
    client_callbacks.on_data_get()
    print(decode(data))
    try_to_close_client()
