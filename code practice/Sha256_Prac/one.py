import hashlib

input_string= "Hello World!"

encoded_string= input_string.encode()

sha256_hash= hashlib.sha256()
print("SHA256 hash=", sha256_hash)

# DATA TO HASH
sha256_hash.update(encoded_string)

# CHANGE THE HASH INTO 16 BINARY
hash_result= sha256_hash.hexdigest()
print("hash_result= ", hash_result)

