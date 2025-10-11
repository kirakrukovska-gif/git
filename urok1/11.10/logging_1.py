import logging

logging.basicConfig(
    filename = "app.log",
    filemode="a",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logging.debug("Init helper")
logging.critical("System fail")
logging.error("Load error")


