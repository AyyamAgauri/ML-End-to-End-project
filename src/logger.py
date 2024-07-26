#Logs any Exception and Info occured
import logging
import os
from datetime import datetime

#Creates a string representing the name of log file which returns month_day_time_hour_min_sec
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

#Creates a path for log file (current_directory/logs/07_26_2024_14_35_22.log)
logs_path = os.path.join(os.getcwd(), 'logs', LOG_FILE)

#Creates the particular directory specified by logs_path
os.makedirs(logs_path, exist_ok= True)

#Overrides the upper commands
LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)


#Configures the message to log
logging.basicConfig(
    filename= LOG_FILE_PATH,
    format= "[ %(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level= logging.INFO
)

