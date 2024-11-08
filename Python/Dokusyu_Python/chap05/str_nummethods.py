# 文字列操作 - 数値系メソッドの違い


'''
isdigit
  True:
    半角数字, 上付き数字, 全角数字, バイト文字
  False:
    ローマ数字, 漢数字
    
isdecimal
  True:
    半角数字, 全角数字
  False:
    上付き数字, ローマ数字, 漢数字
  Error:
    バイト文字

isnumeric
  True:
    半角数字, 上付き数字, 全角数字, ローマ数字, 漢数字
  Error:
    バイト文字
'''

# 半角数字
num_han = '123'
# 上付き数字
num_up = '\u2078'
# 全角数字
num_zen = '５９'
# ローマ数字
num_roma = 'ⅩⅤ'
# 漢数字
num_kan = '二十五'
# バイト文字
num_byte = b'15'

# isdigit
# -> True
print(num_han.isdigit())
print(num_up.isdigit())
print(num_zen.isdigit())
print(num_byte.isdigit())
# -> False
print(num_roma.isdigit())
print(num_kan.isdigit())

# isdecimal
# -> True
print(num_han.isdecimal())
print(num_zen.isdecimal())
# -> False
print(num_up.isdecimal())
print(num_roma.isdecimal())
print(num_kan.isdecimal())
# Error
# print(num_byte.isdecimal())

# isnumeric
# -> True
print(num_han.isnumeric())
print(num_up.isnumeric())
print(num_zen.isnumeric())
print(num_roma.isnumeric())
print(num_kan.isnumeric())
# Error
# print(num_byte.isnumeric())