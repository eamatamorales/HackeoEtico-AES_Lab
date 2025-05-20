
import base64
import os
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet

# Derivar clave desde contraseña
def derivar_clave(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

# Solicitar contraseña
password = input("Ingrese una contraseña: ")
salt = os.urandom(16)
clave = derivar_clave(password, salt)

# Encriptar
mensaje = input("Mensaje a cifrar: ")
f = Fernet(clave)
mensaje_cifrado = f.encrypt(mensaje.encode())
print("Mensaje cifrado:", mensaje_cifrado)

# Desencriptar
f2 = Fernet(clave)
mensaje_descifrado = f2.decrypt(mensaje_cifrado)
print("Mensaje descifrado:", mensaje_descifrado.decode())
