import socket
from server_callbacks import log
from common_func import set_connection_settings, clear_port

sock = socket.socket()
port = set_connection_settings(sock, from_server=True)
print(f"Сервер подключён к порту {port}")
loaded = True
log("loaded")

sock.listen(3)
log("listen")


def try_to_stop_server(string, conn):
    global loaded
    if string == "stop":
        conn.close()
        log("stop")
        loaded = False
        clear_port(port)
    return


while loaded:
    conn, addr = sock.accept()
    log("connected")
    data = conn.recv(1024)
    log("data_get")
    if data:
        conn.send(data.upper())
        log("data_send")
    continue

    # try_to_stop_server(input("Type stop to close connection "), conn)
