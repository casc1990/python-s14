#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
import xml.etree.ElementTree as et
#xml是实现不同语言或程序之间进行数据交换的协议，跟json差不多;至今很多传统公司如金融行业的很多系统的接口还主要是xml。
str_xml = open('city.xml','r',encoding='utf-8')
#print (str_xml.read())  #读取文件内容
tree = et.parse('city.xml')  #直接解析xml文件
root = tree.getroot()  #打印xml根级标签(打印的是内存地址)
print (root.tag)   #<root name="中国">的标签为root
print (root.attrib)  #打印标签的内容。<root name="中国">的标签内容是name="中国"

#遍历xml文档
for one_tag in root:  #循环根级标签（省）
      print (one_tag.tag,one_tag.attrib)  #打印标签名和标签属性 province {'postcode': '610000', 'name': '陕西省'}
      for two_tag in one_tag:   #循环二级标签（市）
          print ('------------')
          print (two_tag.tag,two_tag.attrib) #打印市级标签的标签名和属性。city {'postcode': '610100', 'name': '西安市'}
          for stree_tag in two_tag: #循环三级标签（县）
                print ('\t',stree_tag.tag,stree_tag.attrib) #area {'postcode': '610126', 'name': '高陵县'}
                #print ('\t',stree_tag.text)   .text方法可以获取xml文件里的值。（<gdppc>59900</gdppc>这样的数据用.text获取）

#只取指定的属性
for node in root.iter('gdppc'): #指定要搜索的属性。<gdppc>59911</gdppc>
    print (node.tag,node.text)  #打印属性名和属性值


#xml的增、删、改
import xml.etree.ElementTree as ET

tree = ET.parse("testxml.xml")
root = tree.getroot()

# 修改
for node in root.iter('year'):  #找到要修改的属性
    new_year = int(node.text) + 1  #修改 （属性值加1）
    node.text = str(new_year)    #修改 （变量替换）
    node.set("updated", "yes")   # .set函数追加新属性

tree.write("xmltest.xml")  #写会原文件

# 删除node
for country in root.findall('country'):  #找到所有要修改的标签
    rank = int(country.find('rank').text)  #找到要修改的属性的值
    if rank > 50:
        root.remove(country)  #属性值大于50就删除这个属性

tree.write('output.xml')  #写回到原文件


#创建xml文件文件
new_xml = ET.Element("personinfolist")  #创建根标签
personinfo = ET.SubElement(new_xml, "personinfo", attrib={"enrolled": "yes"}) #创建new_xml下的子标签
name = ET.SubElement(personinfo, "name")  #创建三级标签
name.text = "Alex Li"  #属性赋值
age = ET.SubElement(personinfo, "age", attrib={"checked": "no"})  #同上
sex = ET.SubElement(personinfo, "sex")
age.text = '56'
personinfo2 = ET.SubElement(new_xml, "personinfo", attrib={"enrolled": "no"})
name = ET.SubElement(personinfo2, "name")
name.text = "Oldboy Ran"
age = ET.SubElement(personinfo2, "age")
age.text = '19'

et = ET.ElementTree(new_xml)  # 生成文档对象
et.write("test.xml", encoding="utf-8", xml_declaration=True)  #创建

ET.dump(new_xml)  # 打印生成的格式
