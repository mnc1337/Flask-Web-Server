import hashlib

def set_hash(data: str):
    encoded = data.encode("utf-8")
    key = hashlib.sha256(encoded).hexdigest()

    return key