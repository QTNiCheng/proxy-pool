# import sys
# import time
# sys.path.append('../')
# from Proxy_get.get_proxy import get_proxy
# from DB.db import db_class
#
#
# def save_db():
#     # while True:
#         print('开始抓取IP并存入数据库···')
#         for a, b, c, d, e in zip(get_proxy.Proxy_5U(), get_proxy.Proxy_66ip(), get_proxy.Proxy_xici(),
#                                  get_proxy.Proxy_kuaidaili(), get_proxy.Proxy_manong()):
#             db_class().save_proxy(a)
#             db_class().save_proxy(b)
#             db_class().save_proxy(c)
#             db_class().save_proxy(d)
#             db_class().save_proxy(e)
#         # time.sleep()
