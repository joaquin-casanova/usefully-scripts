import logging

logging.basicConfig(
    filename='./results.log',
    level=logging.INFO,
    filemode='w',
    format='%(name)s - %(levelname)s - %(message)s')

def division_values(x, y):
    logging.info(f"The numerator: {x} and denominador: {y}")
    try:
        result = x / y
        logging.info(f"SUCCESS: The operation was sucessfully")
        logging.info(f"SUCCESS: The operation result was: {result}")
        return result

    except ZeroDivisionError:
        logging.error("ERROR: We are not able to divide by zero")


division_values(1, 0)