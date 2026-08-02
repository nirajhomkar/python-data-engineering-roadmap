import csv, json, logging, shutil

logging.basicConfig(filename="logs/etl.log",level=logging.INFO,
format="%(asctime)s - %(levelname)s - %(message)s")

logging.info("ETL Started")

try:
     #Taking Backup of sales.csv
    shutil.copy2("input/sales.csv","backup/sales.csv")
    logging.info("Backup Created")

    #Archiving Backup folder
    shutil.make_archive("backup","zip","backup")
    logging.info("Backup Archived")

    with open("input/config.json","r") as file:
        logging.info("Reading config.json")
        config = json.load(file)
        print(f"Company : {config['company']}")
        print(f"Currency: {config['currency']}")
        print(f"Tax     : {config['tax_percentage']}%")

    with open("input/sales.csv","r") as file1:
        logging.info("Reading sales.csv")
        reader = csv.DictReader(file1)

        processed_data = []

        for row in reader:
            row["Revenue"] = int(row["Quantity"]) * int(row["Price"])
            processed_data.append(row)

        print(processed_data)
        logging.info("Transformation Completed")

    with open("output/processed_sales.csv","w",newline="") as file2:
        fieldnames = ["Product","Quantity","Price","Revenue"]
        writer = csv.DictWriter(file2,fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(processed_data)
        logging.info("Load Completed")

    with open("output/summary.json","w",newline="") as file3:
        summary = {
            "company": config["company"],
            "currency": config["currency"],
            "total_products": len(processed_data),
            "total_revenue": sum(row["Revenue"] for row in processed_data),
        }
        json.dump(summary, file3)
        logging.info("Summary Created")

        #Archiving Original sales.csv
        shutil.move("input/sales.csv","archive/sales.csv")
        logging.info("Original File Archived")

except Exception :
    logging.exception("ETL Failed")

finally:
    logging.info("ETL Pipeline Completed Successfully")