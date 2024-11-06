# 繰り返し処理 - for命令


# for命令
'''
for 仮引数 in リスト:
    個々の要素に対する処理
'''
# 仮引数 : 一時的にリストの要素を格納するための変数

# リストの要素を出力
data = ['うめ', 'さくら', 'もも']
for value in data:
    print(value)

# 文字ごとに出力
data = 'こんにちは、赤ちゃん'
for value in data:
    print(value)


# range関数の活用
'''
始点から終点までの値を生成
range(第1引数, 第2引数, 第3引数)
第1引数 : 始点
第2引数 : 終点
第3引数 : 増分
'''
# 1から5まで
for i in range(1, 6):
    print(i, '番目のループです。')

# 0からnまで（9は含まれない）
for i in range(0, 10):
    print(i)

# 1飛ばし（10は含まれない）
for i in range(0, 10, 2):
    print(i)

# 逆順（0は含まれない）
for i in range(5, 0, -1):
    print(i)

# rangeのリスト化（普段はrange型なのでリストとして表すにはlist()が必要）
print(list(range(0, 7, 2)))