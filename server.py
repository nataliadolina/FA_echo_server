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


client = []  # Массив где храним адреса клиентов
_conn = None


def accept_incoming_connections():
    while 1:
        conn, addr = _sock.accept()
        _conn = conn
        log("connected")
        log("data_get")
        if addr not in client:
            client.append(addr)


def receive_clients_data():
    while 1:
        if _conn:
            data = _conn.recv(1024)
            for clients in client:
                _sock.sendto(data, clients)
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
    MAIN_THREAD = Thread(target=receive_clients_data, args=[])
    MAIN_THREAD.start()
    ACCEPT_ClIENTS_THREAD.start()
    MAIN_THREAD.join()
    MAIN_THREAD.join()
