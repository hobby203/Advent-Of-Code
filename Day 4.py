import hashlib

key = 'bgvyzdsv'
index = 0
found = False
while not found:
    index += 1
    hashable_key = hashlib.md5()
    hashable_key.update(key+str(index))
    hashed_key = hashable_key.hexdigest()
    if hashed_key[0:5] == 5*'0':
        found = True
print index
