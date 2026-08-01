import logging
logging.basicConfig(filename = 'server.log',level=logging.INFO, format='%(asctime)s - %(levelname)s -%(message)s')
logging.info("Server Started")
logging.warning("CPU Usage High")
logging.error("Server Connection Failed")
print("Formatted logs created successfully.")