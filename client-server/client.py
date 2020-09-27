import socket
import signal
signal.signal(signal.SIGINT,signal.SIG_DFL)

HOST = "127.0.0.1"
PORT = 50000 #サーバーがlistenしているぽーと
BUFSIZE = 256

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.connect((HOST,PORT))

data = sock.recv(BUFSIZE)
print(data.decode("UTF-8"))

msg = input("message:")
try:
    sock.sendall(msg.encode("UTF-8"))
except:
    print("sendall function failed")

sock.close()