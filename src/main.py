from blockchain import Blockchain
from utils import create_block, new_transaction, create_dummy_address
from colors import END, CYAN


def showcase():
    blockchain = Blockchain()
    print(CYAN + f"Chain with length {len(blockchain.chain)}" + END)
    sender = create_dummy_address()
    receiver = create_dummy_address()
    new_transaction(blockchain, sender, receiver, 1)
    create_block(blockchain, receiver, True)
    new_transaction(blockchain, sender, receiver, 2)
    new_transaction(blockchain, sender, receiver, 3)
    create_block(blockchain, receiver, True)
    new_transaction(blockchain, sender, receiver, 4)


if __name__ == "__main__":
    showcase()
