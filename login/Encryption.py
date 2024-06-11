from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from base64 import urlsafe_b64encode, urlsafe_b64decode
import os
import json
from datetime import datetime, timedelta
import jwt

def derive_key(password: str, salt: bytes) -> bytes:
    kdf = Scrypt(
        salt=salt,
        length=32,
        n=2**14,
        r=8,
        p=1,
        backend=default_backend()
    )
    key = kdf.derive(password.encode())
    return key

def encrypt_message(message: str, password: str) -> (bytes, bytes, bytes):
    salt = os.urandom(16)
    key = derive_key(password, salt)
    iv = os.urandom(16)

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(message.encode()) + padder.finalize()

    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    return salt, iv, ciphertext

def decrypt_message(salt: bytes, iv: bytes, ciphertext: bytes, password: str) -> str:
    key = derive_key(password, salt)

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    padded_data = decryptor.update(ciphertext) + decryptor.finalize()

    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    data = unpadder.update(padded_data) + unpadder.finalize()

    return data.decode()


def decrypt_response(response, password):
    token = response.json().get('token')
    try:
        decoded = jwt.decode(token, get_secret_key(), algorithms=['HS256'])
        encrypted_data = decoded['data']
        
        salt = urlsafe_b64decode(encrypted_data['salt'])
        iv = urlsafe_b64decode(encrypted_data['iv'])
        ciphertext = urlsafe_b64decode(encrypted_data['ciphertext'])
        
        decrypted_message = decrypt_message(salt, iv, ciphertext, password)
        return json.loads(decrypted_message)
    
    except jwt.ExpiredSignatureError:
        print("The token has expired.")
    except jwt.InvalidTokenError:
        print("Invalid token.")
    except Exception as e:
        print(f"An error occurred: {e}")

def get_secret_key():
    return 'mi_super_secreta_contraseña'


def get_encrypted_data(salt, iv, ciphertext):
    return {
        'salt': urlsafe_b64encode(salt).decode(),
        'iv': urlsafe_b64encode(iv).decode(),
        'ciphertext': urlsafe_b64encode(ciphertext).decode()
    }

def get_jwt_token(data):
    return jwt.encode({
                'data': data,
                'exp': datetime.utcnow() + timedelta(minutes=30)
            }, get_secret_key(), algorithm='HS256')

def encrypt_fullmessage(data):

    token = get_jwt_token(data)

    return {'token':token}


def decrypt_responseAPI(response, password):
    token = response['token']
    try:
        
        decoded = jwt.decode(token, get_secret_key(), algorithms=['HS256'])
        encrypted_data = decoded['data']
        print("ENCRYPTED DATA:",encrypted_data)
        
       
        return encrypted_data
    
    except jwt.ExpiredSignatureError:
        print("The token has expired.")
    except jwt.InvalidTokenError:
        print("Invalid token.")
    except Exception as e:
        print(f"An error occurred: {e}")