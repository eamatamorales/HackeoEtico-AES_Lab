
# 🔐 Laboratorio AES - Hackeo Ético (Universidad Fidélitas)

Este laboratorio en Python demuestra el uso práctico del cifrado simétrico AES utilizando la librería `cryptography`. Es parte del curso **CY-203 Hackeo Ético**, en la unidad dedicada al rastreo, reconocimiento y protección de datos.

---

## 📂 Contenido del Proyecto

- `aes_utils.py`: Funciones para generar claves, cifrar y descifrar mensajes
- `main.py`: Script principal interactivo para probar el cifrado

---

## 💻 Requisitos

Instalar Python 3 y la librería necesaria:

```bash
pip install cryptography
```

---

## ▶️ Cómo usar

Ejecuta el laboratorio desde la terminal:

```bash
python main.py
```

---

## 🧠 ¿Qué aprenderás?

- Generar claves AES de forma segura  
- Cifrar datos sensibles como contraseñas o tokens  
- Desencriptar datos usando la clave correspondiente  
- Aplicar conceptos reales de protección de la información  

---

## 📘 Aplicaciones reales

- Protección de archivos `.env` o claves API  
- Cifrado de contraseñas en sistemas  
- Seguridad en bases de datos  
- Implementación de herramientas en Pentesting defensivo  

---

## 🎓 Tarea para estudiantes

Extiende el laboratorio original para cubrir los siguientes objetivos:

### ✅ Parte 1 - Cifrado de archivos

1. Crea un archivo llamado `datos.txt` con contenido simulado sensible.
2. Agrega una función que:
   - Lea el contenido del archivo
   - Lo cifre con AES
   - Guarde el contenido cifrado en un archivo `datos.enc`
3. Crea otra función que:
   - Lea `datos.enc`
   - Lo descifre con la clave
   - Muestre el contenido original en pantalla

---

### ✅ Parte 2 - Clave derivada por contraseña

1. Solicita una contraseña al usuario  
2. Deriva una clave segura utilizando `PBKDF2HMAC`  
3. Usa esta clave para cifrar y descifrar mensajes  
4. Guarda el mensaje cifrado y demuestra que puede recuperarse con la misma contraseña  

> 💡 Esta funcionalidad es similar a como funcionan los gestores de contraseñas. Es ideal para proteger datos sin tener que guardar la clave en disco.

---

## 📚 Recursos útiles

- [Documentación de `cryptography`](https://cryptography.io/en/latest/)
- [AES explicado fácil (YouTube)](https://www.youtube.com/watch?v=O4xNJsjtN6E)
- [PBKDF2 Key Derivation](https://cryptography.io/en/latest/hazmat/primitives/kdf/pbkdf2/)

---

**Profesor:** Esteban Mata Morales  
**Curso:** CY-203 Hackeo Ético  
**Universidad Fidélitas de Costa Rica**
