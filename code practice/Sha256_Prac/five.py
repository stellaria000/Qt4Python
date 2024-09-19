import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64

# 입력값
password = "aton5133A!"
user_id = "administrator"

# SHA256 키 생성: 아이디를 뒤집은 문자열 + 원래 아이디
reversed_id = user_id[::-1]
key_data = reversed_id + user_id

# SHA256 해시 생성
hash_key = hashlib.sha256(key_data.encode()).digest()

# AES 암호화 설정
# 고정된 IV 값 (AES는 IV가 16 바이트여야 합니다)
iv = b'HJHJHHWSSWHNMJJW'

# AES 암호화 객체 생성 (모드: CBC)
cipher = AES.new(hash_key, AES.MODE_CBC, iv)

# 비밀번호를 AES로 암호화 (패딩을 적용해야 함)
ciphertext = cipher.encrypt(pad(password.encode(), AES.block_size))

# 암호문을 Base64로 인코딩하여 출력
encrypted_password = base64.b64encode(ciphertext).decode('utf-8')

print("암호화된 비밀번호:", encrypted_password)
