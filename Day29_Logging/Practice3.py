import logging
logging.basicConfig(filename='application.log',level=logging.INFO)
logging.info("Application Started")
logging.warning("Memory Usage High")
logging.error("Database Connection Failed")
print("Logs written successfully.")