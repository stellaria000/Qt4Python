import base64
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def decode_pw(encrypted_str, key_str, check_base64=False):
    encrypted_str = encrypted_str.strip()
    
    if check_base64 and len(encrypted_str) % 4 != 0:
        return "Base64 decoding issue"
    
    try:
        # Base64 디코딩
        pass_code = base64.b64decode(encrypted_str)
        
        # AES 키 생성
        key = key_str[::-1] + key_str
        sha256 = hashlib.sha256()
        sha256.update(key.encode('utf-8'))
        cipher_key = sha256.digest()
        
        # AES 암호화 객체 생성
        iv = b"HJHJHHWSSWHNMJJW"
        cipher = AES.new(cipher_key, AES.MODE_CBC, iv)
        
        # 디버깅 출력
        print(f"Encrypted data (Base64): {encrypted_str}")
        print(f"Decoded encrypted data (bytes): {pass_code}")
        print(f"Key used for decryption (hex): {cipher_key.hex()}")
        print(f"IV used for decryption: {iv}")

        # 패딩 처리 및 복호화
        decrypted_data = cipher.decrypt(pass_code)
        try:
            unpad_data = unpad(decrypted_data, AES.block_size)
            return unpad_data.decode('utf-8')
        except ValueError as ve:
            # 패딩 오류 시
            return f"Padding error: {ve}"
    except (base64.binascii.Error, ValueError) as e:
        # Base64 디코딩 오류 또는 ValueError (예: 패딩 오류)
        return f"Decryption failed: {e}"

def main():
    # 비밀번호 복호화
    decrypted_str = decode_pw("HW4tgSFrkVgfC/m61UnZXouEiiqP11Gxl64AXhnDpUY=", "administrator")

    # 복호화된 문자열 출력
    print(f"복호화된 문자열: {decrypted_str}")

# 메인 함수 실행
if __name__ == "__main__":
    main()
