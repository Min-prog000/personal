price = 100
# i.1：マジックナンバー（コーダーにしか意味が分からない数値）
print(price * 1.1)

price = 100
# 定数であることを大文字の変数で表す
TAX_RATE = 1.1
print(price * TAX_RATE)

# 補足
# 誤差を無くす（Decimal）

from decimal import Decimal
print(price * Decimal('1.1'))