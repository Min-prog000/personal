# 繰り返し処理 - for - リスト内包表記


# リスト内包表記
'''
data = [式 for 仮引数 in リスト]
リストの各要素に対して処理をしたあと、dataに要素として格納
'''
data = [15, 43, 7, 59, 98]
data2 = [i * 2 for i in data]
print(data2)

# 内包表記を使わない場合
data = [15, 43, 7, 59, 98]
data2 = []
for i in data:
    data2.append(i * 2)
print(data2)

# 内包表記に条件をつける
data = [15, 43, 7, 59, 98]
data2 = sum([i for i in data if i < 50])
print(data2)