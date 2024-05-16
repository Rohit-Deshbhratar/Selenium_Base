import logging


class Log:
    def log_config(self):
        # create logger
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)

        # create file handler and set level
        fh = logging.FileHandler("selenium_base.log")

        # set format
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s : %(message)s',
                                      datefmt='%m/%d/%Y %I:%M:%S %p')

        # add formatter to file handler
        fh.setFormatter(formatter)

        # add file handler to logger
        logger.addHandler(fh)

        logger.debug("This is DEBUG")
        logger.info("This is INFO")
        logger.warning("This is WARNING")
        logger.error("This is ERROR")
        logger.critical("This is CRITICAL")


lc = Log()
lc.log_config()
