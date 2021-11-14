from hosts_container import write_host_password, get_password, get_nickname, get_saved_hosts
from data_type_manager import to_hash


def request_account_settings():
    nickname = input("Пожалуйста, введите никнэйм")
    p = to_hash(input("Пожалуйста, придумайте пароль для нового клиента"))
    return nickname, p


def register(addr):
    data = request_account_settings()
    write_host_password([addr, data[0], data[1]])
    print("Пользователь успешно зарегестрирован.")


def auth(addr):
    if addr not in get_saved_hosts():
        register(addr)
    correct_password = get_password(addr)
    p = to_hash(input("Пожалуйста, введите пароль."))
    while p != correct_password:
        p = input("Пароль неверный. Пожалуйста, введите пароль.")
    nickname = get_nickname(addr)
    print(f"Привет, {nickname}")
    return nickname
