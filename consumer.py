import asyncio
from middleware import Middleware
from config import QUEUE_NAMES

async def consume(middleware: Middleware):
    while True:
        for qname in QUEUE_NAMES:
            message = await middleware.dispatch_message(qname)
            if message:
                print(f"[CONSUMER - {qname.upper()}] Messaggio ricevuto: {message}")
        await asyncio.sleep(0.5)
