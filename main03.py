#Pythonのお勉強
#引用元：http://python.rdy.jp/wiki.cgi?page=%CC%E4%C2%EA%BD%B8#p2

#問題集【Simple】

#2つの自然数の最大公約数を求める（ユークリッドの互除法）

#a,b = input(), input()

a,b=300,40

#再帰関数
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
print (gcd(a,b))