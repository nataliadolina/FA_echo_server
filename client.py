import socket
import client_callbacks
from data_type_manager import encode, decode
from connection_settings import set_connection_settings
from threading import Thread
from auth_register import auth


def try_to_close_client():
    global loaded
    global sock
    string = input("Type stop to close connection")
    if string == "stop":
        sock.close()
        client_callbacks.on_connection_closed()
        loaded = False
    return


def read_sock():
    while 1:
        client_callbacks.on_data_get()
        data = sock.recv(1024)
        print(f"От сервера пришло сообщение {decode(data)}")


def send_data():
    while 1:
        sock.send(encode(input("Что отошлём серверу?")))
        client_callbacks.on_data_sent()


if __name__ == "__main__":
    sock = socket.socket()
    host = set_connection_settings(sock, from_server=False)[0]
    client_callbacks.on_connected_to_server()
    auth(host)
    READ_SOCK = Thread(target=read_sock)
    READ_SOCK.start()
    SEND_DATA = Thread(target=send_data())
