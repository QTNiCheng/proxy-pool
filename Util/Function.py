import requests
import time
from lxml import etree
import sys

sys.path.append("../")
from Util import RandomHeader


def get_html_tree(url):
    """
    获取html树
    :param url:
    :return:
    """
    # delay 2s for per request
    try:
        header = RandomHeader.randHeader()
        html = requests.get(url=url, headers=header).content
        return etree.HTML(html)
    except Exception as e:
        print(e)


def get_web_data(url):
    try:
        header = RandomHeader.randHeader()
        web_data = requests.get(url=url, headers=header).text
        return web_data
    except Exception as e:
        print(e)

