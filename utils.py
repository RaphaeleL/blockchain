from blockchain import Blockchain
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
        recipient=receipient_node_identifier,
        amount=1,
    )
    previous_hash = blockchain.hash(last_block)
    block = blockchain.new_block(proof, previous_hash)
    if debug:
        print(f"New Block mined at index: {block['index']}")
        print(f"> Transactions: {block['transactions']}")
        print(f"> Proof: {block['proof']}")
        print(f"> Previous Hash: {block['previous_hash']}")

    return block


def new_transaction(
    blockchain: Blockchain,
    sender: str,
    recipient: str,
    amount: int,
    debug: bool = False,
) -> dict:
    """Add a new Transaction"""
    index = blockchain.new_transaction(sender, recipient, amount)
    if debug:
        print(f"Transaction will be added to Block {index}")
    return index


def chain(blockchain: Blockchain, debug: bool = False):
    """Get the Chain"""
    if debug:
        print(f"Chain with length ({len(blockchain.chain)})")
        for item in blockchain.chain:
            print(f"> {item}")
    return {
        "chain": blockchain.chain,
        "length": len(blockchain.chain),
    }


def create_id() -> str:
    return uuid4().hex
