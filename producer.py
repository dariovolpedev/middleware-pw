import asyncio
from middleware import Middleware
from log_utils import setup_logger

logger = setup_logger("producer")

async def produce(middleware: Middleware):
    eventi = [
        {"queue": "produzione", "message": "Produzione completata: lotto A"},
        {"queue": "magazzino", "message": "Movimentazione in magazzino"},
        {"queue": "logistica", "message": "Richiesta spedizione logistica"}
    ]

    for evento in eventi:
        await middleware.receive_message(evento["queue"], evento["message"])
        logger.info(f"Messaggio inviato a '{evento['queue']}': {evento['message']}")
        await asyncio.sleep(1)

