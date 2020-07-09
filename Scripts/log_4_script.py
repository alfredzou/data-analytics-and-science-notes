import logging

# When a module is imported, it is run
# So its important not to use the root logger to prevent conflicts
import log_4_module

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Creating file handlers
handler = logging.FileHandler("Logs/my_log_4_script.log", mode="w")
handler.setLevel(logging.WARNING)
handler.setFormatter(logging.Formatter("%(levelname)s: %(name)s: %(message)s"))
logger.addHandler(handler)

# Logging
logger.debug(
    "I'm being run as a script. My level is set to WARNING. To be outputted into my_log_4_script.log"
)
logger.info(
    "I'm being run as a script. My level is set to WARNING. To be outputted into my_log_4_script.log"
)
logger.warning(
    "I'm being run as a script. My level is set to WARNING. To be outputted into my_log_4_script.log"
)
logger.error(
    "I'm being run as a script. My level is set to WARNING. To be outputted into my_log_4_script.log"
)
logger.critical(
    "I'm being run as a script. My level is set to WARNING. To be outputted into my_log_4_script.log"
)

