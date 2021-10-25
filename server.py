import socket
from server_callbacks import log
from common_func import set_connection_settings, default_server_settings

sock = socket.socket()
set_connection_settings(default_server_settings, sock.bind)
loaded = True
log("loaded")

sock.listen(1)
log("listen")


def try_to_stop_server(string, conn):
    global loaded
    if string == "stop":
        conn.close()
        log("stop")
        loaded = False


while loaded:
    conn, addr = sock.accept()
    log("connected")
    data = conn.recv(1024)
    log("data_get")
    if data:
        conn.send(data.upper())
        log("data_send")

    try_to_stop_server(input("Type stop to close connection"), conn)
