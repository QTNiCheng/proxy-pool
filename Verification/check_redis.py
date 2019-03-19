import random
import sys
import redis
import time
from concurrent.futures import ThreadPoolExecutor
import logging
logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

sys.path.append('../')
import config
from Verification.proxy_check import check


class db_class(object):
    def __init__(self):
        self.__conn = redis.Redis(host=config.redis_host, port=config.redis_port, db=config.db)
        self.name = config.name

    def check_proxy(self):
        executor = ThreadPoolExecutor(max_workers=16)
        if sys.version_info.major == 3:
            proxy_list = [key.decode('utf-8') for key in self.__conn.hgetall(self.name).keys()]
        else:
            proxy_list =  self.__conn.hgetall(self.name).keys()
        for proxy in proxy_list:
            # time.sleep(0.1)
            if executor.submit(check, proxy):
            # if check(proxy):
                pass
                logger.debug("可用代理：{}".format(proxy))
            else:
                logger.info("不可用代理：{}\n从redis中删除".format(proxy))
                self.__conn.hdel(self.name, proxy)


if __name__ == "__main__":
    t1 = time.time()
    db = db_class()
    db.check_proxy()
    print (time.time() - t1)
