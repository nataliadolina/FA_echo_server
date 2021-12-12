import socket
import os
import socket
import client_callbacks
from data_type_manager import encode, decode
from connection_settings import set_connection_settings
from auth_register import auth
from hosts_container import get_nickname

HOST = None
PORT = None


def run_client(host, port):
    while True:
        try:
            request = input('>')
        except:
            break
        sock = socket.socket()
        try:
            sock.connect((host, port))
        except:
            break
        sock.send(encode_request(host, request))
        client_callbacks.on_data_sent()
        try:
            response = decode(sock.recv(1024))
        except Exception as e:
            print(f"Error occurred on client receiving data {e}")
            break
        else:
            client_callbacks.on_data_get()
            if response == 'exit' or response == 'cstop':
                break
            print(response)

        sock.close()
        client_callbacks.on_connection_closed()


def encode_request(host, req):
    return encode(f"[{get_nickname(host)}]: " + req)


if __name__ == "__main__":
    sock = socket.socket()
    host, port = set_connection_settings()
    client_callbacks.on_connected_to_server()
    auth(host)
    run_client(host, port)