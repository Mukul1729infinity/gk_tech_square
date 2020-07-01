import youtube_dl,os
yd={}
path='PATH TO SAVE VEDIO' # E:/youtube
os.chdir(path)
url='---ENTER VEDIO URL HERE---'
with youtube_dl.YoutubeDL(yd) as y:
    print("start Downloading")
    y.download([url])
print("vedio Download")
