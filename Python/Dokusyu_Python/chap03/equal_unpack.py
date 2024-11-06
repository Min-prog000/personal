# アンパック代入

# 要素数だけ左辺に変数を用意する
data = [1, 2, 3, 4, 5]
a, b, c, d, e = data
print(a)
print(b)
print(c)
print(d)
print(e)


# *変数 : 残りの要素をまとめて代入
data = [1, 2, 3, 4, 5]
m, n, *o = data
print(m)
print(n)
print(o)

r, *s, t = data
print(r)
print(s)
print(t)

*x, y, z = data
print(x)
print(y)
print(z)

# 要素数より多いとき'*'つきの変数は空リスト
data = [1, 2]
a, b, *c = data
print(a)
print(b)
print(c)


# _ : 切り捨て
data = [1, 2, 3, 4, 5]
a, _, b, _, c = data
print(a)
print(b)
print(c)
print(_)    # 変数名が'_'なだけで値はある

# *_も可能
x, *_, y = data
print(x)
print(_)
print(y)


# 入れ子リスト
data = [1, 2, [31, 32, 33]]
a, b, c = data
print(a)
print(b)
print(c)

# 入れ子リストの要素は()で変数をくくって取り出す
x, y, (z1, z2, z3) = data
print(x)
print(y)
print(z1)
print(z2)
print(z3)


# スワッピング（値交換）
# cだともう一つ変数が必要
x = 15
y = 38
x, y = y, x
print(x, y)