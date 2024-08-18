from tinydb import TinyDB
from models.snapshot import Snapshot


PATH = "db.json"
db = TinyDB(PATH)
snapshots = db.table("snapshots")


def register_snapshot(snapshot: Snapshot) -> None:
    snapshots.insert(snapshot.model_dump())


def yield_snapshots():
    docs = snapshots.all()
    for doc in docs:
        yield Snapshot.model_validate(doc)
