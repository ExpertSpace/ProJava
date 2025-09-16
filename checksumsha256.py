import hashlib
import json
import os

FILES = [
    "ShortcutDoctorUSB.jar",
    "ShortcutDoctorUSB.exe"
]

def sha256sum(filename, block_size=65536):
    h = hashlib.sha256()
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(block_size), b""):
            h.update(chunk)
    return h.hexdigest()

data = {}

for f in FILES:
    if os.path.exists(f):
        size = os.path.getsize(f)
        hashval = sha256sum(f)
        data[f] = {
            "size": size,
            "sha256": hashval
        }
    else:
        data[f] = {
            "size": None,
            "sha256": None
        }

with open("hashes.json", "w", encoding="utf-8") as out:
    json.dump(data, out, indent=4, ensure_ascii=False)

print("✅ hashes.json обновлён")
