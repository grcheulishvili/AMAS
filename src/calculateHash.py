import hashlib

def md5(self):
    hash = hashlib.md5()
    with open(hashlib.__file__, "rb") as file:
        for f in file:
            hash.update(f)
    return hash.hexdigest()