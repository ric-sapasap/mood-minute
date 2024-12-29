from tinydb import TinyDB, Query

db = TinyDB("test-db.json")
result = db.get(
    doc_id=1
)
print(result)
