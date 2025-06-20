# main.py

import asyncio
from middleware import Middleware
from producer import produce
from consumer import consume
from logger import setup_logger

logger = setup_logger("main")

async def main():
    middleware = Middleware()
    try:
        await asyncio.gather(
            produce(middleware),
            consume(middleware)
        )
    except Exception as e:
        logger.error(f"Errore durante l'esecuzione: {e}")

if __name__ == "__main__":
    asyncio.run(main())
