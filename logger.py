import logging
import os

log_level = os.environ.get('LOG_LEVEL', 'INFO').upper()

def get_level_name(level_number):
  """Returns the name of the logging level for the given number."""
  return logging.getLevelName(level_number)

def setup_logging():
    log_level_str = os.environ.get("LOG_LEVEL", "INFO").upper()
    try:
        log_level = getattr(logging, log_level_str)

    except AttributeError:
        log_level = logging.INFO
        print(f"Invalid log level '{log_level_str}' in environment variable. Defaulting to INFO.")
    
    level_name = get_level_name(log_level)
    print(f"Setting up logger with level {level_name}")
    logging.basicConfig(level=log_level, format='%(asctime)s %(levelname)s %(pathname)s:%(lineno)d:%(funcName)s %(message)s')

# Just call to setup logging before anything...
setup_logging()


def get_logger(source_name):
    """
    Gets the configured logger
    """
    logger = logging.getLogger(source_name)

    class ShortPathFormatter(logging.Formatter):
       def format(self, record):
           # Get the filename and truncate it
           filename = os.path.basename(record.filename)
           
           # Customize the format string
           log_format = f'%(asctime)s {filename}:%(lineno)d %(levelname)s - %(message)s'

           # Create a new Formatter instance with the customized format
           formatter = logging.Formatter(log_format)
           # Return the formatted log message
           return formatter.format(record)


    handler = logging.StreamHandler()
    handler.setFormatter(ShortPathFormatter())
 
    logger.addHandler(handler)

    return logger

