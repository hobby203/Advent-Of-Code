import hashlib

k = 'bgvyzdsv'
i = 0
f = False
while not found:
    i += 1
    h_k = hashlib.md5()
    hashable_key.update(key+str(index))
    hashed_key = hashable_key.hexdigest()
    if hashed_key[0:5] == 5*'0':
        found = True
print index
