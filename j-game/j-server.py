import socket
import signal

signal.signal(signal.SIGINT,signal.SIG_DFL)

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(("",50000))
sock.listen()
sock.connect((HOST,PORT))

while True:
    sock_c, addr = sock.accept()

    r = "■■■■■■■■■■\n"\
        "北九州工業高等専門学校　生産デザイン工学科　情報システムコース\n"\
        "4年通年科目「ネットワークプログラミング」課題用プログラム　ver.2020-1。\n"\
        "■■■■■■■■■■\n\n"\
        "■　ゲームの概要\n"\
        "　このゲームは0～2のうち一つの数字を互いに出して勝敗を決めるゲームだよ。\n"\
        "■　数字の対応\n"\
        "　0->やせ我慢　　1->愛情　　2->小切手　　3->ゲーム終了\n"\
        "■　強い/弱いの規則\n"\
        "「やせ我慢」をしているヤンキーも「愛情」を見せられると弱さを見せちゃうんだ。\n"\
        "→「やせ我慢」より「愛情」が強い\n"\
        "でも「愛情」も「小切手」を見せられると心が揺らいじゃうよ。\n"\
        "→「愛情」より「小切手」が強い\n"\
        "ただ、「小切手」を見せられたとしても「やせ我慢」で耐えられるんだ。\n"\
        "→「小切手」より「やせ我慢」が強い\n\n"\
        "■　クライアント作成のポイント\n"\
        "1. サーバに接続\n"\
        "2. ルールを受信して表示\n"\
        "3.キーボードから入力した0～2の数字のどれかを送る\n"\
        "4.サーバ側で計算された勝負結果が送られてくる\n"\
        "（以後、勝負の繰り返し）\n"\
        "※「3」を送るとゲーム終了となり、最終成績が送られてくる\n\n"\
        "ちなみに「3」を送るまではずっとゲームが続く神仕様だよ！\n"

    try:
            sock_c.sendall(r.encode("UTF-8"))
        except:
            print("sendall function failed.")

    BUFSIZE = 256

    while True:
        a += 1
        
        date = sock.recv(BUFSIZE)
        print(date.decode("UTF-8"))
        if data == "0" :




    try:
        sock_c.sendall(msg.encode("UTF-8"))
    except:
        print("sendall function failed.")
    sock_c.close()