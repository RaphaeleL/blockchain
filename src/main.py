from blockchain import Blockchain
from utils import mine, new_transaction, chain, create_id


def showcase_mining():
    blockchain = Blockchain()
    receipient_node_identifier = create_id()
    while True:
        _ = mine(blockchain, receipient_node_identifier, True)


def showcase_transactions():
    blockchain = Blockchain()
    _ = chain(blockchain)
    sender_node_identifier = create_id()
    receipient_node_identifier = create_id()
    _ = new_transaction(
        blockchain, sender_node_identifier, receipient_node_identifier, 1
    )
    _ = mine(blockchain, receipient_node_identifier, True)
    _ = new_transaction(
        blockchain, sender_node_identifier, receipient_node_identifier, 1
    )
    _ = new_transaction(
        blockchain, sender_node_identifier, receipient_node_identifier, 1
    )
    _ = mine(blockchain, receipient_node_identifier, True)
    _ = new_transaction(
        blockchain, sender_node_identifier, receipient_node_identifier, 1
    )


if __name__ == "__main__":
    showcase_transactions()
    # showcase_mining()
