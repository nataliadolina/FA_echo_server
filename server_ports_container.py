from data_type_manager import to_type
from file_manager import write_to_file, read_from_file

saved_ports = []


def save_port(port):
    write_to_file("saved_ports.txt", str(port), "a+")


def get_saved_ports(type):
    print(read_from_file("saved_ports.txt"))
    return [to_type(type, i) for i in read_from_file("saved_ports.txt")]


def delete_port(port):
    if port in saved_ports:
        saved_ports.remove(port)
