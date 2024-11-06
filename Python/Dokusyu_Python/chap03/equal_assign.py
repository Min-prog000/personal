# ミュータブルとイミュータブル

# ミュータブル
data1 = [1, 2, 3]
data2 = data1
data1[0] = 100
print(data1)
print(data2)    # 同じ場所

# イミュータブル
x = 1
y = x
print(id(x))
print(id(y))
x += 10
print(id(x))    # 場所が変わってる
print(id(y))
print(x)
print(y)

# データそのものを置き換えた場合
data1 = [1, 2 ,3]
data2 = data1
data1 = [4, 5, 6]
print(data1)    # [4, 5, 6]
print(data2)    # [1, 2, 3]