from datetime import datetime
import logging
import os
from datetime import datetime

LOG_DIR= "banking_logs"

CURRENT_TIME_STEMP= f"{datetime.now().strftime('%Y-%m-%d %H-%M-%S')}"

log_file_name= f"log{CURRENT_TIME_STEMP}.log"

os.makedirs(LOG_DIR, exist_ok=True)

log_file_path= os.path.join(LOG_DIR,log_file_name)

logging.basicConfig(filename=log_file_path,
filemode="w",
format='[%(asctime)s]^;%(levelname)s^;%(lineno)d^;%(filename)s^;%(funcName)s()^;%(message)s',
level=logging.INFO
)