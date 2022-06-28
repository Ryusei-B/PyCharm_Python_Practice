#Pythonのお勉強
#引用元：http://python.rdy.jp/wiki.cgi?page=%CC%E4%C2%EA%BD%B8#p2

#問題集【Simple】

#10000以下の素数を表示する

# 少しちゃんとした方法

from math import sqrt
for i in range(2,10000):
    if 0 not in [i%j for j in range(2, int(sqrt(i))+1)]:
        print (i)