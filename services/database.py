from tinydb import TinyDB
from datetime import datetime

from models.snapshot import Snapshot


class DatabaseService:
    PATH = "db.json"

    def __init__(self) -> None:
        self.db = TinyDB(self.PATH)
        self.snapshots = self.db.table("snapshots")

    def register_snapshot(self, snapshot: Snapshot) -> None:
        self.snapshots.insert(snapshot.model_dump())

    def yield_snapshots(self):
        docs = self.snapshots.all()
        for doc in docs:
            yield Snapshot.model_validate(doc)
