import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename="logs.log",
    filemode='a',
    format="We have next logging message: %(asctime)s:%(levelname)s - %(message)s")

# logging.debug("debug2")
# logging.info("info2")
# logging.warning("warning2")
# logging.error("error2")
# logging.critical("critical2")

try:
    print(10/0)
except Exception:
    logging.exception("Exception")