from aes_utils import generar_clave, cargar_clave, encriptar_mensaje, desencriptar_mensaje

print("Laboratorio AES - Encriptación de Información Sensible")

# 1. Generar o cargar clave
try:
    clave = cargar_clave()
    print("Clave cargada exitosamente.")
except FileNotFoundError:
    clave = generar_clave()
    print("Clave generada y guardada.")

# 2. Mensaje simulado (ej. contraseña o API key)
mensaje = input("\nIngrese el dato a proteger (ej. contraseña, token, etc.): ")

# 3. Encriptar mensaje
cifrado = encriptar_mensaje(mensaje, clave)
print(f"\nMensaje cifrado: {cifrado}")

# 4. Desencriptar para verificar
descifrado = desencriptar_mensaje(cifrado, clave)
print(f"Mensaje descifrado: {descifrado}")
