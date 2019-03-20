import re
import sys
import requests
import logging
logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
sys.path.append('../')
from Util.RandomHeader import randHeader


def check(proxy):
    verify_regex = r"\w{3,5}\://\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}"
    try:
        r = requests.get("https://www.baidu.com", timeout=2, headers=randHeader(),  proxies={"{http}": "{proxy}"
                         .format(http=proxy[:proxy.index(":")], proxy=proxy)})
        _proxy = re.findall(verify_regex, proxy)
        return True if len(_proxy) == 1 and _proxy[0] == proxy and r.status_code == 200 else False
    except Exception as e:
        logger.info("{}：验证超时，不通过".format(proxy))
        print(e)



