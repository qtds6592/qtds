        
def getList(ll):
    re=[]
    aa=0;
    for m in ll:
        re.append(aa+m)
        aa=m
    re.append(1)
    return re
def fib():
    l=[]
    while True:
        l = getList(l)
        yield l
    
    
    
g = fib()
def get():
    return next(g)
for b in fib():
    n = n + 1
    print(b)
    if n == 10:
        break
    
for n in list(range(0,10)):
    x = next(g)
    print(x)
----------
利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
def normalize(name):
    print(name)
    s1 = name[0:1].upper()
    print(s1)
    s2 = name[1:len(name)] .lower()
    print(s2)
    return s1+s2
        
    return 
# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
======
Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
# -*- coding: utf-8 -*-

from functools import reduce

def prod(L):
    return reduce(lambda x, y: x * y, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

=======
def not_empty(s):
    return s and s.strip()

list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))
# 结果: ['A', 'B', 'C']
=======
回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()滤掉非回数：

# -*- coding: utf-8 -*-

def is_palindrome(num):
    #print('num:',num)
    a = str(num)
    c=0
    n=0
    for b in a:
        # print('b',b)
        c = 10**(n)*int(b)+c
        # print('c',c)
        n = n + 1 
    c2 = int(c)
    # print('c2',c2)
    return num == c2

        
# 测试:
output = filter(is_palindrome, range(1000, 100000))
print(list(output))
======

from operator import itemgetter

L = ['bob', 'about', 'Zoo', 'Credit']

print(sorted(L))
print(sorted(L, key=str.lower))

students = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

print(sorted(students, key=itemgetter(0)))
print(sorted(students, key=lambda t: t[1]))
print(sorted(students, key=itemgetter(1), reverse=True))
=======
请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志
@log
def f():
    print('aaaaaa')

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        func(*args, **kw)
        print('end %s():' % func.__name__)
    return wrapper

@log('nnnn')
def f():
    print('aaaaaa')

def log(test):
    def aaa(fun):
        @functools.wraps(fun)
        def wrapper(*args, **kw):
            print('call %s():%s' % (fun.__name__,test))
            fun(*args, **kw)
            print('end %s():%s' % (fun.__name__,test))
        return wrapper
    return aaa
    -----------------------------
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def print_score(self):
        print('%s: %s' % (self.name, self.score))
    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))
    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
        
==============
请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：

# -*- coding: utf-8 -*-

class Screen(object):
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, value):
        self.__width = value
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, value):
        self.__height = value
    @property
    def resolution(self):
        return self.__height * self.__width
# test:
s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution

=====

def bar():
    try:
        print('11')
        raise ValueError('invalid value: %s' % 1)
        print('22')
    except ValueError as e:
        print('ValueError!')
    print('33')
    
========
/Users/yang/Documents/Pytest/src/mydict.py
import os

# 查看当前目录的绝对路径:
>>> os.path.abspath('.')
'/Users/michael'
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
>>> os.path.join('/Users/michael', 'testdir')
'/Users/michael/testdir'
# 然后创建一个目录:
>>> os.mkdir('/Users/michael/testdir')
# 删掉一个目录:
>>> os.rmdir('/Users/michael/testdir')

os.path.join()
>>> os.path.split('/Users/michael/testdir/file.txt')
('/Users/michael/testdir', 'file.txt')
>>> os.path.splitext('/path/to/file.txt')
('/path/to/file', '.txt')
# 对文件重命名:
>>> os.rename('test.txt', 'test.py')
# 删掉文件:
>>> os.remove('test.py')

>>> [x for x in os.listdir('.') if os.path.isdir(x)]
['.lein', '.local', '.m2', '.npm', '.ssh', '.Trash', '.vim', 'Applications', 'Desktop', ...]
要列出所有的.py文件，也只需一行代码：

>>> [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
['apis.py', 'config.py', 'models.py', 'pymonitor.py', 'test_db.py', 'urls.py', 'wsgiapp.py']
-----------------
>>> f = open('dump.txt', 'wb')
>>> pickle.dump(d, f)
>>> f.close()
>>> f = open('dump.txt', 'rb')
>>> d = pickle.load(f)
>>> f.close()
>>> d

import json

d = dict(name='Bob', age=20, score=88)
data = json.dumps(d)
print('JSON Data is a str:', data)
reborn = json.loads(data)
print(reborn)

class Student(object):

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return 'Student object (%s, %s, %s)' % (self.name, self.age, self.score)

s = Student('Bob', 20, 88)
std_data = json.dumps(s, default=lambda obj: obj.__dict__)
print('Dump Student:', std_data)
rebuild = json.loads(std_data, object_hook=lambda d: Student(d['name'], d['age'], d['score']))
print(rebuild)

-------------------------
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))
    
if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
    
-----
from multiprocessing import Process, Queue
import os, time, random

# 写数据进程执行的代码:
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

# 读数据进程执行的代码:
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()
======
import time, threading

# 新线程执行的代码:
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)

==============

import time, threading
balance = 0
lock = threading.Lock()
def run_thread(n):
    for i in range(100000):
        # 先要获取锁:
        lock.acquire()
        try:
            # 放心地改吧:
            change_it(n)
        finally:
            # 改完了一定要释放锁:
            lock.release()
t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
===============

import threading

# 创建全局ThreadLocal对象:
local_school = threading.local()

def process_student():
    # 获取当前线程关联的student:
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()

t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
===========
假设你获取了用户输入的日期和时间如2015-1-21 9:01:30，以及一个时区信息如UTC+5:00，均是str，请编写一个函数将其转换为timestamp：

# -*- coding:utf-8 -*-

import re
from datetime import datetime, timezone, timedelta

def to_timestamp(dt_str, tz_str):
    cday = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    num = int(re.match(r'^UTC([+|-]\d{1,2}):00$',tz_str).group(1))
    end = cday.replace(tzinfo=timezone(timedelta(hours=num)))
    return end.timestamp()

# 测试:

t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('Pass')
=======
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print('Point:', p.x, p.y)

from collections import deque

q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)

from collections import defaultdict

dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print('dd[\'key1\'] =', dd['key1'])
print('dd[\'key2\'] =', dd['key2'])

from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)

================

根据用户输入的口令，计算出存储在数据库中的MD5口令：
import hashlib
def calc_md5(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    print(md5.hexdigest())
    
设计一个验证用户登录的函数，根据用户输入的口令是否正确，返回True或False：
d = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}

def login(user, password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    print(md5.hexdigest())
    print(d[user])
    if md5.hexdigest() == d[user]:
        return True
    else:
        return False
a = login('bob','aaa')

-------------------
根据用户输入的登录名和口令模拟用户注册，计算更安全的MD5：

db = {}
def get_md5(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    print(md5.hexdigest())
    return md5.hexdigest()
    
def register(username, password):
    db[username] = get_md5(password + username + 'the-Salt')
    
然后，根据修改后的MD5算法实现用户登录的验证：

def login(username, password):
    md5 = get_md5(password + username + 'the-Salt')
    print(md5)
    print(db[username])
    if md5 == db[username]:
        print('OK')
    else:
        print('NOT OK')
        
======
import itertools
itertools.count(1)
itertools.cycle('ABC')
itertools.repeat('A', 3)
itertools.chain('ABC', 'XYZ')

for key, group in itertools.groupby('AAABBBCCAAA')
for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):

class Query(object):
    def __init__(self, name):
        self.name = name
    def __enter__(self):
        print('Begin')
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print('Error')
        else:
            print('End')
    def query(self):
        print('Query info about %s...' % self.name)
with Query('Bob') as q:
    q.query()
    
    
-----
from contextlib import contextmanager

class Query(object):

    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)

@contextmanager
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q
    print('End')

很多时候，我们希望在某段代码执行前后自动执行特定代码，也可以用@contextmanager实现。例如：

@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)

with tag("h1"):
    print("hello")
    print("world")
代码的执行顺序是：

with语句首先执行yield之前的语句，因此打印出<h1>；
yield调用会执行with语句内部的所有语句，因此打印出hello和world；
最后执行yield之后的语句，打印出</h1>。

如果一个对象没有实现上下文，我们就不能把它用于with语句。这个时候，可以用closing()来把该对象变为上下文对象。例如，用with语句使用urlopen()：

from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)
closing也是一个经过@contextmanager装饰的generator，这个generator编写起来其实非常简单：

@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()
==============

from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))
    def end_element(self, name):
        print('sax:end_element: %s' % name)
    def char_data(self, text):
        print('sax:char_data: %s' % text)
==========

from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()
    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message', 'Hello, %s' % name)

app = Application()
# 设置窗口标题:
app.master.title('Hello World')
# 主消息循环:
app.mainloop()

===========
TCP
import socket, threading, time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 监听端口:
s.bind(('127.0.0.1', 9999))
s.listen(5)
print('Waiting for connection...')

def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)

while True:
    # 接受一个新连接:
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
    
    
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('127.0.0.1', 9999))
# 接收欢迎消息:
print(s.recv(1024).decode('utf-8'))
for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()
----
UPD

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定端口:
s.bind(('127.0.0.1', 9999))

print('Bind UDP on 9999...')

while True:
    # 接收数据:
    data, addr = s.recvfrom(1024)
    print('Received from %s:%s.' % addr)
    reply = 'Hello, %s!' % data.decode('utf-8')
    s.sendto(reply.encode('utf-8'), addr)
    

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据:
    s.sendto(data, ('127.0.0.1', 9999))
    # 接收数据:
    print(s.recv(1024).decode('utf-8'))

s.close()
========

请编写函数，在Sqlite中根据分数段查找指定的名字：
import os, sqlite3

db_file = os.path.join('', 'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)

# 初始数据:
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
cursor.close()
conn.commit()
conn.close()

def get_score_in(low, high):
    ' 返回指定分数区间的名字，按分数从低到高排序 '
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        cursor.execute('select name from user where score >= ? and  score <=  ? order by score asc',(low, high))
        values = cursor.fetchall()
        print(values)
        l=[]
        for i in values:
            print(i[0])
            l.append(i[0])
        return l
    finally:
        cursor.close()
        conn.close()
# 测试:
assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)
====
from wsgiref.simple_server import make_server
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello, web!</h1>']

# 导入我们自己编写的application函数:
from hello import application

# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
httpd = make_server('', 8001, application)
print('Serving HTTP on port 8000...')
# 开始监听HTTP请求:
httpd.serve_forever()

====

# hello.py

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    print(environ['PATH_INFO'][1:])
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]

====

def consumer():
    r = ''
    n = 0
    while True:
        print('yield mae=',n)
        n = yield int(r) + 1
        print('yield ato=',n)
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        #r = '200 OK'

def produce(c):
    c.send(0)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)