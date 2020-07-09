# To start logging with Python, import the logging module
import logging

# We can log to console using `logging.my_level`
# Notice how `logging.debug` isn't printed, and `logging.warning` is printed
# This is due to the default logging level of the root logger
logging.debug("I'm a debug message")
logging.info("I'm a info message")
logging.warning("I'm a warning message")
logging.error("I'm a error message")
logging.critical("I'm a critical message")
print("")

# We can also check the default logging level of the root logger
# The default level is 30 (or WARNING), so any message levels below 30 are not printed
print(f"The default logging level is: {logging.root.level}")
print("")

# We can check the logging levels using `logging.MYLEVEL`
# So that means DEBUG and INFO logs won't be printed
print(f"DEBUG level: {logging.DEBUG}")
print(f"INFO level: {logging.INFO}")
print(f"WARNING level: {logging.WARNING}")
print(f"ERROR level: {logging.ERROR}")
print(f"CRITICAL level: {logging.CRITICAL}")

