import logging

# We create a logger, which is a child of the root logger
# We set the logging level to DEBUG as a default
logger = logging.getLogger("logger of log_3.py")
logger.setLevel(logging.DEBUG)

# A handler redirects outputs from the loggers to a file or terminal
# A logger can have multiple handlers attached
# FileHandler is used to control output to files
# StreamHandler is used to control output to terminal (sys.stdout,syst.stderr)
# Each handler can be customised to suit programmer's needs

# Lets create a file handler for info messages
handler1 = logging.FileHandler("Logs/my_log_3_info.log", mode="w")
handler1.setLevel(logging.INFO)
logger.addHandler(handler1)

# Lets create a file handler for critical messages and add formatting
handler2 = logging.FileHandler("Logs/my_log_3_crit.log", mode="w")
handler2.setLevel(logging.CRITICAL)
handler2.setFormatter(logging.Formatter("%(levelname)s: %(name)s: %(message)s"))
logger.addHandler(handler2)

# Let's create a stream handler
# We can see it outputting into our terminal
import sys

handler3 = logging.StreamHandler(sys.stdout)
handler3.setLevel(logging.WARNING)
logger.addHandler(handler3)

# Note logging has been replaced with logger
logger.debug("I'm a debug message")
logger.info("I'm a info message")
logger.warning("I'm a warning message")
logger.error("I'm a error message")
logger.critical("I'm a critical message")
