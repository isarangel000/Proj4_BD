from cryptography.fernet import Fernet

# 🚨 Gere a chave uma vez e cole aqui
# chave = Fernet.generate_key()
# print(chave)

chave = b'2O1j6m8lFh1r2q9P3tLZQx7nT1mFv5yVx7J8X2nM3R4='  # substitua pela sua chave gerada
fernet = Fernet(chave)

def criptografar(texto):
    return fernet.encrypt(texto.encode())

def descriptografar(texto_criptografado):
    return fernet.decrypt(texto_criptografado).decode()
