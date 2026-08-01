import logging
logging.basicConfig(filename = 'error.log',level=logging.ERROR, format='%(asctime)s - %(levelname)s -%(message)s')
try:
    number = int(input("Enter a number: "))
    print(f"You entered: {100/number}")
except ZeroDivisionError:
    logging.exception("Division Error")
print("Program Finished")