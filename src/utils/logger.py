from loguru import logger
import sys
import logging

# Define a unified log format string
log_format = "{time:YYYY-MM-DD HH:mm:ss} | {level} | {module}:{function}:{line} - {message}"

# Configure Loguru and remove the default logging configuration
logger.remove()

# Use a unified log format to configure standard output and standard error output, support colored display
logger.add(sys.stdout, level="DEBUG", format=log_format, colorize=True)
logger.add(sys.stderr, level="ERROR", format=log_format, colorize=True)

# Configure log file output using the same unified format, with automatic rotation when the file size reaches 1MB
logger.add("logs/app.log", rotation="1 MB", level="DEBUG", format=log_format)

# Set an alias for the logger to make it easier to import and use in other modules.
LOG = logger

# Make the LOG variable public to allow other modules to use it via from logger import LOG
__all__ = ["LOG"]
