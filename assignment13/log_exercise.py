import logging

logging.basicConfig(
    filename='assignment13.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def example_function():
    logging.info("Function started")
    try:
        result = 10 / 2
        logging.debug(f"Calculation result: {result}")
    except ZeroDivisionError as e:
        logging.error("Tried to divide by zero")
    logging.info("Function finished")

logging.debug("This is a debug message.")
logging.info("This is an info message.")
logging.warning("This is a warning message.")
logging.error("This is an error message.")
logging.critical("This is a critical message.")

example_function()
