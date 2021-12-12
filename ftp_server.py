import socket
import sys
import time
import os
from server_commands import commands_dict
from dir_settings import dirname
from dir_commands import dir_commands
from server_callbacks import log
from connection_settings import set_connection_settings
from data_type_manager import encode, decode
from file_manager import reset_all
from threading import Thread


def run_server(host="", port=53210):
    def accept_client_conn(serv_sock, cid):
        client_sock, client_addr = serv_sock.accept()
        print(f'Client #{cid} connected '
              f'{client_addr[0]}:{client_addr[1]}')
        return client_sock

    serv_sock = create_serv_sock(host, port)
    cid = 0
    while True:
        client_sock = accept_client_conn(serv_sock, cid)
        t = Thread(target=serve_client, args=(serv_sock, client_sock, cid))
        print("Client connected")
        t.start()
        cid += 1


def serve_client(serv_sock, client_sock, cid):
    while True:
        request = read_request(client_sock)
        if request is None:
            print(f'Client #{cid} unexpectedly disconnected')
            break
        else:
            req = decode(request)
            if 'exit' in req:
                write_response_close(client_sock, encode('exit'), cid)
                break
            if 'sstop' in req:
                write_response_closes(serv_sock, client_sock, encode('cstop'), cid)
                break

            response = handle_request(req)
            write_response(client_sock, response)


def read_request(client_sock):
    request = bytearray()
    try:
        request = client_sock.recv(1024)
        if not request:
            # Клиент преждевременно отключился.
            return None
        log("data_get")
        return request

    except ConnectionResetError:
        # Соединение было неожиданно разорвано.
        return None
    except:
        raise


def handle_request(request):
    def parse(req):
        return " ".join(req.split()[1:])

    def process(req):
        print(f"Получен реквест - {req}. Ключи - {dir_commands.keys()}")
        if req == 'pwd':
            return dirname
        elif req == 'ls':
            return '; '.join(os.listdir(dirname))

        elif req in commands_dict.keys():
            return commands_dict[req]()

        elif req.split()[0] in dir_commands.keys():
            command, *args = req.split()
            return dir_commands[command](args)
        return 'bad request'

    print(request)
    # time.sleep(5)
    return process(parse(request))


def handle_commands(request):
    commands_dict[request]()


def write_response(client_sock, response):
    print("Writing response - " + response)
    client_sock.sendall(encode(response))
    log("data_send")


def create_serv_sock(serv_host, serv_port):
    serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
    serv_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    log("connected")

    serv_sock.bind((serv_host, serv_port))
    log("loaded")
    serv_sock.listen()
    log("listen")
    return serv_sock


def write_response_close(client_sock, response, cid):
    client_sock.sendall(response)
    client_sock.close()
    print(f'Client #{cid} has been served')


def write_response_closes(serv_sock, client_sock, response, cid):
    client_sock.sendall(response)
    client_sock.close()
    serv_sock.close()
    print(f'Client #{cid} has been stopped server')
    log("stop")
    os._exit(0)


if __name__ == '__main__':
    reset_all()
    host, port = set_connection_settings(True)
    run_server(host, port)
