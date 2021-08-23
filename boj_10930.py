import hashlib

data = input()

data = data.encode()
result = hashlib.sha256(data).hexdigest()

print(result)