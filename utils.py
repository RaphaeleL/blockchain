from blockchain import Blockchain
from uuid import uuid4


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


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
    print(
        bcolors.WARNING + f"New Block mined at index: {block['index']+1}" + bcolors.ENDC
    )
    if debug:
        print(f"> Transactions: {block['transactions']}")
        print(f"> Proof: {block['proof']}")
        print(f"> Previous Hash: {block['previous_hash']}")
    _ = chain(blockchain)
    return block


def new_transaction(
    blockchain: Blockchain,
    sender: str,
    recipient: str,
    amount: int,
) -> dict:
    """Add a new Transaction"""
    index = blockchain.new_transaction(sender, recipient, amount)
    print(
        bcolors.OKGREEN + f"Transaction will be added to Block {index}" + bcolors.ENDC
    )
    return index


def chain(blockchain: Blockchain, debug: bool = False):
    """Get the Chain"""
    print(bcolors.OKCYAN + f"Chain with length {len(blockchain.chain)}" + bcolors.ENDC)
    if debug:
        for item in blockchain.chain:
            print(f"> {item}")
    return {
        "chain": blockchain.chain,
        "length": len(blockchain.chain),
    }


def create_id() -> str:
    return uuid4().hex
