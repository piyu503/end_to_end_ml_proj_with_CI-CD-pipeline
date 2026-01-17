import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# 1. Create logs directory ONLY
logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)

# 2. Create full log file path
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# 3. Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# if __name__ == "__main__":
#     logging.info("Logging has started!!")