def on_connected_to_server():
    print("Клиент подключился к серверу.")


def on_connection_closed():
    print("Произошёл разрыв соединения с сервером.")


def on_data_sent():
    print(f"Данные отправлены.")


def on_data_get():
    print("Получены данные с сервера.")
