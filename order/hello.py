# 路由功能

from flask import Flask
# 导入imooc文件里变量route_imooc
from order.imooc import route_imooc






app=Flask(__name__)
app.register_blueprint(route_imooc,url_prefix = "/imooc")


@app.route('/')
def hello_world():
    return '这是 /  页面'



@app.route('/api')
def index():
    return 'this is api page'


@app.route('/api/hello')
def api():
    return 'this is  api/hello page'


# gjhkhjkffghgdhctest
# testy






















if __name__ =='__main__':
    app.run(host='0.0.0.0')