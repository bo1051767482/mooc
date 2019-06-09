# 蓝牙功能


from flask import Blueprint


route_imooc=Blueprint("imooc_page",__name__)


@route_imooc.route("/")
def page1():
    return '蓝牙'

@route_imooc.route("/api")
def page2():
    return '蓝牙this is api page'
