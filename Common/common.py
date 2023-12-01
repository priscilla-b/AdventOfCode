import logging

def get_logger(log_level='debug'):

    log_level = getattr(logging, log_level.upper(), None)
    
    if log_level is None or not isinstance(log_level, int):
        raise ValueError(f"Invalid log level: {log_level}")
    
    logging.basicConfig(format="%(asctime)s.%(msecs)03d:%(levelname)s:%(name)s:\t%(message)s", 
                    datefmt='%H:%M:%S')
    logger = logging.getLogger(__name__)
    logger.setLevel(log_level)

    return logger