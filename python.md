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

			   2：控件.bind("事件名"，函数名) 

布局管理器：控件.pack（）这样控件才能显示



## 3. 网络编程

网络编程里的一个基础组件:套接字(socket) ，提供了两个方法（send，recv） 用来发送与接收，socket.gethostname ：获取当前主机名

模块：urllib1与urllib2

urllib2.request()  与urllib2.urlopen()



获取远程文件：urlretrieve(“url”,"副本文件地址") 获取网页内容，存在副本文件中



## 4. 面向web

读取本地文件用 open()

读取网络文件  引入 urllib.request   ，使用urlopen()

     import urllib.request  

urllib.request.urlopen()

获取到文件或者网页之后，读取内容用 read()，解码用decode（），常用于中文解码

从英文意思上看，encode和decode分别指编码和解码。在python中，Unicode类型是作为编码的基础类型，即：

            decode                 encode
      str ---------> str(Unicode) ---------> str


### 4.1 re模块中常用功能函数

**正则模块 re**

**1、compile()**

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



str.format() 的基本使用如下:

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

![img](http://www.runoob.com/wp-content/uploads/2013/11/2112205-861c05b2bdbc9c28.png)

| 模式       | r    | r+   | w    | w+   | a    | a+   |
| ---------- | ---- | ---- | ---- | ---- | ---- | ---- |
| 读         | +    | +    |      | +    |      | +    |
| 写         |      | +    | +    | +    | +    | +    |
| 创建       |      |      | +    | +    | +    | +    |
| 覆盖       |      |      | +    | +    |      |      |
| 指针在开始 | +    | +    | +    | +    |      |      |
| 指针在结尾 |      |      |      |      | +    | +    |





## pickle 模块

python的pickle模块实现了基本的数据序列和反序列化。

通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储。

通过pickle模块的反序列化操作，我们能够从文件中创建上一次程序保存的对象。

基本接口：

```python
pickle.dump(obj, file, [,protocol])
```

有了 pickle 这个对象, 就能对 file 以读取的形式打开:

```python
x = pickle.load(file)
```

**注解：**从 file 中读取一个字符串，并将它重构为原来的python对象。

**file:** 类文件对象，有read()和readline()接口。

实例1：

```python
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

```python
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