# 代入演算子

# = : 代入
data = 1
data2 = 1
# += : 加算
data += 1
# -= : 減算
data -= 1
# *= : 乗算
data *= 2
# /= : 除算
data /= 2
# //= : 除算（切り捨て）
data //= 2
# %= : 剰余
data2 %= 2
# **= : べき乗
data2 **= 2
# & : 論理積
data2 &= 2
# ^= : 排他的論理和
data2 ^= 2
# |= : 論理和
data2 |= 2
# >>= : 右シフト
data2 >>= 2
# <<= : 左シフト
data2 <<= 2

print(data)
print(data2)

num1 = 10
num2 = num1
print(id(num1))
print(id(num2))