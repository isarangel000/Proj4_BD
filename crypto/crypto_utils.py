from cryptography.fernet import Fernet

chave = b'2O1j6m8lFh1r2q9P3tLZQx7nT1mFv5yVx7J8X2nM3R4='  
fernet = Fernet(chave)

def criptografar(texto):
    return fernet.encrypt(texto.encode())

def descriptografar(texto_criptografado):
    return fernet.decrypt(texto_criptografado).decode()
