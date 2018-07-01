import sys
from multiprocessing import Process

sys.path.append('../')
from Proxy_get.get_proxy import run as get_proxy
from flask_api.flask_api import run as flask_run


def run():
    p_list = list()
    p1 = Process(target=get_proxy, name='get_proxy')
    p_list.append(p1)
    p2 = Process(target=flask_run, name='flask_run')
    p_list.append(p2)

    for p in p_list:
        p.daemon = True
        p.start()
    for p in p_list:
        p.join()


if __name__ == '__main__':
    run()


