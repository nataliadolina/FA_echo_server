from settings_data_utils import get_saved_ports, default_server_settings, default_client_settings
from server_ports_container import save_port
import re

default_settings = {True: default_server_settings, False: default_client_settings}


def request_connection_settings():
    host = input("Введите имя хоста.")
    port = input("Введите имя порта.")
    return host, port


def check_host(hostname):
    if len(hostname) > 255 or len(hostname) < 1:
        return False
    if hostname[-1] == ".":
        hostname = hostname[:-1]
    allowed = re.compile("(?!-)[A-Z\d-]{1,63}(?<!-)$", re.IGNORECASE)
    return all(allowed.match(x) for x in hostname.split("."))


def check_port(port, from_server):
    if from_server:
        return port.isdigit() and port not in get_saved_ports("str")
    return port.isdigit() and port in get_saved_ports("str")


def check_settings(_settings, from_server):
    host, port = _settings
    is_valid_host, is_valid_port = check_host(host), check_port(port, from_server)
    if not is_valid_host:
        host = default_settings[from_server][0]()
        print(f"Хост установился автоматически - {host}")
    if not is_valid_port:
        port = default_settings[from_server][1]()
        print(f"Порт установился автоматически - {port}")
    return host, int(port)


def set_connection_settings(socket, from_server=False):
    def get_bind_func():
        binders = {True: socket.bind, False: socket.connect}
        return binders[from_server]

    settings = request_connection_settings()
    settings = check_settings(settings, from_server)
    get_bind_func()(settings)
    host, port = settings
    if from_server:
        save_port(port)
    return host, port
