# 比較演算子

# 主な比較演算子
# < : 左辺が右辺より小さいときTrue
print(5 < 10)
# > : 左辺が右辺より大きいときTrue
print(5 > 10)
# == : 左辺と右辺が等しいかときTrue
print(5 == 5)
# <= : 左辺が右辺以下のときTrue
print(5 <= 10)
# >= : 左辺が右辺以上のときTrue
print(5 >= 10)
# != : 左辺が右辺と等しくないときTrue
print(5 != 10)
# is : 左辺と右辺のオブジェクトが等しいときTrue
print([1, 2] is [1, 2])
a = [1, 2]
b = a
print(a is b)       # True
print(a is [1, 2])  # False
print(b is [1, 2])  # False
a[0] = 2
print(a is [2, 2])  # False
print(a is b)       # True
print(a is a)       # True
print(b is b)       # True
# is not : 左辺と右辺のオブジェクトが等しくないときTrue
print([1, 2] is not [1, 2])
# in : 左辺が右辺に含まれているときTrue
print(3 in [1, 2, 3])
# not in : 左辺に右辺が含まれていないときTrue
print(4 not in [1, 2, 3])