default_client_settings = ("localhost", 9090)
default_server_settings = ("", 9090)


def request_connection_settings():
    host = input("Введите имя хоста.")
    port = input("Введите имя порта.")
    return host, port


def write_to_file(filename, data):
    with open(f"txt/{filename}", 'a+', encoding="UTF-8") as file:
        file.write(data)


def set_connection_settings(default, binding_func):
    settings = request_connection_settings()
    try:
        binding_func(settings)
    except Exception as e:
        print(f"Возникло исключеение {e}")
        print("Установлено значение по умолчанию")
        binding_func(default)


def encode(string):
    return str.encode(string, "UTF-8")


def decode(bytes):
    return bytes.decode()
