import logging

# Now lets configure the configuration of the logger using `logging.basicConfig()`
# We've set the logging level, log path and log format


log_format = "%(levelname)s: %(name)s: %(message)s"
logging.basicConfig(
    level=logging.DEBUG, filename="Logs/my_log_2.log", format=log_format, filemode="w"
)

# Revisiting the previous logging exercise.
# If we open up the my_log_2.log file, you can see the debug message is now printed
# And also, we don't print to the terminal now

logging.debug("I'm a debug message")
logging.info("I'm a info message")
logging.warning("I'm a warning message")
logging.error("I'm a error message")
logging.critical("I'm a critical message")

# The root logger can only be configured once, so the bottom configuration is ignored

logging.basicConfig(
    level=logging.CRITICAL, filename="Logs/my_log_2.log", format=log_format
)

logging.critical("--------------------")
logging.debug("I'm a debug message")
logging.info("I'm a info message")
logging.warning("I'm a warning message")
logging.error("I'm a error message")
logging.critical("I'm a critical message")

