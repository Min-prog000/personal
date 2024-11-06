# 算術演算子
# + :加算
print(2 + 3)
# - :減算
print(5 - 2)
# * :乗算
print(2 * 4)
# ** :べき乗
print(2 ** 3)
# / :除算
print(7 / 3)
# // :除算（切り捨て）
print(7 // 3)
# % :剰余
print(10 % 3)


# 文字列同士
# + :連結
print('10' + '3')
print('こんにちは、' + 'あかちゃん')
# * :繰り返し
print('こんにちは' * 3)


# 文字列と数値
# print(15 + '30')  error
# 整数型に合わせる
print(15 + int('30'))
# 文字列型に合わせる
print(str(15) + '30')


# 除算
# divmod :商と剰余を返す
print(divmod(5, 3))


# 浮動小数点数における誤差
# 小数は誤差が出てくる（2進数変換後循環するから）
print(0.2 * 3)          # 0.6000000000000001
print(0.2 * 3 == 0.6)   # False

# decimal :誤差なしで小数を表現（引数は文字列型）
import decimal

d1 = decimal.Decimal('0.2')
d2 = decimal.Decimal('3')
d3 = decimal.Decimal('0.6')

print(d1 * d2)
print(d1 * d2 == d3)