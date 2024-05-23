# Import Dependencies
import os
import sys
import logging

# Logging format
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s])"

# Create directory for logs if doesn't exist
log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

# Logger Object
logger = logging.getLogger('TumorClassifierLogger')