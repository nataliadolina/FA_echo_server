from common_func import write_to_file

log_filename = "log.txt"
msg_dict = {"loaded": "Сервер запущен.", "listen": "Происходит прослушивание порта.", "connected": "Клиент подключён.",
            "data_get": "Получены данные от клиента.", "data_send": "Данные отправлены.",
            "stop": "Произошла остновка сервера."}


def log(msg_key):
    write_to_file(log_filename, msg_dict[msg_key])
    write_to_file(log_filename, "\n")
