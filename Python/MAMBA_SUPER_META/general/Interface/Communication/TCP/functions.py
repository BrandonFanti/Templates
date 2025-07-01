import socket 

def listen(host, port, connection_limit=1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(connection_limit)  # allow only one connection at a time
    return sock

def connect(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    return sock

def send(sock, message):
    if sock:
        sock.sendall(message.encode('utf-8'))
    else:
        raise Exception("Not connected!")

def receive(sock, size=1024):
    if sock:
        data = sock.recv(size).decode('utf-8')
        return data
    else:
        raise Exception("Not connected!")
