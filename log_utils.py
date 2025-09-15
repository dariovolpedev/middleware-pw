import os
import logging
from config import LOG_DIR, LOG_LEVEL

def setup_logger(name: str):
    os.makedirs(LOG_DIR, exist_ok=True)  # garantisce che la cartella esista

    logger = logging.getLogger(name)
    logger.setLevel(LOG_LEVEL)

    if not logger.handlers:
        log_path = os.path.join(LOG_DIR, f"{name}.log")
        fh = logging.FileHandler(log_path)
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    return logger
