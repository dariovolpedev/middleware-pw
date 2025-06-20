from cryptography.fernet import Fernet, InvalidToken
from config import FERNET_KEY

fernet = Fernet(FERNET_KEY)

def encrypt_message(message: str) -> bytes:
    """Cifra un messaggio stringa restituendo un token bytes."""
    return fernet.encrypt(message.encode())

def decrypt_message(token: bytes) -> str:
    """Decifra un token cifrato in bytes e restituisce la stringa originale."""
    try:
        return fernet.decrypt(token).decode()
    except InvalidToken:
        return "[ERRORE: token non valido]"
