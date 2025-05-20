
from cryptography.fernet import Fernet

# Cargar clave desde archivo
def cargar_clave():
    with open("clave.key", "rb") as archivo_clave:
        return archivo_clave.read()

# Encriptar contenido de archivo
def cifrar_archivo(nombre_archivo, clave):
    f = Fernet(clave)
    with open(nombre_archivo, "rb") as file:
        datos = file.read()
    datos_cifrados = f.encrypt(datos)
    with open("datos.enc", "wb") as file_enc:
        file_enc.write(datos_cifrados)

# Desencriptar archivo
def descifrar_archivo(nombre_archivo, clave):
    f = Fernet(clave)
    with open(nombre_archivo, "rb") as file_enc:
        datos_cifrados = file_enc.read()
    datos = f.decrypt(datos_cifrados)
    print("Contenido original del archivo:")
    print(datos.decode())

# Uso
clave = cargar_clave()
cifrar_archivo("venv.txt", clave)
descifrar_archivo("datos.enc", clave)
