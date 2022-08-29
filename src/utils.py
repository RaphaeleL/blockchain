from __future__ import print_function
import builtins as __builtin__
from blockchain import Blockchain
from colors import Colors
from uuid import uuid4


def mine(
    blockchain: Blockchain, receipient_node_identifier: str, debug: bool = False
) -> dict:
    """Mine a new Block"""
    last_block = blockchain.last_block
    # last_proof = last_block["proof"]
    proof = blockchain.proof_of_work(last_block)
    blockchain.new_transaction(
        sender="0",
        receiver=receipient_node_identifier,
        amount=1,
    )
    previous_hash = blockchain.hash(last_block)
    block = blockchain.new_block(proof, previous_hash)
    print(Colors.WARNING + f"New Block mined at index: {block['index']}" + Colors.ENDC)
    if debug:
        # print(f"> Transactions: {block['transactions']}")
        print(f"> Transactions:")
        for transaction in block["transactions"]:
            print(f"  > {transaction}")
        print(f"> Proof: {block['proof']}")
        print(f"> Previous Hash: {block['previous_hash']}")
    _ = chain(blockchain)
    return block


def new_transaction(
    blockchain: Blockchain,
    sender: str,
    receiver: str,
    amount: int,
) -> dict:
    """Add a new Transaction"""
    index = blockchain.new_transaction(sender, receiver, amount)
    print(Colors.OKGREEN + f"Transaction will be added to Block {index}" + Colors.ENDC)
    return index


def chain(blockchain: Blockchain, debug: bool = False) -> dict:
    """Get the Chain"""
    print(Colors.OKCYAN + f"Chain with length {len(blockchain.chain)}" + Colors.ENDC)
    if debug:
        for item in blockchain.chain:
            print(f"> {item}")
    return {
        "chain": blockchain.chain,
        "length": len(blockchain.chain),
    }


def create_id() -> str:
    return uuid4().hex


# def print(*args, **kwargs):
# """My custom print() function."""
# __builtin__.print("My overridden print() function!")
# return __builtin__.print(*args, **kwargs)
