import logging

logging.basicConfig(
    filename = "trace.log",
    filemode="w",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

try:
    print(f"{10*10}")
except Exception as e:  
    logging.exception("something went wrong")






