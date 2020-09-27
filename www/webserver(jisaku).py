import socket
import signal

signal.signal(signal.SIGINT,signal.SIG_DFL)

MY_ADDRESS = ""
MY_PORT = 50000 #サーバーがlistenしているぽーと
BUFSIZE = 1024

# HTTP Request の中身
statusline = "HTTP/1.1 200 OK\r\n"
blank_line = "\r\n"
contents = "いいよ～"

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.bind((MY_ADDRESS, MY_PORT))

sock.listen()


#ここはまだ途中##############3
req = "" #初期化
while req.find("\r\n")<0:
    data = sock_c.recv(BUFSIZE)
    if not data:
        break
    req += sock_c.recv(BUFSIZE).decode("UTF-8")
i_CRLF = req.find("\r\n")
if i_CRLF < 0:
    print("No Request Line")#ここは適当にCRLFがなかったことがわかるように
else:
    req_l = req[:i_CRLF]
#####################





while True:
    sock_c, addr = sock.accept()

    req = sock_c.recv(BUFSIZE)
    print(req.decode("UTF-8"))

    try:
        # HTTP Request を送信
        sock_c.sendall(statusline.encode("UTF-8"))
        sock_c.sendall(blank_line.encode("UTF-8"))
        sock_c.sendall(contents.encode("UTF-8"))
    except:
        print("failed to sendall()")
    sock_c.close()

sock.close()
