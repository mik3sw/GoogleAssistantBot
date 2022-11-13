import logging
from rich.logging import RichHandler
from rich.console import Console
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
    if context.error == "argument of type 'NoneType' is not iterable":
        pass
    else:
        logger.info('[LOG] errore: {}'.format(context.error))

def log(msg):
    console = Console()
    console.log(msg)


'''import logging


FORMAT = "%(message)s"
logging.basicConfig(
    level="NOTSET", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
)

log = logging.getLogger("rich")
log.info("Hello, World!")'''