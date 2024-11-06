# 数値セパレーター

value = 1_234_567
pi = 3.141_259_265_359
num = 0.123_456e10

# 10進数リテラル以外でも使用可能
a = 0b01_01_01
b = 0xf4_240
c = 0o23_420

# 数値プレフィックスの間では使えない
# '0b'の後
d = 0b_1011_0001
# '0b'の間 -> エラー
# e = 0_b_1011_0001

print(value)
print(pi)
print(num)
print(a)
print(b)
print(c)
print(d)