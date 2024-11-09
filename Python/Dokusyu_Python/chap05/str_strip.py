# 文字列操作 - 空白除去


# strip : 文字列前後の対象文字列をすべて除去(内部は除去されない)
# lstrip : 文字列先頭の対象文字列を除去
# rstrip : 文字列後方の対象文字列を除去

'''
str.strip(chars)
str.lstrip(chars)
str.rstrip(chars)

str : 文字列
chars : 対象文字列(規定は空白)
'''

# 空白 : 半角空白, 全角空白, タブ文字(\t, \v), 改行文字(\n, \r), フォームフィード(\f)

# e.g.
# msg = '_＿こんにちは_\t\n\r' (_は半角空白, ＿は全角空白)
msg = ' 　こんにちは \t\n\r'
# 前後から除去
print('「' + msg.strip() + '」')
# 前方から除去
print('「' + msg.lstrip() + '」')
# 後方から除去
print('「' + msg.rstrip() + '」')

# 特定文字の除去
msg2 = '!======［Hello, World］======!'
# msg2から'!', '=', '［', '］'を除去
print('「' + msg2.strip('!=［］') + '」')


# replace : 文字列全体からの除去
msg = '  こ ん に ち は  '
print(msg.replace(' ', ''))