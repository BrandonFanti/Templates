from .muta_funcs import (
    muta_tx,
    muta_rx,
    transaction
)

def apply_transaction(obj, transaction_function=transaction):
    obj.transaction = transaction

def overload_rx_tx(obj):
    filter_client.receive       = muta_rx
    filter_client.send          = muta_tx


def muta_all(client):
    # "New class"
    filter_client               = client

    # *New* function
    filter_client.transaction   = transaction

    # "Alternative functions" (overloading)
    filter_client.receive       = muta_rx
    filter_client.send          = muta_tx

    return filter_client