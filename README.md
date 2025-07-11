﻿# Middleware Asincrono in Python

Questo progetto implementa un sistema di middleware asincrono per la comunicazione tra componenti software autonomi, ispirato al pattern Message-Oriented Middleware (MOM). È progettato per simulare la comunicazione tra sottosistemi aziendali (produzione, magazzino, logistica) in modo non bloccante, sicuro e scalabile.

ARCHITETTURA

L'architettura è composta da tre moduli principali:
- Producer: genera messaggi simulati (es. eventi aziendali).
- Middleware: riceve, cifra e accoda i messaggi in modalità FIFO asincrona.
- Consumer: recupera i messaggi, li decifra e li elabora.

FUNZIONALITÀ PRINCIPALI

- Comunicazione asincrona tramite asyncio.
- Coda FIFO con asyncio.Queue.
- Cifratura simmetrica dei messaggi con cryptography (Fernet).
- Logging personalizzato per ciascun modulo.
- Modularità e separazione delle responsabilità.

COME ESEGUIRE IL PROGETTO

1. Creare un ambiente virtuale (opzionale)

   python -m venv venv
   source venv/bin/activate  (Linux/Mac)
   venv\Scripts\activate     (Windows)

2. Installare le dipendenze

   pip install -r requirements.txt

3. Avviare il sistema

   python main.py

   Verranno eseguiti in parallelo il producer e il consumer, con log salvati nei file:
   - producer.log
   - middleware.log
   - consumer.log

STRUTTURA DEI FILE

- main.py          → Avvio del sistema
- producer.py      → Simula l'invio di eventi
- consumer.py      → Simula la ricezione e gestione
- middleware.py    → Logica asincrona e coda FIFO
- encryption.py    → Cifratura e decifratura dei messaggi
- config.py        → Parametri globali
- logger.py        → Logging personalizzato
- requirements.txt → Dipendenze


SICUREZZA

- I messaggi sono cifrati con chiave simmetrica (Fernet).
- La chiave è contenuta in config.py (in produzione si consiglia l’uso di variabili d’ambiente).

AUTORE

Project Work a cura di [Dario Volpe], Corso di Laurea Triennale in Informatica per le aziende digitali.
