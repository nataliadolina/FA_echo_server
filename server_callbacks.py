def on_server_loaded():
    print("Сервер запущен.")


def on_server_start_listening():
    print("Происходит прослушивание порта.")


def on_client_connected(adrs):
    print(f"Клиент {adrs} подключён.")


def on_get_data_from_client():
    print("Получены данные от клиента.")


def on_server_data_send():
    print("Данные отправлены.")


def on_client_disconnected():
    print("Клиент отключился.")


def on_server_stop():
    print("Произошла остновка сервера")
