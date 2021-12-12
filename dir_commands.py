import os
from dir_settings import dirname, server_folder, client_folder


def create_directory(string):
    string = string[0]
    try:
        dir = server_folder + to_dir(string)
        os.mkdir(dir, mode=0o777, dir_fd=None)
    except FileExistsError:
        return "[ERROR]: Директория уже существует"
    return f"[INFO]: Успешно создана директория {dir}"


def remove_directory(string):
    string = string[0]
    try:
        dir = server_folder + to_dir(string)
        os.rmdir(dir, dir_fd=None)

    except FileNotFoundError:
        return "[ERROR]: Директория не найдена"
    return f"[INFO]: Успешно удалена директория {dir}"


def to_dir(string):
    if string[0] != "/":
        string = "/" + string

    return string


def read_file_data(filepath):
    with open(filepath, "rt", encoding="UTF-8") as file:
        return file.read()


def write_file_data(filenamepath, data):
    with open(filenamepath, "wt", encoding="UTF-8") as file:
        file.write(data)


def create_file(args):
    filename = args[0]
    try:
        with open(server_folder + to_dir(filename), mode="w+"):
            return f"[INFO]: New file {filename} created on server!"
    except Exception as e:
        return f"[ERROR]: Exception occurred {e}."


def delete_file(filename):
    try:
        os.remove(server_folder + to_dir(filename[0]))
    except Exception as e:
        return f"[ERROR]: File with name {filename[0]} does not exist."
    return f"[INFO]: File {filename[0]} was deleted successfully."


def move_file(args):
    dir1, dir2 = args
    if dirname not in dir2:
        return f"[ERROR]: File cannot be moved outside root directory - {dirname}."
    try:
        os.replace(dir1, dir2)
    except Exception as e:
        return f"[ERROR]: Exception occurred {e}."
    return f"[INFO]: File moved successfully."


def copy_to_server(filename):
    return copy_file_to_folder(client_folder + to_dir(filename[0]), server_folder)


def copy_to_client(filename):
    return copy_file_to_folder(server_folder + to_dir(filename[0]), client_folder)


def copy_file_to_folder(path1, path2):
    try:
        data = read_file_data(path1)  # считываем данные из файла, который хотим копировать
        move_file([path1, path2])  # перемещаем файл в папку, куда хотим копировать
        write_file_data(path1, data)  # восстанавливаем перемещённый файл в прошлой директории
    except Exception as e:
        return f"[ERROR]: Exception occurred {e}."
    return f"[INFO]: File {path1} was copied to {path2} successfully."


def rename_file(filename_new_filename):
    filename, new_filename = filename_new_filename
    try:
        print(server_folder + to_dir(filename), server_folder + to_dir(new_filename))
        os.rename(server_folder + to_dir(filename), server_folder + to_dir(new_filename))
    except Exception as e:
        return f"[ERROR]: Exception occurred {e}."
    return f"[INFO]: File {filename} was successfully renamed."


def show_file_data(filename):
    try:
        data = read_file_data(server_folder + to_dir(filename[0]))
    except Exception as e:
        return f"[ERROR]: File {filename} is not found."
    return f"[INFO]: Data from {filename}: \n {data}"


dir_commands = {"mkdir": create_directory, "rmdir": remove_directory, "touch": create_file, "rm": delete_file,
                "cpserver": copy_to_server, "cpclient": copy_to_client, "rename": rename_file, "cat": show_file_data}
