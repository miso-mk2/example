import time

def kansu():
    timer1 = time.time()

    hoge = input("何か入力=")
    print(hoge)

    timer2 = time.time()
    return  timer2 - timer1 

print(kansu())

"timeモジュールの時計を開始時と終了時で比較して、関数の実行にかかった時間を確認する"