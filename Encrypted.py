from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.padding import PKCS7
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import os

def encrypt_file(file_path, key):
    if len(key) != 16:
        raise ValueError("The key must be exactly 16 characters long.")

    # Convertir la clé en bytes
    key = key.encode('utf-8')

    # Générer un IV (vecteur d'initialisation) aléatoire
    iv = os.urandom(16)

    # Configurer le chiffrement
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Lire et ajouter un padding au contenu du fichier
    with open(file_path, 'rb') as f:
        data = f.read()

    padder = PKCS7(128).padder()
    padded_data = padder.update(data) + padder.finalize()

    # Chiffrer les données
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

    # Écrire le fichier chiffré (IV + données chiffrées)
    encrypted_file_path = file_path + '.enc'
    with open(encrypted_file_path, 'wb') as f:
        f.write(iv + encrypted_data)

    print(f"Encrypted file saved as {encrypted_file_path}")

# Exemple d'utilisation
print("Encrypted file AES 16-bit ")
print()
encrypt_file(input('Path file :'), str(input("Key (16 characters) : ")))
