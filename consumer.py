import asyncio
from middleware import Middleware
from config import QUEUE_NAMES
from logger import setup_logger

async def consume(middleware: Middleware):
    while True:
        for qname in QUEUE_NAMES:
            message = await middleware.dispatch_message(qname)
            if message:
                logger.info(f"[{qname.upper()}] Messaggio ricevuto: {message}")
        await asyncio.sleep(0.5)
