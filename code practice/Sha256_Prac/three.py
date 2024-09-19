from Crypto.Cipher import AES
import hashlib
import base64
from Crypto.Util.Padding import unpad

def decrypt_password(encrypted_str_base64, key_str, iv):
    try:
        # Base64로 인코딩된 암호문을 디코딩
        encrypted_str = base64.b64decode(encrypted_str_base64)
        
        # SHA-256으로 키 생성
        # key_str을 바이트로 변환 후 해시 생성
        sha256 = hashlib.sha256()
        sha256.update(key_str.encode('utf-8'))
        cipher_key = sha256.digest()

        # AES 암호화 객체 생성
        cipher = AES.new(cipher_key, AES.MODE_CBC, iv)
        
        # 패딩 없이 먼저 복호화 시도
        decrypted_data = cipher.decrypt(encrypted_str)

        try:
            # 패딩을 제거해 복호화
            decrypted_data = unpad(decrypted_data, AES.block_size)
        except ValueError:
            # 패딩 제거 실패 시, 패딩 없는 데이터 반환
            print("패딩 해제 실패: 원시 데이터 반환 중")

        # UTF-8로 디코딩 시도
        return decrypted_data.decode('utf-8', errors='ignore')

    except Exception as e:
        # 복호화 중 문제가 발생하면 오류 메시지 반환
        return f"복호화 실패: {e}"

def main():
    # Base64로 인코딩된 암호문
    encrypted_str_base64 = "34D61070644C5535E0D5D05C947A0B4C0A65748898D1AD6096617FF4DEED4E2B"
    
    # 원래 문자열로 생성된 키
    key_str = "administrator"
    key2Use= key_str[::-1]+ key_str
    
    # 암호화에 사용된 IV (16바이트)
    iv = b'HJHJHHWSSWHNMJJW'

    # 비밀번호 복호화
    decrypted_str = decrypt_password(encrypted_str_base64, key_str, iv)

    # 복호화된 문자열 출력
    print(f"복호화된 문자열: {decrypted_str}")

# 메인 함수 실행
if __name__ == "__main__":
    main()
