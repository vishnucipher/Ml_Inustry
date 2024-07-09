'''
logger.py is a file in your project that sets up and manages logging. 
Logging is a way to keep track of what your program 
is doing by writing messages to a console, file, or another place. 
These messages can help you understand the program's flow and diagnose problems.


This module defines functions and classes which implement a 
flexible event logging system for applications and libraries'''


import logging
import os
from datetime import datetime

LOG_FILE =f"{datetime.now().strftime('%m_%d_%Y_%H_%S')}.log"
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)
LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format ="[%(asctime)s %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
