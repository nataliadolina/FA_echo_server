import socket
from server_callbacks import log
from connection_settings import set_connection_settings
from server_ports_container import delete_port
from file_manager import reset_all
from threading import Thread


def try_to_stop_server(string, conn):
    global loaded
    if string == "stop":
        conn.close()
        log("stop")
        loaded = False
        delete_port(port)
    return


def accept_incoming_connections():
    while 1:
        conn, addr = _sock.accept()
        log("connected")
        log("data_get")
        data = conn.recv(1024)
        conn.sendto(data, addr)
        log("data_send")


if __name__ == "__main__":
    reset_all()
    _sock = socket.socket()
    port = set_connection_settings(_sock, from_server=True)
    print(f"Сервер подключён к порту {port}")
    loaded = True
    log("loaded")

    _sock.listen(5)
    log("listen")
    ACCEPT_ClIENTS_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_ClIENTS_THREAD.start()
    ACCEPT_ClIENTS_THREAD.join()
