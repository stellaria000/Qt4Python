import hashlib
import base64

def generate_salted_hash(password, salt_bytes):
    # HASH FIRST: SHA256(PASSWORD)
    sha256_f = hashlib.sha256()
    sha256_f.update(password.encode('utf-8'))
    hash_f = sha256_f.hexdigest()

    # CONVERT SALT BYTES TO BASE64
    salt = base64.b64encode(salt_bytes).decode('utf-8')

    # HASH SECOND: SHA256(HASH FIRST+SALT)
    sha256 = hashlib.sha256()
    combined = (hash_f + salt).encode('utf-8')
    sha256.update(combined)
    hash_result = sha256.digest()

    # CONVERT RESULT TO BASE64
    return base64.b64encode(hash_result).decode('utf-8')

def main():
    # PASSWORD AND ID(USED FOR MAKING SALT) TO ENCRYPT
    password = ""
    user_id = ""
    salt_string = user_id[::-1] + user_id  # DI+ ID
    salt_bytes = salt_string.encode('utf-8')

    # PRINT RESULT
    result = generate_salted_hash(password, salt_bytes)
    print(f"Generated salted hash: {result}")

if __name__ == "__main__":
    main()
