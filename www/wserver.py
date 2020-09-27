import socket
import signal

# キーボードからの[ctrl]+[c]を非同期で受付
signal.signal(signal.SIGINT, signal.SIG_DFL)

# 待受に使うIPアドレスとポート番号
MY_ADDRESS = ""
MY_PORT = 50000
# 受信用バッファサイズ
BUFSIZE = 1024



def get_request(sock_c):
    req=""

    while req.find("\r\n")<0:
        data = sock_c.recv(BUFSIZE)
        if not data:
            break
        req += data.decode("UTF-8")

        i_CRLF = req.find("\r\n")
        if i_CRLF < 0 :
            print("No Request Line")
            return (None,None,None)
        else:
            req_l = req[:i_CRLF]
            return (req_l,None,None)





# ソケットを作成
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 自分の情報をソケットに登録
sock.bind((MY_ADDRESS, MY_PORT))
# ソケットを待ち受け状態にする
sock.listen()

while True:
    # 接続要求→受理
    sock_c, addr = sock.accept()

    line, header, body = get_request(sock_c)

    print("request line: {}\n".format(line))
    print("request header: {}\n".format(header))
    print("request body: {}\n".format(body))

    sock_c.close()

    
# 待ち受け用ソケットを閉じる
sock.close()
