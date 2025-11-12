from .functions import (
    connect,
    send,
    receive,
)

from ..base.client import client

class client(client):
    sock = None
    host=None
    port=None
    target = None

    def __init__(self, *args, host=None, port=None, **kwargs):
        if host:
            self.host = None
            if port:
                self.port = port
                self.target = (host, port)
                self.connect(*self.target)

    def connect(self, host, port):
        self.sock = connect(host, port)

    def send(self, message):
        send(self.sock, message)

    def receive(self, size=512):
        return receive(
            self.sock, 
            size=size
        )