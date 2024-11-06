# 浮動小数点数の比較


# 2進数変換で丸め誤差が発生
print(0.2 * 3 == 0.6)   # False

# 対処法
# 1. Decimal型
import decimal
a = decimal.Decimal('0.2')
b = decimal.Decimal('3')
c = decimal.Decimal('0.6')
print(a * b == c)   # True

# 2. 丸め単位による比較
# EPSILON : 計算機イプシロン（丸め単位）
#           誤差の許容範囲（これ未満なら誤差として許される）
EPSILON = 0.00001
x = 0.2 * 3
y = 0.6
print(abs(x - y) < EPSILON) # True 小数点第5位までは等しい

# 3. isclose関数
# isclose : 小数点第9位までが許容範囲（範囲内ならTrue）
import math
print(math.isclose(0.2 * 3, 0.6))   # True

# rel_tol : 相対誤差
#           値の大きい方が基準（0扱い）となりその値からの差分未満が許容範囲
print(math.isclose(0.1, 0.1001, rel_tol=0.0001))    # False
print(math.isclose(0.1, 0.1001, rel_tol=0.001))     # True
# abs_tol : 絶対誤差
#           指定した桁数までが許容範囲
print(math.isclose(0.1, 0.1001, abs_tol=0.0001))    # True
print(math.isclose(0.1, 0.1001, abs_tol=0.00001))   # False