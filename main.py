import settings
from koemotion import Koemotion
from logging import FileHandler, getLogger, StreamHandler, DEBUG, INFO, Formatter

logger = getLogger(__name__)
logger.setLevel(DEBUG)

# file handler
fh: FileHandler = FileHandler('log/main.log', encoding='utf-8', mode='a')
fh.setLevel(DEBUG)
formatter = Formatter('[%(asctime)s] %(name)s %(levelname)s: %(lineno)d: %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

# stream handler
ch: StreamHandler = StreamHandler()
ch.setLevel(INFO)
console_formatter = Formatter('[%(asctime)s] %(name)s %(levelname)s: %(lineno)d: %(message)s')
ch.setFormatter(console_formatter)
logger.addHandler(ch)



def main():

    KOEMOTION_API_KEY = settings.KOEMOTION_API_KEY
    logger.debug(KOEMOTION_API_KEY)




if __name__ == '__main__':
    main()
