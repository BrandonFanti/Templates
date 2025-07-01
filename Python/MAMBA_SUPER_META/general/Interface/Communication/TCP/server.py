from .functions import (
    listen,
    send,
    receive,
)

from ..base.server import server

class server(server):
    sock = None
    target = None

    def __init__(self, *args, host=None, port=None, **kwargs):
        if host:
            self.host = None
            if port:
                self.port = port
                self.target = (host, port)
                self.listen(*self.target)

    def listen(self, host, port, **kwargs):
        self.sock = listen(host, port, **kwargs)

    def accept(self):
        return self.sock.accept()

    def send(self, message):
        send(self.sock, message)

    def receive(self, **kwargs):
        return receive(
            self.sock,
            **kwargs
        )