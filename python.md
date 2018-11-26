

# python学习重点笔记

## 1. Python3 的六个标准数据类型：

- **不可变数据（3 个）：**Number（数字）、String（字符串）、Tuple（元组）；
- **可变数据（3 个）：**List（列表）、Dictionary（字典）、Set（集合）。

 **加号 + 是列表连接运算符，星号 * 是重复操作，+相当于js的concat，而*更厉害，是对数组内容重复：[a,b]\*2 == [a,b,a,b]，字符串页可以用\*来重复内容** 

**元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开。**

集合（set类型）与js定义相似。

字典（Dictionary）：键值对，

### 1.1 Python数据类型转换

有时候，我们需要对数据内置的类型进行转换，数据类型的转换，你只需要将数据类型作为函数名即可。

以下几个内置的函数可以执行数据类型之间的转换。这些函数返回一个新的对象，表示转换的值。

| 函数                                                         | 描述                                                |
| ------------------------------------------------------------ | --------------------------------------------------- |
| [int(x [,base\])](http://www.runoob.com/python3/python-func-int.html) | 将x转换为一个整数                                   |
| [float(x)](http://www.runoob.com/python3/python-func-float.html) | 将x转换到一个浮点数                                 |
| [complex(real [,imag\])](http://www.runoob.com/python3/python-func-complex.html) | 创建一个复数                                        |
| [str(x)](http://www.runoob.com/python3/python-func-str.html) | 将对象 x 转换为字符串                               |
| [repr(x)](http://www.runoob.com/python3/python-func-repr.html) | 将对象 x 转换为表达式字符串                         |
| [eval(str)](http://www.runoob.com/python3/python-func-eval.html) | 用来计算在字符串中的有效Python表达式,并返回一个对象 |
| [tuple(s)](http://www.runoob.com/python3/python3-func-tuple.html) | 将序列 s 转换为一个元组                             |
| [list(s)](http://www.runoob.com/python3/python3-att-list-list.html) | 将序列 s 转换为一个列表                             |
| [set(s)](http://www.runoob.com/python3/python-func-set.html) | 转换为可变集合                                      |
| [dict(d)](http://www.runoob.com/python3/python-func-dict.html) | 创建一个字典。d 必须是一个序列 (key,value)元组。    |
| [frozenset(s)](http://www.runoob.com/python3/python-func-frozenset.html) | 转换为不可变集合                                    |
| [chr(x)](http://www.runoob.com/python3/python-func-chr.html) | 将一个整数转换为一个字符                            |
| [ord(x)](http://www.runoob.com/python3/python-func-ord.html) | 将一个字符转换为它的整数值                          |
| [hex(x)](http://www.runoob.com/python3/python-func-hex.html) | 将一个整数转换为一个十六进制字符串                  |
| [oct(x)](http://www.runoob.com/python3/python-func-oct.html) | 将一个整数转换为一个八进制字符串                    |



## 2. GUI

引入Tkinter 工具库，

给控件加事件，1： 控件["command"]=函数名 

​			   2：控件.bind("事件名"，函数名) 

布局管理器：控件.pack（）这样控件才能显示



## 3. 网络编程

网络编程里的一个基础组件:套接字(socket) ，提供了两个方法（send，recv） 用来发送与接收，socket.gethostname ：获取当前主机名

模块：urllib1与urllib2

urllib2.request()  与urllib2.urlopen()



获取远程文件：urlretrieve(“url”,"副本文件地址") 获取网页内容，存在副本文件中



## 4. 面向web

读取本地文件用 open()

读取网络文件  引入 urllib.request   ，使用urlopen()

​     import urllib.request  

urllib.request.urlopen()

获取到文件或者网页之后，读取内容用 read()，解码用decode（），常用于中文解码

从英文意思上看，encode和decode分别指编码和解码。在python中，Unicode类型是作为编码的基础类型，即：

            decode                 encode
      str ---------> str(Unicode) ---------> str


### 4.1 re模块中常用功能函数

**正则模块 re**

#### **1、compile()**

编译正则表达式模式，返回一个对象的模式。（可以把那些常用的正则表达式编译成正则表达式对象，这样可以提高一点效率。）

格式：

re.compile(pattern,flags=0)

pattern: 编译时用的表达式字符串。

flags 编译标志位，用于修改正则表达式的匹配方式，如：是否区分大小写，多行匹配等。常用的flags有：

| 标志               | 含义                                                     |
| ------------------ | -------------------------------------------------------- |
| re.S(DOTALL)       | 使.匹配包括换行在内的所有字符                            |
| re.I（IGNORECASE） | 使匹配对大小写不敏感                                     |
| re.L（LOCALE）     | 做本地化识别（locale-aware)匹配，法语等                  |
| re.M(MULTILINE)    | 多行匹配，影响^和$                                       |
| re.X(VERBOSE)      | 该标志通过给予更灵活的格式以便将正则表达式写得更易于理解 |
| re.U               | 根据Unicode字符集解析字符，这个标志影响\w,\W,\b,\B       |



```python

```



#### **2、match()**

决定RE是否在字符串刚开始的位置匹配。//注：这个方法并不是完全匹配。当pattern结束时若string还有剩余字符，仍然视为成功。想要完全匹配，可以在表达式末尾加上边界匹配符'$'

格式：

re.match(pattern, string, flags=0)

```python
print(re.match('com','comwww.runcomoob').group())
print(re.match('com','Comwww.runcomoob',re.I).group())
执行结果如下：
com
com
```



#### **3、search()**

 格式：

re.search(pattern, string, flags=0)

re.search函数会在字符串内查找模式匹配,只要找到第一个匹配然后返回，如果字符串没有匹配，则返回None。

```
print(re.search('\dcom','www.4comrunoob.5com').group())
执行结果如下：
4com
```

*注：match和search一旦匹配成功，就是一个match object对象，而match object对象有以下方法：

- group() 返回被 RE 匹配的字符串
- start() 返回匹配开始的位置
- end() 返回匹配结束的位置
- span() 返回一个元组包含匹配 (开始,结束) 的位置
- group() 返回re整体匹配的字符串，可以一次输入多个组号，对应组号匹配的字符串。

a. group（）返回re整体匹配的字符串，
b. group (n,m) 返回组号为n，m所匹配的字符串，如果组号不存在，则返回indexError异常
c.groups（）groups() 方法返回一个包含正则表达式中所有小组字符串的元组，从 1 到所含的小组号，通常groups()不需要参数，返回一个元组，元组中的元就是正则表达式中定义的组。 

```python
import re
a = "123abc456"
 print(re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(0))   #123abc456,返回整体
 print(re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(1))   #123
 print(re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(2))   #abc
 print(re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(3))   #456
###group(1) 列出第一个括号匹配部分，group(2) 列出第二个括号匹配部分，group(3) 列出第三个括号匹配部分。###
```

  

#### **4、findall()**

re.findall遍历匹配，可以获取字符串中所有匹配的字符串，**返回一个列表。**

 格式：

re.findall(pattern, string, flags=0)

```python
p = re.compile(r'\d+')
print(p.findall('o1n2m3k4'))
执行结果如下：
['1', '2', '3', '4']
```



```python
import re
tt = "Tina is a good girl, she is cool, clever, and so on..."
rr = re.compile(r'\w*oo\w*')
print(rr.findall(tt))
print(re.findall(r'(\w)*oo(\w)',tt))#()表示子表达式 
执行结果如下：
['good', 'cool']
[('g', 'd'), ('c', 'l')]
```



#### **5、split()**

按照能够匹配的子串将string分割后返回列表。

可以使用re.split来分割字符串，如：re.split(r'\s+', text)；将字符串按空格分割成一个单词列表。

格式：

re.split(pattern, string[, maxsplit])

maxsplit用于指定最大分割次数，不指定将全部分割。

```python
print(re.split('\d+','one1two2three3four4five5'))
执行结果如下：
['one', 'two', 'three', 'four', 'five', '']
```



#### **6、sub()**

使用re替换string中每一个匹配的子串后返回替换后的字符串。

格式：

re.sub(pattern, repl, string, count)

按 Ctrl+C 复制代码

按 Ctrl+C 复制代码

re.sub还允许使用函数对匹配项的替换进行复杂的处理。

如：re.sub(r'\s', lambda m: '[' + m.group(0) + ']', text, 0)；将字符串中的空格' '替换为'[ ]'。

```python
import re
text = "JGood is a handsome boy, he is cool, clever, and so on..."
print(re.sub(r'\s+', lambda m:'['+m.group(0)+']', text,0))
执行结果如下：
JGood[ ]is[ ]a[ ]handsome[ ]boy,[ ]he[ ]is[ ]cool,[ ]clever,[ ]and[ ]so[ ]on...
```



#### **7、subn()**

 返回替换次数

格式：

subn(pattern, repl, string, count=0, flags=0)

```python
print(re.subn('[1-2]','A','123456abcdef'))
print(re.sub("g.t","have",'I get A,  I got B ,I gut C'))
print(re.subn("g.t","have",'I get A,  I got B ,I gut C'))
执行结果如下：
('AA3456abcdef', 2)
I have A,  I have B ,I have C
('I have A,  I have B ,I have C', 3)
```



#### 8、注意点

**1、re.match与re.search与re.findall的区别：**

re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；而re.search匹配整个字符串，直到找到一个匹配。

```python
a=re.search('[\d]',"abc33").group()
print(a)
p=re.match('[\d]',"abc33")
print(p)
b=re.findall('[\d]',"abc33")
print(b)
执行结果：
3
None
['3', '3']
```

**2、贪婪匹配与非贪婪匹配**

*?,+?,??,{m,n}?    前面的*,+,?等都是贪婪匹配，也就是尽可能匹配，后面加?号使其变成惰性匹配



```python
a = re.findall(r"a(\d+?)",'a23b')
print(a)
b = re.findall(r"a(\d+)",'a23b')
print(b)
执行结果：
['2']
['23']
```



```python
a = re.match('<(.*)>','<H1>title<H1>').group()
print(a)
b = re.match('<(.*?)>','<H1>title<H1>').group()
print(b)
执行结果：
<H1>title<H1>
<H1>
```



**3、用flags时遇到的小坑**

```python
print(re.split('a','1A1a2A3',re.I))#输出结果并未能区分大小写
这是因为re.split(pattern，string，maxsplit,flags)默认是四个参数，当我们传入的三个参数的时候，系统会默认re.I是第三个参数，所以就没起作用。如果想让这里的re.I起作用，写成flags=re.I即可。 
```



#### 9、正则的小实践

1、匹配电话号码

```python
p = re.compile(r'\d{3}-\d{6}')
print(p.findall('010-628888'))
```

2、匹配IP

```python
re.search(r"(([01]?\d?\d|2[0-4]\d|25[0-5])\.){3}([01]?\d?\d|2[0-4]\d|25[0-5]\.)","192.168.1.1")
```



#### 10、str.format() 的基本使用如下:

```python
>>> print('{}网址： "{}!"'.format('菜鸟教程', 'www.runoob.com'))
菜鸟教程网址： "www.runoob.com!"
```

括号及其里面的字符 (称作格式化字段) 将会被 format() 中的参数替换。

在括号中的数字用于指向传入对象在 format() 中的位置，如下所示：

```python
>>> print('{0} 和 {1}'.format('Google', 'Runoob'))
Google 和 Runoob
>>> print('{1} 和 {0}'.format('Google', 'Runoob'))
Runoob 和 Google
```

如果在 format() 中使用了关键字参数, 那么它们的值会指向使用该名字的参数。

```python
>>> print('{name}网址： {site}'.format(name='菜鸟教程', site='www.runoob.com'))
菜鸟教程网址： www.runoob.com
```

位置及关键字参数可以任意的结合:

```python
>>> print('站点列表 {0}, {1}, 和 {other}。'.format('Google', 'Runoob',
                                                       other='Taobao'))
站点列表 Google, Runoob, 和 Taobao。
```

'!a' (使用 ascii()), '!s' (使用 str()) 和 '!r' (使用 repr()) 可以用于在格式化某个值之前对其进行转化:



```python
>>> import math
>>> print('常量 PI 的值近似为： {}。'.format(math.pi))
常量 PI 的值近似为： 3.141592653589793。
>>> print('常量 PI 的值近似为： {!r}。'.format(math.pi))
常量 PI 的值近似为： 3.141592653589793。
```





| r    | 以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。 |
| ---- | ------------------------------------------------------------ |
| rb   | 以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。 |
| r+   | 打开一个文件用于读写。文件指针将会放在文件的开头。           |
| rb+  | 以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。 |
| w    | 打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。 |
| wb   | 以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。 |
| w+   | 打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。 |
| wb+  | 以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。 |
| a    | 打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。 |
| ab   | 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。 |
| a+   | 打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。 |
| ab+  | 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。 |

[![img](https://camo.githubusercontent.com/c7563c879f6f85107c9efce0b2ed0cccccea2f22/687474703a2f2f7777772e72756e6f6f622e636f6d2f77702d636f6e74656e742f75706c6f6164732f323031332f31312f323131323230352d383631633035623262646263396332382e706e67)](https://camo.githubusercontent.com/c7563c879f6f85107c9efce0b2ed0cccccea2f22/687474703a2f2f7777772e72756e6f6f622e636f6d2f77702d636f6e74656e742f75706c6f6164732f323031332f31312f323131323230352d383631633035623262646263396332382e706e67)

| 模式       | r    | r+   | w    | w+   | a    | a+   |
| ---------- | ---- | ---- | ---- | ---- | ---- | ---- |
| 读         | +    | +    |      | +    |      | +    |
| 写         |      | +    | +    | +    | +    | +    |
| 创建       |      |      | +    | +    | +    | +    |
| 覆盖       |      |      | +    | +    |      |      |
| 指针在开始 | +    | +    | +    | +    |      |      |
| 指针在结尾 |      |      |      |      | +    | +    |

#### 11、pickle 模块

python的pickle模块实现了基本的数据序列和反序列化。

通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储。

通过pickle模块的反序列化操作，我们能够从文件中创建上一次程序保存的对象。

基本接口：

```
pickle.dump(obj, file, [,protocol])
```

有了 pickle 这个对象, 就能对 file 以读取的形式打开:

```
x = pickle.load(file)
```

**注解：**从 file 中读取一个字符串，并将它重构为原来的python对象。

**file:** 类文件对象，有read()和readline()接口。

实例1：

```
#!/usr/bin/python3
import pickle

# 使用pickle模块将数据对象保存到文件
data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}

selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)

output = open('data.pkl', 'wb')

# Pickle dictionary using protocol 0.
pickle.dump(data1, output)

# Pickle the list using the highest protocol available.
pickle.dump(selfref_list, output, -1)

output.close()
```

实例2：

```
#!/usr/bin/python3
import pprint, pickle

#使用pickle模块从文件中重构python对象
pkl_file = open('data.pkl', 'rb')

data1 = pickle.load(pkl_file)
pprint.pprint(data1)

data2 = pickle.load(pkl_file)
pprint.pprint(data2)

pkl_file.close()
```



### 5.类







### 6. 程序打包

安装 setuptools 模块，使用pip install

导入 setup

from setuptools import setup

setup(

name='hello',

version='1.1',

description='demo',

py_modules=['hello'])

将该程序存储为setup.py，且其所在目录下包含 hello.py

创建exe文件，导入py2exe这个模块

创建macos 文件，导入py2app模块



### 7.  新闻汇总项目

NNTP协议

from nntplib import NNTP

server= NNTP('URL')

NNTP对象的方法(server)

| 方法                         | 描述                                                         |
| ---------------------------- | ------------------------------------------------------------ |
| group(name)                  | 选择一个组的名字，返回一个元组（rsp，ct，fst，lst，group）：服务器的返回信息文章的数量、第一个和最后一个文章的号码以及组名，所有数据都是字符串（返回的group与我们传进去的那么应该是相同的） |
| xhdr(hdr,artrg,     [ofile]) | 返回文章范围artrg（“头-尾”的格式）内文章hdr头的列表，或输出到文件ofile中 |
| body(id[,ofile])             | 给定文章的id，id可以是消息的ID（放在尖括号里），或一个文章号（是一个字符串），返回一个元祖（rsp，anum，mid，data）：服务器的返回信息、文章号（是一个字符串）、消息的ID（放在尖括号里）和文章所有行的列表或把数据输出到文件ofile中 |
| head(id)                     | 与body()相似，只是返回的元祖中那个行的列表中只包含了文章的标题 |
| article(id)                  | 也跟body()一样，只是返回的元祖中哪个行的列表中包含了文章的标题和内容 |
| stat(id)                     | 让文章的“指针”指向id（同上，是一个消息的ID或是文章的号码）。返回一个跟body一样的元祖（rsp，anum，mid），但不包含文章的数据 |
| next()                       | 用法和stat()类似，把文章指针移到下一篇文章，返回与stat()相似的元祖 |
| last()                       | 用法和stat()类似，把文章指针转移到最后一篇文章，返回与stat()相似的元祖 |
| post(ufile)                  | 上传ufile文件对象里的内容（使用ufile.readlines()），并在当前新闻组发表 |
| quit()                       | 关闭连接，然后退出。                                         |



## 8. 机器学习与深度学习

机器学习

参考链接：

https://baijiahao.baidu.com/s?id=1606694239390920783&wfr=spider&for=pc

https://laboo.top/2018/11/21/tfjs-dr/

* 无监督学习
  * 聚类
* 有监督学习

回归

分类

机器学习： 管理员提取事物的特征=>训练模型



## 9. 数据挖掘（爬虫）

爬虫集锦：https://github.com/facert/awesome-spider