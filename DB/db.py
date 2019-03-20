import random
import sys
import redis
import time
import logging
sys.path.append('../')
import config
from Verification.proxy_check import check
import logging
logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class db_class(object):
    def __init__(self):
        self.__conn = redis.Redis(host=config.redis_host, port=config.redis_port, db=config.db)
        self.name = config.name

    def save_proxy(self, proxy):
        time.sleep(0.1)
        if check(proxy):
            logger.info("{}：验证通过，写入redis".format(proxy))
            self.__conn.hset(self.name, proxy, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

    def get_proxy(self):
        key = self.__conn.hgetall(name=self.name)
        # return random.choice(key.keys()) if key else None
        # key.keys()在python3中返回dict_keys，不支持index，不能直接使用random.choice
        # 另：python3中，redis返回为bytes,需要解码
        rand_key = random.choice(list(key.keys())) if key else None
        if isinstance(rand_key, bytes):
            return rand_key.decode('utf-8')
        else:
            return rand_key

    def get_all_proxy(self):
        if sys.version_info.major == 3:
            return [key.decode('utf-8') for key in self.__conn.hgetall(self.name).keys()]
        else:
            return self.__conn.hgetall(self.name).keys()

    def del_proxy(self, proxy):
        self.__conn.hdel(self.name, proxy)





