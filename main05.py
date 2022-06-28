#Pythonのお勉強
#引用元：http://python.rdy.jp/wiki.cgi?page=%CC%E4%C2%EA%BD%B8#p2

#問題集【Simple】

#10000以下の素数を表示する

# 怠惰な方法
for i in range(2, 10000):
    if 0 not in [i % j for j in range(2, (i / 2 + 1))]:

#line 10, in <module> range(2, i / 2 + 1)]: be interpreted as an integerのエラー出る
#range(start, stop, step)においてstopの値をfloat型にしているためTypeErrorが発生
#stopの数値をint型、つまり整数の数値を代入することでTypeErrorを解決することができる

        print (i)
