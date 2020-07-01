import socket
hostname=socket.gethostname()
IPadd=socket.gethostbyname(hostname)
print("my Current Ip:",IPadd)
