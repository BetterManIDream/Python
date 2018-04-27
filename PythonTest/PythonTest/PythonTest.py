#温度转换
'''val=input("请输入带有符号的温度值(32C):")
if(val[-1] in ['c','C']):
    f=1.8*float(val[0:-1])+32
    print("转换后的温度是:%.2fF"%f)
elif val[-1] in ['f','F']:
    c=(float(val[0:-1])-32)/1.8
    print("转换后的温度是:%.2fC"%c)
else:
    print("输入有误！")'''

#绘制蟒蛇移动
'''import turtle

def drawSnake(rad,angle,len,neckrad):
    for i in range (len):
        turtle.circle(rad,angle)
        turtle.circle(-rad,angle)
    turtle.circle(rad,angle/2)
    turtle.config_dict(rad)
    turtle.circle(neckrad+1,180)
    turtle.config_dict(rad*2/3)
def main():
    turtle.setup(1200,800,0,0)
    pythonsize=30
    turtle.pensize(pythonsize)
    turtle.pencolor("blue")  #  turtle.pencolor("#3B9909")  
    turtle.seth(-40)
    drawSnake(40,80,5,pythonsize/2)

main()'''

#递归
'''def fact(n):  
    if n==0:
        return 1
    else:
       return fact(n-1)*n       
print(fact(989))'''

'''def reverse(s):
    if s=='':
        return s
    else:
        return reverse(s[1:])+s[0]
print(reverse("lfssnh"))'''

#绘制五角星
'''from turtle import Turtle

p=Turtle()
p.speed(1)
p.pensize(2)
p.color("red","red")
p.begin_fill()
p.right(180)
p.forward(100)
p.right(180)
for i in range(5):
    p.forward(200)
    p.right(144)
p.end_fill()'''

#打印当前用户以及IP地址
'''import socket

host_name=socket.gethostname()
print("Host Name:",host_name,"\nIP Adress:",socket.gethostbyname(host_name))'''

#获取IP地址
'''import socket

def get_remote_machine_info():
    remote_host='www.jd.com'
    try:
        print("IP Adress:",socket.gethostbyname(remote_host))
    except socket.error:
        print(socket.error)

get_remote_machine_info()'''

#线程测试
'''import threading

def do_this(what):
    whoami(what)

def whoami(what):
    print("Thread %s says: %s" % (threading.current_thread(),what))
  
if __name__ == "__main__":
    whoami("I'm mian program!")
    for n in range(4):
        p=threading.Thread(target=do_this,args=("I'm function %s"% n, ))
        p.start()'''

#TCP Server
'''from datetime import datetime
import socket
address = ('0.0.0.0', 60001)

max_size = 1000
print('Starting the server at', datetime.now())
print('Waiting for a client to connect....')
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(address)
server.listen(5)
client, addr = server.accept()
data = client.recv(max_size)

print('Start the server at',datetime.now())
print('Waiting for a client to connect...')
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(address)
server.listen(5)

print(datetime.now(),'', client.getsockname(), 'said:', data)
client.sendall(b'Are you talking to me?')
client.close()
server.close()'''

#TCP Client
'''from datetime import datetime 
from socket import*

address=('192.168.1.220',60001)

client=socket(AF_INET, SOCK_STREAM)
client.connect(address)
client.sendall(b'Hello Sever!')
data = client.recv(1024)
print(datetime.now(),':',data,'exit!')
client.close()'''

#多线程TCP Server
'''from datetime import datetime
from socket import *
from os import *
from threading import Thread

def Threader(sock):
    while True:
        cmd=sock.recv(1024)
        if cmd=='exit':
            sock.close()
            exit()
        sock.send(cmd)
        print(datetime.now(),':',cmd)

s=socket(AF_INET,SOCK_STREAM)
s.bind(('0.0.0.0',60001))
s.listen(1)
print('Server start at',datetime.now())
while True:
    sock,addr=s.accept()
    print('Client',addr,'connect')
    t=Thread(target=Threader,args=(sock,))
    t.start()'''


#多线程Client 实现输入/打印
import sys  
from socket import*
from threading import Thread

def Receive(sock):
    while True:
        data = sock.recv(1024)
        if data=='exit':
           sock.close()
           exit()
        print('Client Receive:',data)

def Input(sock):
    while True:
        data=input()
        if data == 'exit':
            break
        sock.sendall(data.encode())
        print('Client Send:',data) 

address = ('192.168.1.220',60001)
sock=socket(AF_INET,SOCK_STREAM)
sock.connect(address)

s=Thread(target=Receive,args=(sock,))
t=Thread(target=Input,args=(sock,))
s.start()
t.start()

   


