import asyncio
from middleware import Middleware

async def produce(middleware: Middleware):
    eventi = [
        {"queue": "produzione", "message": "Produzione completata: lotto A"},
        {"queue": "magazzino", "message": "Movimentazione in magazzino"},
        {"queue": "logistica", "message": "Richiesta spedizione logistica"}
    ]

    for evento in eventi:
        await middleware.receive_message(evento["queue"], evento["message"])
        print(f"[PRODUCER] Messaggio inviato a '{evento['queue']}': {evento['message']}")
        await asyncio.sleep(1)
