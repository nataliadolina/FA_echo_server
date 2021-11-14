from hosts_container import write_host_password


def write_to_file(filename, data, mode):
    with open(f"txt/{filename}", mode, encoding="UTF-8") as file:
        file.write(data)


def read_from_file(filename):
    with open(f"txt/{filename}", 'r', encoding="UTF-8") as file:
        res = [i.strip() for i in file.readlines()]
        return res


def clear_file(filename):
    with open(f"txt/{filename}", 'w+', encoding="UTF-8") as file:
        file.write('')


def reset_all():
    clear_file("saved_ports.txt")
    clear_file("log.txt")
