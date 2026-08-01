import logging

logging.basicConfig(
    filename="etl.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Program Started")

try:
    logging.info("Reading sales.csv")

    with open("sales.csv", "r") as file:
        data = file.read()

    logging.info("Processing Completed")

except Exception:
    logging.exception("ETL Failed")

finally:
    logging.info("Program Finished")