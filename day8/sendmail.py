#!/usr/bin/env python
#- coding:utf-8
import pymysql
import datetime,requests,os,sys
#reload(sys)
sys.setdefaultencoding('utf-8')
#tolist = "iaas_ops@jd.com"
email_list = "pengbo@jd.com"
resource = {'CPU':'cpu','MEM':'memory','DISK':'disk'}
#WorkPath = '/export/Data/user_list'
Today = (datetime.datetime.now() + datetime.timedelta(days=-1)).strftime("%Y-%m-%d")

HtmlContent = '''
 <html xmlns:v="urn:schemas-microsoft-com:vml"
        xmlns:o="urn:schemas-microsoft-com:office:office"
        xmlns:x="urn:schemas-microsoft-com:office:excel"
        xmlns="http://www.w3.org/TR/REC-html40">
        
        <head>
        
        
        </head>
        
        <body link=blue vlink=purple>
        
        <style type="text/css">
        table.gridtable {
            font-family: verdana,arial,sans-serif;
            font-size:16px;
            color:#333333;
            border-width: 2px;
            border-color: #666666;
            border-collapse: collapse;
        }

        table.gridtable th {
            border-width: 1px;
            text-align: left;
            padding: 8px;
            border-style: solid;
            border-color: #666666;
            background-color: #b8d1f3;
        }
        table.gridtable td {
            border-width: 1px;
            padding: 8px;
            border-style: solid;
            border-color: #666666;
/*            background-color: #ffffff;*/
        }

        .font {
            font-family: verdana,arial,sans-serif;
            font-size:16px;      
            color:#FF0000 ;      
        }
        </style>
        
        <!-- Table goes in the document BODY -->
        <table class="gridtable">
        <th>产品类型</th><th>机房</th><th>资源类型</th><th>总资源</th><th>可用资源</th><th>已用资源</th>%s</table>
        </html>
'''
MailContent = ''
postdata = ''

class MysqlConf(object):
    def __init__(self, host, port, user, passwd, db):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.db = db
    def select_cpu(self,resource_type):
        conn = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.db,
                               charset='utf8')
        cursor = conn.cursor()
        resource_used_dict = {}
        resource_total_used_sql = "select sum(f.%s) as %s from instance i inner join space s on i.space_id=s.space_id inner join flavor f on s.flavor_id=f.flavor_id where i.host_ip in (select ip from host);" % (resource_type,resource_type)
        resource_constant_sql = "select %s from host" % resource_type
        host_num_sql = "select count(*) as host_num from host;"
        resource_constant_cursor = cursor.execute(resource_constant_sql)
        resource_constant_data = int(cursor.fetchall()[0][0])   #各资源的常量，如cpu为64核
        if resource_type == 'memory' or resource_type == 'disk':
            resource_total_used_cursor = cursor.execute(resource_total_used_sql)
            resource_total_used_data = int(cursor.fetchall()[0][0]) / 1024 / 1024 / 1024  # 总使用量
            resource_total_size_cursor = cursor.execute(host_num_sql)
            resource_total_size_data = int(cursor.fetchall()[0][0]) * resource_constant_data / 1024 / 1024 / 1024.0 * 0.8  #总大小
        if resource_type == 'cpu':
            resource_total_used_cursor = cursor.execute(resource_total_used_sql)
            resource_total_used_data = int(cursor.fetchall()[0][0])  # 总使用量
            resource_total_size_cursor = cursor.execute(host_num_sql)
            resource_total_size_data = int(cursor.fetchall()[0][0]) * resource_constant_data  #总大小
        resource_total_free_data = resource_total_size_data - resource_total_used_data  # 总剩余量
        conn.close()
        resource_used_dict = {'product':'jmiss-mongo','idc':'bj02','resource_type': resource_type,\
        'total':resource_total_size_data,'used':resource_total_used_data,'free':resource_total_free_data}
        print '总使用数：',resource_total_used_data
        print '资源常量:',resource_constant_data
        print '资源总量:',resource_total_size_data
        print '总剩余量:',resource_total_free_data
        print '返回的字典:',resource_used_dict

        return resource_used_dict


cpu_info = MysqlConf("172.19.29.18",3358,"iaas_ops_ro","httznVWLvlUsC51UsjZk","jmiss_mongo_prod_hb")
#result_data = cpu_info.select_cpu('cpu')

for i,j in resource.items():
    result_data = cpu_info.select_cpu(j)
    if j == 'cpu':
        total = str(result_data['total']) + ' core'
        used =  str(result_data['used']) + ' core'
        free =  str(result_data['free']) + ' core'
    else:
        total = str(result_data['total']) + ' GB'
        used = str(result_data['used']) + ' GB'
        free = str(result_data['free']) + ' GB'
    MailContent += '<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>' %\
                   (result_data['product'],result_data['idc'],result_data['resource_type'],total,used,free)
TotalContent = HtmlContent % MailContent
postdata = {'tolist':email_list,'subject':'资源使用趋势','content':TotalContent}

print '-----发送邮件的表格内容-----:',MailContent
print '-----邮件的总html格式内容----------', TotalContent
print '-----post到邮件里的数据-------------',postdata

if __name__ == "__main__":
    r = requests.post('http://mail.iaas.jcloud.com',data=postdata)
    print r.text


