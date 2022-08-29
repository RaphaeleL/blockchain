import hashlib
from time import time
from uuid import uuid4
import json


class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.new_block(previous_hash=1, proof=100)

    def new_transaction(self, sender: str, recipient: str, amount: int) -> dict:
        """Creates a new Block and adds it to the chain"""
        self.current_transactions.append(
            {
                "sender": sender,
                "recipient": recipient,
                "amount": amount,
            }
        )
        return self.last_block["index"] + 1

    def new_block(self, proof: int, previous_hash: str = None) -> dict:
        """Creates a new Block and adds it to the chain"""
        block = {
            "index": len(self.chain) + 1,
            "timestamp": time(),
            "transactions": self.current_transactions,
            "proof": proof,
            "previous_hash": previous_hash or self.hash(self.chain[-1]),
        }
        self.current_transactions = []
        self.chain.append(block)
        return block

    @staticmethod
    def hash(block: dict) -> str:
        """Hashes a Block"""
        # We must make sure that the Dictionary is Ordered,
        # or we'll have inconsistent hashes
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        """Returns the last Block in the chain"""
        return self.chain[-1]

    def proof_of_work(self, last_proof: int) -> int:
        """
        Simple Proof of Work Algorithm:
         - Find a number p' such that hash(pp') contains leading 4 zeroes,
            where p is the previous p'
         - p is the previous proof, and p' is the new proof
        """
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
        return proof

    @staticmethod
    def valid_proof(last_proof: int, proof: int) -> bool:
        """
        Validates the Proof: Does hash(last_proof, proof)
            contain 4 leading zeroes?
        """
        guess = f"{last_proof}{proof}".encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"


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


def showcase():
    blockchain = Blockchain()
    sender_node_identifier = str(uuid4()).replace("-", "")
    receipient_node_identifier = str(uuid4()).replace("-", "")
    _ = mine(blockchain, receipient_node_identifier, True)
    _ = new_transaction(
        blockchain, sender_node_identifier, receipient_node_identifier, 1, True
    )
    _ = chain(blockchain, True)


if __name__ == "__main__":
    showcase()
