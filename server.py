import socket
import server_callbacks
from common_func import set_connection_settings, default_server_settings, write_to_file

sock = socket.socket()
set_connection_settings(default_server_settings, sock.bind)
server_callbacks.on_server_loaded()

sock.listen(1)
server_callbacks.on_server_start_listening()


def try_to_stop_server(string, conn):
    if string == "stop":
        conn.close()


while True:
    conn, addr = sock.accept()
    server_callbacks.on_client_connected(addr)
    data = conn.recv(1024)
    server_callbacks.on_get_data_from_client()
    if data:
        conn.send(data.upper())
        server_callbacks.on_server_data_send()

    try_to_stop_server(input("Type stop to close connection"), conn)
