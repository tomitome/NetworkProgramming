import socket
import signal
import threading

signal.signal(signal.SIGINT,signal.SIG_DFL)

def commum(sock_c,addr):
    msg = 'unnti'
    try:
        sock_c.sendall(msg.encode("UTF-8"))
    except:
        print("sendall function failed.")
    date = sock.recv(BUFSIZE)
    print(date.decode("UTF-8"))

    sock_c.close()


MY_ADDRESS = ""
MY_PORT = 50000

BUFSIZE = 256

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.bind((MY_ADDRESS,MY_PORT))

sock.listen()

while True:
    sock_c, addr = sock.accept()
    # msg = "4421"
    # try:
    #     sock_c.sendall(msg.encode("UTF-8"))
    # except:
    #     print("sendall function failed.")
    # sock_c.close()
    p = threading.Thread(target=commum,args=(sock_c,addr))
    p.start()

sock.close()