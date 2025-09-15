# config.py
import logging

# livello di log
LOG_LEVEL = logging.INFO 

# cartella o percorso dove mettere i file di log
LOG_DIR = "log"

# Chiave per la cifratura Fernet (puoi rigenerarla se vuoi)
FERNET_KEY = b'V-nfQ9bB_gCyazQCM3zRMMGnHT6cA4jWsp2j7zmKWS8='

# Nome della coda dei messaggi
QUEUE_NAME = "event_queue"

# Parametri base
MAX_RETRIES = 3

# Timeout in secondi per dispatch_message
TIMEOUT_SECONDS = 5  

# Denominazioni diverse code per diversi reparti
QUEUE_NAMES = ["produzione", "magazzino", "logistica"]