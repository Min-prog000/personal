# 浮動小数点型（float）

# 指数表現
# <仮数部>e<符号><指数部>
# <仮数部>*10の<符号><指数部>
data1 = 1.4142e10
data2 = 1.173205e-7
# eは大文字も可
data3 = 4.51E4

# 一般的には仮数部が0.で始まるように表す
# example: 17.32 -> 0.1732*(10**2)
data4 = 0.1732e2
# example: 506.3 -> 0.503*(10**3)
data5 = 0.503e3

# 先頭の0は省略可
data6 = .4271

print(data1)
print(data2)
print(data3)
print(data4)
print(data5)
print(data6)