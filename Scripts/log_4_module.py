import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Creating file handlers
handler = logging.FileHandler("Logs/my_log_4_module.log", mode="w")
handler.setLevel(logging.ERROR)
handler.setFormatter(logging.Formatter("%(levelname)s: %(name)s: %(message)s"))
logger.addHandler(handler)

# Logging
logger.debug(
    "I'm being run as a module. My level is set to ERROR. To be outputted into my_log_4_module.log"
)
logger.info(
    "I'm being run as a module. My level is set to ERROR. To be outputted into my_log_4_module.log"
)
logger.warning(
    "I'm being run as a module. My level is set to ERROR. To be outputted into my_log_4_module.log"
)
logger.error(
    "I'm being run as a module. My level is set to ERROR. To be outputted into my_log_4_module.log"
)
logger.critical(
    "I'm being run as a module. My level is set to ERROR. To be outputted into my_log_4_module.log"
)
