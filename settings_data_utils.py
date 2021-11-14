from file_manager import write_to_file, read_from_file
from data_type_manager import to_type
import random
from server_ports_container import get_saved_ports
from hosts_container import get_saved_hosts


def get_free_server():
    p = get_saved_ports("int")
    print(p)
    print(p[random.randint(0, len(p)-1)])
    return p[random.randint(0, len(p)-1)]


def get_default_server_host():
    return ""


def generate_unique_port():
    saved_ports = get_saved_ports("int")
    if not saved_ports:
        return default_port
    print(max(saved_ports) + 1)
    return max(saved_ports) + 1


def generate_unique_host():
    def generate():
        res = "127."
        for i in range(3):
            res += str(random.randint(0, 255))
            if i != 2:
                res += "."
        return res

    res = generate()
    while res in get_saved_hosts():
        res = generate()
    return res


default_port = 9090
default_client_settings = (generate_unique_host, get_free_server)
default_server_settings = (get_default_server_host, generate_unique_port)
