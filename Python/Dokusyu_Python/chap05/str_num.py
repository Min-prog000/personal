# 文字列操作 - 半角数値変換


# unicodedata.digit : 数値文字を半角整数に変換
# unicodedata.numeric : 数値文字を半角浮動小数点数に変換

import unicodedata

# 整数変換
print(unicodedata.digit('５'))

# 小数変換(漢数字, ローマ数字も変換可能)
print(unicodedata.numeric('Ⅹ'))
print(unicodedata.numeric('陸'))