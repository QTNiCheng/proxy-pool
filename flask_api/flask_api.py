from flask import Flask, jsonify, Response, request
import sys
app = Flask(__name__)

sys.path.append('../')
from DB.db import db_class
import config


class JsonResponse(Response):

    @classmethod
    def force_type(cls, response, environ=None):
        if isinstance(response, (dict, list)):
            response = jsonify(response)

        return super(JsonResponse, cls).force_type(response, environ)


app.response_class = JsonResponse


@app.route('/')
def index():
    api_list = {
        'get': u'get an usable proxy',
        'get_all': u'get all proxy from proxy pool',
        'delete?proxy=127.0.0.1:8080': u'delete an unable proxy',
        'get_status': u'proxy statistics'
    }
    return api_list


@app.route('/get')
def get_proxy():
    proxy = db_class().get_proxy()
    return proxy if proxy else 'no proxy!'


@app.route('/get_all/')
def get_all():
    proxy_all = db_class().get_all_proxy()
    return proxy_all


@app.route('/delete/', methods=['GET'])
def delete():
    proxy = request.args.get('proxy')
    db_class().del_proxy(proxy)
    return 'success'


def run():
    app.debug = False
    app.run(host=config.flask_host, port=config.flask_port)


if __name__ == '__main__':
    app.debug = True
    app.run()