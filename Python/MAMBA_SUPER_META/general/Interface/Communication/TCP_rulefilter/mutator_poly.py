from ..TCP.client import client

from .muta_funcs import (
    muta_tx,
    muta_rx,
    transaction
)

# "New class"
filter_client               = client

# *New* function
filter_client.transaction   = transaction

# "Alternative functions" (overloading)
filter_client.receive       = muta_rx
filter_client.send          = muta_tx
