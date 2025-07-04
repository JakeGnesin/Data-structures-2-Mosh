import hashlib
import time
import json
from enum import Enum
from typing import List, Dict
import uuid


class TransactionStatus(Enum):
    INITIATED = "INITIATED"
    PENDING = "PENDING"
    VERIFIED = "VERIFIED"
    COMPLETE = "COMPLETE"


class Transaction:
    def __init__(self, sender: str, receiver: str, amount: float):
        self.id = str(uuid.uuid4())
        self.sender, self.receiver, self.amount = sender, receiver, amount
        self.timestamp = time.time()
        self.status = TransactionStatus.INITIATED
        self.status_history = [(self.status, self.timestamp)]

    def update_status(self, status: TransactionStatus):
        self.status = status
        self.status_history.append((status, time.time()))

    def to_dict(self) -> Dict:
        return {
            "id": self.id, "sender": self.sender, "receiver": self.receiver,
            "amount": self.amount, "timestamp": self.timestamp,
            "status": self.status.value,
            "status_history": [(s.value, t) for s, t in self.status_history]
        }


class Block:
    def __init__(self, index: int, transactions: List[Transaction], prev_hash: str):
        self.index, self.transactions, self.prev_hash = index, transactions, prev_hash
        self.timestamp, self.nonce = time.time(), 0
        self.hash = self._calc_hash()

    def _calc_hash(self) -> str:
        block = json.dumps({
            "index": self.index, "transactions": [t.to_dict() for t in self.transactions],
            "timestamp": self.timestamp, "prev_hash": self.prev_hash, "nonce": self.nonce
        }, sort_keys=True)
        return hashlib.sha256(block.encode()).hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = [Block(0, [], "0")]
        self.difficulty = 4
        self.pending = []
        self.sorted_txs = []

    def add_transaction(self, sender: str, receiver: str, amount: float) -> Transaction:
        tx = Transaction(sender, receiver, amount)
        self.pending.append(tx)
        self.sorted_txs.append(tx)
        self.sorted_txs.sort(key=lambda x: x.amount, reverse=True)
        return tx

    def mine(self, miner: str):
        block = Block(len(self.chain), self.pending, self.chain[-1].hash)
        while block.hash[:self.difficulty] != "0" * self.difficulty:
            block.nonce += 1
            block.hash = block._calc_hash()
        for tx in block.transactions:
            for status in [TransactionStatus.PENDING, TransactionStatus.VERIFIED, TransactionStatus.COMPLETE]:
                tx.update_status(status)
        self.chain.append(block)
        self.pending = [Transaction("network", miner, 10.0)]

    def get_sorted_transactions(self) -> List[Dict]:
        return [tx.to_dict() for tx in self.sorted_txs]

    def get_transaction_status(self, tx_id: str) -> Dict:
        for tx in self.sorted_txs:
            if tx.id == tx_id:
                return tx.to_dict()
        return {"error": "Transaction not found"}


if __name__ == "__main__":
    bc = Blockchain()
    t1 = bc.add_transaction("Alice", "Bob", 100.0)
    t2 = bc.add_transaction("Bob", "Charlie", 50.0)
    t3 = bc.add_transaction("Charlie", "Alice", 200.0)
    bc.mine("Miner1")
    print("\nSorted Transactions:")
    for tx in bc.get_sorted_transactions():
        print(
            f"ID: {tx['id'][:8]}..., Amount: {tx['amount']}, Status: {tx['status']}")
    print("\nTransaction Status:", bc.get_transaction_status(t1.id))
    print("\nTransaction Status:", bc.get_transaction_status(t2.id))
    print("\nTransaction Status:", bc.get_transaction_status(t3.id))
