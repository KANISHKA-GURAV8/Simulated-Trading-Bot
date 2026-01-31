import logging
import  os

LOG_DIR="logs"
LOG_FILE=os.path.join(LOG_DIR,"trading_bot.log")

def setup_logger():
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

    logger=logging.getLogger("trading_bot")
    logger.setLevel(logging.INFO)

    if logger.handlers:
        return logger
    
    file_handler=logging.FileHandler(LOG_FILE)
    formatter=logging.Formatter('%(asctime)s|%(levelname)s|%(name)s|%(message)s')
    
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
