import logging
from rich.logging import RichHandler
#level=logging.INFO
FORMAT = "%(message)s"
#FORMAT='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(
    format=FORMAT, 
    level="NOTSET",
    datefmt="[%X]", 
    handlers=[RichHandler()]
)

#logger = logging.getLogger(__name__)
logger = logging.getLogger("rich")
def init(update, context):
    logger.info('[LOG] errore: {}'.format(context.error))


'''import logging


FORMAT = "%(message)s"
logging.basicConfig(
    level="NOTSET", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
)

log = logging.getLogger("rich")
log.info("Hello, World!")'''