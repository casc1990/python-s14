#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
import shutil,zipfile,tarfile
#zipfile zip压缩与解压缩
#zip压缩
f = zipfile.ZipFile('backup.zip','w')  #backup.zip：要压缩的压缩包名；w:表示创建一个zip文件（r表示读取zip文件）
f.write('test')  #要压缩的文件1
f.write('test1.txt')  #要压缩的文件2
#f.write("test/111.txt", "test22/111.txt")   把test/111压缩到test22/111.txt里
f.close()  #必须关闭后才能压缩

#zip解压
f1 = zipfile.ZipFile('backup.zip','r') #backup.zip：要读取的压缩包名；r：读取zip文件
a = f1.namelist()  # f1.namelist() 会返回压缩包内所有文件名的列表形式。 ['test', 'test1.txt']
print (a)
for i in f1.namelist():
    print (i)    #循环列表，打印每一个文件
f2 = zipfile.ZipFile('backup.zip','r')
for i in f2.infolist():   #f2.infolist() 返回压缩包内所有文件的信息(列表形式)
    print (i.filename,i.file_size,i.header_offset)  #i.filename：文件名；i.file_size：文件大小\
#                                           i.header_offset:偏移。输出如：test1.txt 21730 21764
f3 = zipfile.ZipFile('backup.zip','r')
print (f3.read(f3.namelist()[0]))  #f3.read()方法可以读取文件内容（取第一个文件，读取文件内容）

#tarfile tar压缩与解压缩
#tar压缩
f4 = tarfile.open('backup.tar.gz','w:gz')  #tarfile.open()表示对tar进行处理；backup.tar.gz：压缩包名称\
#                  'w:gz'表示创建压缩文件(w)，并且格式是gzip格式的(gz). bz:bzip2
f4.add('test')  #要压缩的文件1
f4.add('test1.txt')  #要压缩的文件2
f4.close()  #必须关闭后才能压缩

#tar解压
f5 = tarfile.open('backup.tar.gz','r:gz')  #用gzip方式解压backup.tar.gz
#f5.extract()  #一条一条解压
f5.extractall() #将所有文件解压到当前。加上绝对路径就解压到指定路径
f5.close()  #关闭文件



#tarfile  tar压缩与解压缩


print ('shutil 是高级的文件，文件夹，压缩包处理模块。')
#shutil.copyfileobj(fsrc, fdst[, length])  将文件内容拷贝到另一个文件中
#shutil.copyfileobj(open('test','r',encoding='utf-8'),open('test1.txt','w',encoding='utf-8'))

#shutil.copyfile(src, dst)

#shutil.copymode(src, dst)

#shutil.copystat(src, dst)

#shutil.copy(src, dst)

#shutil.copy2(src, dst)

#shutil.ignore_patterns(*patterns)
#shutil.copytree(src, dst, symlinks=False, ignore=None)

#shutil.rmtree(path[, ignore_errors[, onerror]])

#shutil.move(src, dst)

#shutil.make_archive(base_name, format,...)
print ('''
创建压缩包并返回文件路径，例如：zip、tar

    base_name： 压缩包的文件名，也可以是压缩包的路径。只是文件名时，则保存至当前目录，否则保存至指定路径，
    如：www                        =>保存至当前路径
    如：/Users/wupeiqi/www =>保存至/Users/wupeiqi/
    format： 压缩包种类，“zip”, “tar”, “bztar”，“gztar”
    root_dir： 要压缩的文件夹路径（默认当前目录）
    owner： 用户，默认当前用户
    group： 组，默认当前组
    logger： 用于记录日志，通常是logging.Logger对象
''')
print ('shutil 对压缩包的处理是通过调用ZipFile 和 TarFile两个模块来进行的。')


#