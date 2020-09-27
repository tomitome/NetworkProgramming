import socket
import signal
# キーボードのctl+cを使えるようにするため
signal.signal(signal.SIGINT,signal.SIG_DFL)
# ソケットの作成（指定して作られたソケットオブジェクトをsockに代入）
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 接続のための準備（マジックナンバーにならないように変数で宣言）
HOST = "127.0.0.1"   # 接続先（自分自身だけど）
PORT = 50000     # サーバーがlistenしているぽーと
# 接続開始
sock.connect((HOST,PORT))

# マジックナンバーを避ける
#BUFSIZE = 256
# 受信したデータを代入
#data = sock.recv(BUFSIZE)
# 受信したデータをデコードして出力
#print(data.decode("UTF-8"))


SIZE = 2048
rule = sock.recv(SIZE)
print(rule.decode("UTF-8", errors="ignore"))

#data = sock.recv(BUFSIZE)
#print(data.decode("UTF-8", errors="ignore"))


while True:
    godhand= input("出す手:")
    try:
        sock.sendall(godhand.encode("UTF-8"))
    except:
        print("sendall function failed")
    kekka = sock.recv(SIZE)
    print(kekka.decode("UTF-8", errors="ignore"))
    if godhand == "3" :
        break
#ソケットを閉じて通信終了
sock.close()