import traceback
import logging

logging.basicConfig(filename='sample.log')
try:
    print(4/0)
except Exception as e:
    print("error: " + traceback.format_exc())
    logging.error(traceback.format_exc())
