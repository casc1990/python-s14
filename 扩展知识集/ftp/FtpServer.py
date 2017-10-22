#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
__date__ = '2017/10/21 16:09'

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler, ThrottledDTPHandler
from pyftpdlib.servers import FTPServer
import settings
import logging


def get_user(userfile):
    # 定义一个用户列表
    user_list = []
    with open(userfile,encoding='utf-8') as f:
        for line in f:
            if not line.startswith('#') and line:
                if len(line.split()) == 4:
                    user_list.append(line.split())
                else:
                    print("user.conf配置错误")
    return user_list


def ftp_server():
    # 实例化虚拟用户，这是FTP验证首要条件
    authorizer = DummyAuthorizer()

    # 添加用户权限和路径，括号内的参数是(用户名， 密码， 用户目录， 权限)
    # authorizer.add_user('user', '12345', '/home/', perm='elradfmw')
    user_list = get_user('user')
    for user in user_list:
        name, passwd, permit, homedir = user
        try:
            authorizer.add_user(name, passwd, homedir, perm=permit)
        except Exception as e:
            print(e)

    # 添加匿名用户 只需要路径
    if settings.enable_anonymous == 'on':
        authorizer.add_anonymous(settings.anonymous_path)

    # 下载上传速度设置
    dtp_handler = ThrottledDTPHandler
    dtp_handler.read_limit = settings.max_download
    dtp_handler.write_limit = settings.max_upload

    # 初始化ftp句柄
    handler = FTPHandler
    handler.authorizer = authorizer

    # 日志记录
    if settings.enable_logging == 'on':
        logging.basicConfig(filename=settings.loging_name, level=logging.INFO)

    # 欢迎信息
    handler.banner = settings.welcome_msg

    # 添加被动端口范围
    handler.passive_ports = range(settings.passive_ports[0], settings.passive_ports[1])

    # 监听ip 和 端口
    server = FTPServer((settings.ip, settings.port), handler)

    # 最大连接数
    server.max_cons = settings.max_cons
    server.max_cons_per_ip = settings.max_per_ip

    # 开始服务
    print('开始服务')
    server.serve_forever()


if __name__ == "__main__":
    ftp_server()