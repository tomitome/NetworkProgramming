import socket
import signal

signal.signal(signal.SIGINT,signal.SIG_DFL)

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(("",50000))
sock.listen()

while True:
    sock_c, addr = sock.accept()
    msg = "4421"
    try:
        sock_c.sendall(msg.encode("UTF-8"))
    except:
        print("sendall function failed.")
    sock_c.close()

sock.close()