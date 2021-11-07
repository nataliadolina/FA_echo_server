import socket
import random


def get_free_server():
    p = get_saved_ports("int")
    print(p[random.randint(0, len(p) - 1)])
    return p[random.randint(0, len(p) - 1)]


def generate_unique_port():
    saved_ports = get_saved_ports("int")
    if not saved_ports:
        return default_port
    print(max(saved_ports) + 1)
    return max(saved_ports) + 1


default_port = 9090
default_client_settings = ("127.0.0.1", get_free_server)
default_server_settings = ("", generate_unique_port)


def request_connection_settings():
    host = input("Введите имя хоста.")
    port = input("Введите имя порта.")
    return host, port


def write_to_file(filename, data, mode):
    with open(f"txt/{filename}", mode, encoding="UTF-8") as file:
        file.write(data)


def read_from_file(filename):
    with open(f"txt/{filename}", 'r', encoding="UTF-8") as file:
        res = [i.strip() for i in file.readlines()]
        return res


def save_port(port):
    write_to_file("saved_ports.txt", str(port) + "\n", 'a+')


def clear_port(_port):
    ports = [str(port) for port in get_saved_ports("int") if port != _port]
    res = ""
    for p in ports:
        res += p + "\n"
    write_to_file("saved_ports.txt", res, "w")


def to_type(type, el):
    if type == "str":
        return str(el)
    if type == "int":
        return int(el)
    return el


def get_saved_ports(type):
    return [to_type(type, i) for i in read_from_file("saved_ports.txt") if i.isdigit()]


def set_connection_settings(socket, from_server=False):
    def check_settings(_settings):
        if from_server and _settings[1] in get_saved_ports("str"):
            return False
        if not _settings[1].isdigit():
            return False
        if not from_server and not _settings[0].isdigit() and _settings[0] != default_client_settings[0]:
            return False
        if from_server and not _settings[0].isdigit() and _settings[0] != default_server_settings[1]:
            return False
        return True

    settings = request_connection_settings()
    default_settings = {True: {"default_settings": default_server_settings, "binding_func": socket.bind},
                        False: {"default_settings": default_client_settings, "binding_func": socket.connect}}

    if not check_settings(settings):
        print("Хост и порт установились автоматически.")
        settings = default_settings[from_server]["default_settings"]
        settings = settings[0], settings[1]()
    default_settings[from_server]["binding_func"](settings)
    host, port = settings
    if from_server:
        save_port(port)
    return port


def encode(string):
    return str.encode(string, "UTF-8")


def decode(bytes):
    return bytes.decode()
