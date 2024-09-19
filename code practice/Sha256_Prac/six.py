import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

# 암호화된 데이터를 복호화하는 함수
def decrypt_password(encrypted_password, user_id):
    # SHA256 키 생성: 아이디를 뒤집은 문자열 + 원래 아이디
    reversed_id = user_id[::-1]
    key_data = reversed_id + user_id

    # SHA256 해시 생성
    hash_key = hashlib.sha256(key_data.encode()).digest()

    # AES 암호화 설정 (복호화에도 동일한 IV 사용)
    iv = b'HJHJHHWSSWHNMJJW'
    cipher = AES.new(hash_key, AES.MODE_CBC, iv)


    # Base64로 인코딩된 암호문을 디코딩
    encrypted_data = base64.b64decode(encrypted_password)
    print(f"encrypted data= {encrypted_data}")

    # AES 복호화 수행
    decrypted_data = cipher.decrypt(encrypted_data)
    print(f"decrypted data= {decrypted_data}")

    # 복호화된 데이터에서 패딩 제거
    try:
        decrypted_password = unpad(decrypted_data, AES.block_size).decode('utf-8')
        print(f"decrpted password= {decrypted_password}")
    except ValueError:
        return "패딩 오류: 복호화된 데이터에 잘못된 패딩이 포함되어 있습니다."

    return decrypted_password

# 메인 코드
if __name__ == "__main__":
    # 암호화된 비밀번호 (암호화 예시 코드에서 얻은 값)
    encrypted_password = "HW4tgSFrkVgfC/m61UnZXouEiiqP11Gxl64AXhnDpUY="  

    # 복호화할 아이디
    user_id = "administrator"

    # 복호화
    decrypted_password = decrypt_password(encrypted_password, user_id)

    # 복호화된 비밀번호 출력
    print("복호화된 비밀번호:", decrypted_password)
