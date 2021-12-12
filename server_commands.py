import os
from file_manager import read_from_file, clear_file


def clauth():
    clear_file("saved_hosts.csv")
    return f"[INFO] Successfully cleaned log file"


def rdlog():
    data = read_from_file("log.txt")
    if data:
        return "[INFO] server logs: \n" + "\n".join(data)
    return "[INFO]You have no logs"


def cllog():
    clear_file("log.txt")
    return f"[INFO] Successfully cleaned log file"


def help():
    return "\n".join(read_from_file("commands_instruction.txt"))



commands_dict = {"rdlog": rdlog, "cllog": cllog, "clauth": clauth, "help": help}