from flask import Flask, request
from gevent import pywsgi
import json
from src.image_paddlepaddle import img_load



app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    # msg = request.args['msg']
    with open('template/databind.html') as file_obj:
        html = file_obj.read()
        html = html % (1)
    return html


@app.route('/convert', methods=['GET', 'POST', 'PUT'])
def convert():

    img = request.files['img']
    msg = img_load(img)
    return msg


@app.route('/login', methods=['POST'])
def login():
    result = {
        "flag": False,
        "msg": ""
    }
    params = json.loads(request.get_data())
    if params['account'] == "admin" and params['password'] == "123456":
        result['flag'] = True
    else:
        result['msg'] = "账号数据异常！"
    return result


@app.route('/profiling1', methods=['GET'])
def profiling1():
    msg = request.args['msg']
    with open('template/databind.html') as file_obj:
        html = file_obj.read()
    return html


@app.before_request
def before():
    """
    针对app实例定义全局拦截器
    """
    url = request.path  # 读取到当前接口的地址
    print(url)
    pass


if __name__ == '__main__':
    server = pywsgi.WSGIServer(('0.0.0.0', 5050), app)
    server.serve_forever()
