import logging

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

logger.info('Start reading database')


records = {'john':55, 'tom':66}
logger.debug('Recodrs: %s',records)
logger.info('Updateing records ...')
logger.info('Finish updating records')