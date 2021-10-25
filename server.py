import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)

while True:
    conn, addr = sock.accept()
    print(f"User {addr} connected")
    data = conn.recv(1024)
    if data:
        conn.send(data.upper())
