import logging
import time
from contextlib import AbstractContextManager
from logging import Handler, LogRecord
from typing import Any, List, Optional

from pyspark.sql import SparkSession


logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


class Log4JProxyHandler(Handler):
    """Handler to forward messages to log4j."""

    Logger: Any

    def __init__(self, spark_session: SparkSession):
        """Initialise handler with a log4j logger."""
        Handler.__init__(self)
        self.Logger = spark_session._jvm.org.apache.log4j.Logger

    def emit(self, record: LogRecord):
        """Emit a log message."""
        logger = self.Logger.getLogger(record.name)
        if record.levelno >= logging.CRITICAL:
            # Fatal and critical seem about the same.
            logger.fatal(record.getMessage())
        elif record.levelno >= logging.ERROR:
            logger.error(record.getMessage())
        elif record.levelno >= logging.WARNING:
            logger.warn(record.getMessage())
        elif record.levelno >= logging.INFO:
            logger.info(record.getMessage())
        elif record.levelno >= logging.DEBUG:
            logger.debug(record.getMessage())
        else:
            pass

    def close(self):
        """Close the logger."""

class LoggingDelegatedToSpark(AbstractContextManager):

    handler: Handler
    root_handlers: List[Handler]

    def __init__(self, spark_session: SparkSession):
        """Initialise logging context handler."""
        self.handler = Log4JProxyHandler(spark_session)

    def __enter__(self):
        """Divert logging to log4j."""
        self.root_handlers = logging.root.handlers[:]
        for h in self.root_handlers:
            logging.root.removeHandler(h)
        logging.root.addHandler(self.handler)
        logging.getLogger("Log4JProxyHandler").debug("Installed log4j log handler.")

    def __exit__(self, exc_type, exc_value, traceback):
        """Un-divert logging to log4j."""
        # TODO: Log the exception
        logging.root.removeHandler(self.handler)
        for h in self.root_handlers:
            logging.root.addHandler(h)
        logging.getLogger("Log4JProxyHandler").debug("Removed log4j log handler.")


def main():
    log.warning("Starting program. This message uses default Python logging handling")

    spark = SparkSession.builder.appName("Logging Example").getOrCreate()
    with LoggingDelegatedToSpark(spark):
        # All logging in the scope of the context handler is forwarded to the Spark's log4j.
        for l in [log, logging, logging.getLogger('p4j'), logging.getLogger('pyspark')]:
            l.warning("After initialisation")
            l.critical("This is a highly critical message. Prepare your self-esteem!")
            l.error("This is an error")
            l.warning("This is an warning")
            l.info("Information")
            l.debug("de bugs are all over de place")

    # Messages outside the scope of the context handler use the previous logging configuration.
    # Forwarding to log4j still works, but the context handler has removed the diversion.
    spark.stop()
    log.warning("After shutdown")
    time.sleep(2)
    logging.info("More information")


if __name__ == '__main__':
    main()
