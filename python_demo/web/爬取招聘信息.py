from urllib.request import urlopen
import re
p=re.compile('<a href="(/jobs/\\d+)/">(.*?)</a>')
text=urlopen("https://www.python.org/jobs").read().decode()
# print(text)
ary =[]
for url,name in p.findall(text):
    # print('{}({})'.format(name,url))
    print(name,url)
    ary+=[{name:url}]
print(ary)
# res=urlopen('https://www.catac.cn').read()
data1=open('E:\pythonedit.txt',"w")
# print(res)
# print(data.read())
data1.write(str(ary))
#
# data1.close()
# storagePath = "E:\pythonedit.txt"
# def storageToLocalFiles(storagePath, data):
#     fhandle = open(storagePath,"wb")
#     fhandle.write(data)
#     fhandle.close()
# # 调用文件数据保存方法
# storagePath = "E:\pythonedit.txt"
# storageToLocalFiles(storagePath, res)


# import urllib
# import urllib.request
#
# # 抓取页面方法，调用该方法返回抓取到数据
# def read_pageHtml(url):
#     file = urllib.request.urlopen(url)
#     data = file.read()
#     return data
#
# # 传入需要抓取页面的链接 并调用抓取页面方法获得页面数据
# url = "https://www.catac.cn/"
# data = read_pageHtml(url)
# # 控制台打印数据
# print(data)
# # 将数据生成txt文件方法 传入保存文件路径 storagePath 以及文件数据 data
# def storageToLocalFiles(storagePath, data):
#     fhandle = open(storagePath,"wb")
#     fhandle.write(data)
#     fhandle.close()
# # 调用文件数据保存方法
# storagePath = "E:\pythonedit.txt"
# storageToLocalFiles(storagePath, data)
