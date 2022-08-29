from blockchain import Blockchain
from colors import YELLOW, END, GREEN, CYAN
from uuid import uuid4


def create_block(blockchain: Blockchain, receiver: str, debug: bool = False) -> dict:
    """Mine / Create a new Block"""
    last_block = blockchain.last_block
    proof = blockchain.proof_of_work(last_block)
    blockchain.new_transaction(
        sender="genesis",
        receiver=receiver,
        amount=1,
    )
    previous_hash = blockchain.hash(last_block)
    block = blockchain.new_block(proof, previous_hash)
    print(YELLOW + f"New Block mined with index: {block['index']}" + END)
    if debug:
        print("> Transactions:")
        for transaction in block["transactions"]:
            print(f"  > {transaction}")
        print(f"> Proof: {block['proof']}")
        print(f"> Previous Hash: {block['previous_hash']}")
        print(CYAN + f"Chain with length {len(blockchain.chain)}" + END)
    return block


def new_transaction(
    blockchain: Blockchain,
    sender: str,
    receiver: str,
    amount: int,
) -> dict:
    """Add a new Transaction"""
    index = blockchain.new_transaction(sender, receiver, amount)
    print(GREEN + f"Transaction will be added to Block {index}" + END)
    return index


def print_chain_length(blockchain: Blockchain):
    """Get the Chain"""
    print(CYAN + f"Chain with length {len(blockchain.chain)}" + END)


def create_dummy_address() -> str:
    return uuid4().hex
