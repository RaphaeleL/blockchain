class blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []

    def new_transaction(self):
        """Creates a new Block and adds it to the chain"""
        print("Creating a new Transaction")

    def new_block(self):
        """Creates a new Block and adds it to the chain"""
        print("Creating a new block")

    @staticmethod
    def hash(block):
        """Hashes a Block"""
        pass

    @property
    def last_block(self):
        """Returns the last Block in the chain"""
        pass


if __name__ == "__main__":
    bc = blockchain()
