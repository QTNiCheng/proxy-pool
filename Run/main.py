import sys
from multiprocessing import Process
import logging
logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

sys.path.append('../')
from Proxy_get.get_proxy import run as get_proxy
from flask_api.flask_api import run as flask_run
from Verification.check_redis import db_class
import config

def run():
    p_list = list()
    if config.check_redis:
        logger.info('开启redis中的代理验证~~~~~')
        db = db_class()
        p0 = Process(target=db.check_proxy(), name='check_proxy')
        p_list.append(p0)
    if config.updata_proxy:
        logger.info('开启redis中的代理更新~~~~~')
        p1 = Process(target=get_proxy, name='get_proxy')
        p_list.append(p1)
    logger.info('启动flask-API~~~~~')
    p2 = Process(target=flask_run, name='flask_run')
    p_list.append(p2)

    for p in p_list:
        p.daemon = True
        p.start()
    for p in p_list:
        p.join()


if __name__ == '__main__':
    run()


