from cryptography.fernet import Fernet

# Generar clave segura
def generar_clave():
    clave = Fernet.generate_key()
    with open("clave.key", "wb") as archivo_clave:
        archivo_clave.write(clave)
    return clave

# Cargar clave desde archivo
def cargar_clave():
    with open("clave.key", "rb") as archivo_clave:
        return archivo_clave.read()

# Encriptar mensaje
def encriptar_mensaje(mensaje, clave):
    f = Fernet(clave)
    mensaje_cifrado = f.encrypt(mensaje.encode())
    return mensaje_cifrado

# Desencriptar mensaje
def desencriptar_mensaje(mensaje_cifrado, clave):
    f = Fernet(clave)
    mensaje_descifrado = f.decrypt(mensaje_cifrado).decode()
    return mensaje_descifrado
