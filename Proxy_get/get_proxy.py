import re
import sys
from concurrent.futures import ThreadPoolExecutor
import threading
sys.path.append('../')

from Util.Function import get_html_tree
from Util.Function import get_web_data
from DB.db import db_class


class get_proxy(object):
    """
    proxy getter
    """

    def __init__(self):
        pass

    @staticmethod
    def Proxy_5U():
        """
        无忧代理 http://www.data5u.com/
        :return:
        """
        url = 'http://www.data5u.com/free/gngn/index.shtml'
        html_tree = get_html_tree(url)
        ul_list = html_tree.xpath('//ul[@class="l2"]')  # /html/body/div[5]/ul/li[2]/ul[2]/span[1]/li
        for ul in ul_list:
            try:
                http_s = ul.xpath('.//li/a/text()')[1]
                http_s = http_s.lower()
                ip = ':'.join(ul.xpath('.//li/text()')[0:2])
                # print("{}://{}".format(http_s, ip))
                # print("{}://{}".format(http_s, ip))  # /html/body/div[5]/ul/li[2]/ul/span[4]/li/a
                db_class().save_proxy("{}://{}".format(http_s, ip))
            except Exception as e:
                print(e)

    @staticmethod
    def Proxy_66ip():
        """
        代理66 http://www.66ip.cn/
        :param area: 抓取代理页数，page=1北京代理页，page=2上海代理页......
        :param page: 翻页
        :return:
        """
        for area_index in range(1, 33):
            for i in range(1, 11):
                url = "http://www.66ip.cn/areaindex_{}/{}.html".format(area_index, i)
                html_tree = get_html_tree(url)
                tr_list = html_tree.xpath("//*[@id='footer']/div/table/tr[position()>1]")
                if len(tr_list) == 0:
                    continue
                for tr in tr_list:
                    db_class().save_proxy("http://" + tr.xpath("./td[1]/text()")[0] + ":" + tr.xpath("./td[2]/text()")[0])

    @staticmethod
    def Proxy_xici():
        """
        西刺代理 http://www.xicidaili.com
        :return:
        """
        for page in range(1, 50):
            url = 'http://www.xicidaili.com/nn/{page}'.format(page=page)
            tree = get_html_tree(url)
            proxy_list = tree.xpath('.//table[@id="ip_list"]//tr[position()>1]')
            for proxy in proxy_list:
                try:
                    http_s = proxy.xpath('./td/text()')[5]
                    ip = ':'.join(proxy.xpath('./td/text()')[0:2])
                    db_class().save_proxy("{}://{}".format(http_s.lower(), ip))
                except Exception as e:
                    print(e)

    @staticmethod
    def Proxy_kuaidaili():
        """
        快代理 https://www.kuaidaili.com
        """
        for page in range(1, 50):
            url = 'https://www.kuaidaili.com/free/inha/{page}/'.format(page=page)
            tree = get_html_tree(url)
            proxy_list = tree.xpath('.//table//tr')
            for tr in proxy_list[1:]:
                db_class().save_proxy("http://" + ':'.join(tr.xpath('./td/text()')[0:2]))

    @staticmethod
    def Proxy_manong():
        """
        码农代理 https://proxy.coderbusy.com/
        :return:
        """
        for page in range(1, 50):
            url = 'https://proxy.coderbusy.com/classical/country/cn.aspx?page={page}'.format(page=page)
            web_data = get_web_data(url)
            proxies = re.findall('data-ip="(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})".+?>(\d+)</td>', web_data)
            try:
                for proxy in proxies:
                    tem = ("http://{}".format(':'.join(proxy)))
                    db_class().save_proxy(tem)
            except Exception as e:
                print(e)


def run():
    t_list = [threading.Thread(target=get_proxy.Proxy_66ip), threading.Thread(target=get_proxy.Proxy_5U),
              threading.Thread(target=get_proxy.Proxy_kuaidaili), threading.Thread(target=get_proxy.Proxy_manong),
              threading.Thread(target=get_proxy.Proxy_xici)]
    for t in t_list:
        t.start()
    for t_ in t_list:
        t_.join()


# if __name__ == '__main__':
#     run()
