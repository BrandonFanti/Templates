from ..TCP.functions import (
    send,
    receive
)

def muta_tx(client, message):
    if 'bad word' in message:
        raise Exception("We don't abide!")
    send(client.sock, message)


def muta_rx(client, **kwargs):
    if kwargs.get('size', 1024) > 1024:
        raise Exception("Too big!")
    receive(client.sock, **kwargs)



def transaction(client, message):
    client.send(message)
    return muta_rx(client.sock)

