import os
from file_manager import read_from_file, clear_file


def cls():
    return os.system('cls' if os.name == 'nt' else 'clear')


def clauth():
    clear_file("saved_hosts.csv")
    print(f"[INFO] Successfully cleaned log file")
    return


def rdlog():
    data = read_from_file("log.txt")
    if data:
        print("[INFO] server logs:")
        print("\n".join(data))
    else:
        print("[INFO]You have no logs")


def cllog():
    clear_file("log.txt")
    print(f"[INFO] Successfully cleaned log file")
    return


def help():
    print("\n".join(read_from_file("commands_instruction.txt")))
    return


commands_dict = {"csl": cls, "rdlog": rdlog, "cllog": cllog, "clauth": clauth, "help": help}


def commands():
    print("Вы можете вводить команды для управления сервером. Введите help, чтобы получить документацию.")
    while 1:
        try:
            n = input()
            if n.isspace() or n == "":
                continue
            commands_dict[n]()
        except:
            print("[ERROR]Got unknown command")
            continue
