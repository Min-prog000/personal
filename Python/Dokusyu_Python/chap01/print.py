name = '山田'
print(name)

# 空白区切りで出力
print('Hello', name, 'さん!')

# sep(区切り文字指定)
print('Hello', name, 'さん!', sep='+')

# end(末尾文字指定。通常は改行)
print('こんにちは', end=' ')
print('こんにちは')

# sep, end同時使用
print('Hello', name, 'さん!', sep='+', end=' ')
print('ようこそ')