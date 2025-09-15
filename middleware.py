import asyncio
from asyncio import Queue
from encryption import encrypt_message, decrypt_message
from log_utils import setup_logger
from config import MAX_RETRIES, TIMEOUT_SECONDS

logger = setup_logger("middleware")

class Middleware:
    def __init__(self):
        self.queues = {}  # nome_coda -> Queue

    def _get_queue(self, queue_name: str) -> Queue:
        if queue_name not in self.queues:
            self.queues[queue_name] = Queue()
        return self.queues[queue_name]

    async def receive_message(self, queue_name: str, message: str):
        encrypted = encrypt_message(message)
        queue = self._get_queue(queue_name)
        await queue.put(encrypted)
        logger.info(f"Messaggio ricevuto su coda '{queue_name}': {message}")

    async def dispatch_message(self, queue_name: str):
        queue = self._get_queue(queue_name)

        if queue.empty():
            return None

        try:
            encrypted = await asyncio.wait_for(queue.get(), timeout=TIMEOUT_SECONDS)
            message = decrypt_message(encrypted)
            logger.info(f"Messaggio distribuito da '{queue_name}': {message}")
            return message

        except asyncio.TimeoutError:
            logger.warning(f"Timeout su coda '{queue_name}' (nessun messaggio consumato entro {TIMEOUT_SECONDS}s)")
            return None

        except Exception as exc:
            # qui arrivano gli errori di decrittazione o altro nel processing
            logger.error(f"Errore durante l'elaborazione del messaggio su '{queue_name}': {exc}")
            return None


