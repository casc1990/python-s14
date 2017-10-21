#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
__date__ = '2017/10/21 18:50'

from http.server import HTTPServer, CGIHTTPRequestHandler

port = 80

httpd = HTTPServer(('127.0.0.1', port), CGIHTTPRequestHandler)
print("Starting simple_httpd on port: " + str(httpd.server_port))
httpd.serve_forever()