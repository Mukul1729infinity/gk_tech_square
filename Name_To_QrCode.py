import pyqrcode
import datetime
now = datetime.datetime.now()
name=input('Enter Your Name')
k=pyqrcode.create(name)
k.png("test.png",scale=10)
import os
os.system('test.png')
print("Your QR CODE IS READY of " + "Name: " + name+",Powered By INFINITY1729 "+ "Date:"+now.strftime("%Y-%m-%d %H:%M:%S"))
