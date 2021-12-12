import socket
from server_callbacks import log
from connection_settings import set_connection_settings_and_bind
from hosts_container import get_nickname
from data_type_manager import encode, decode
from file_manager import reset_all
from threading import Thread
from server_commands import commands

connected_clients = []


def send_msg(sender_addr, getter_addr, conn, data):
    nickname = get_nickname(sender_addr)
    msg = f"[{nickname}]: " + decode(data)
    try:
        print(msg)
        conn.sendto(encode(msg), getter_addr)
    except Exception as e:
        print("Возникло исключение " + e.__repr__())


def accept_incoming_data():
    while 1:
        conn, addr = _sock.accept()
        host = conn.getsockname()
        if addr not in connected_clients:
            connected_clients.append(host)
        log("connected")
        log("data_get")
        data = conn.recv(1024)
        print(data)
        for client in connected_clients:
            print(client)
            send_msg(host[0], client, conn, data)
        log("data_send")


if __name__ == "__main__":
    reset_all()
    _sock = socket.socket()
    port = set_connection_settings_and_bind(_sock, from_server=True)
    print(f"Сервер подключён к порту {port}")
    loaded = True
    log("loaded")

    _sock.listen(5)
    log("listen")
    MAIN_THREAD = Thread(target=accept_incoming_data)
    COMMANDS_THREAD = Thread(target=commands)
    MAIN_THREAD.start()
    COMMANDS_THREAD.start()
    MAIN_THREAD.join()
    COMMANDS_THREAD.join()
