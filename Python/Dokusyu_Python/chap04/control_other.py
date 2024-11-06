# ループの制御 - 制御方法のオプション


# breakしなかったときの処理
'''
for 仮引数 in リスト:
    ...処理...
    if 条件式:
        break
else:
    breakで終了しなかったときに実行する処理
'''

# elseが実行される場合
# data = ['さくら', 'うめ', 'ききょう', 'くちなし', 'ぼたん']

# elseが実行されない場合
data = ['さくら', 'うめ', '×', 'くちなし', 'ぼたん']

for name in data:
    # 要素が'×'のときにループ終了
    if name == '×':
        break
    print(name)
else:
    print('正常終了しました')


# 入れ子ループの中断・スキップ

# 入れ子の方だけbreakを実装した場合
# -> 外側のループは続く
for i in range(1, 10):
    for j in range(1, 10):
        result = i * j
        if result > 50:
            break
        print(result, end=' ')
    print()  # 改行

# 入れ子の外側にもbreakを実装した場合
# -> 外側のループも中止する
for i in range(1, 10):
    for j in range(1, 10):
        result = i * j
        if result > 50:
            break
        print(result, end=' ')
    else:
        print()
        continue
    print()
    break  # 内側のループでbreakが実行されたときに実行（外側のループも中止）

# フラグによる脱出
# 設定した変数を内側のbreak実行時に変更し外側のループのif文でさらにbreak実行
# -> 外側のループも中止する
flag = False
for i in range(1, 10):
    for j in range(1, 10):
        result = i * j
        if result > 50:
            flag = True
            break
        print(result, end=' ')
    print()
    # フラグがTrueなら外側のループからも抜け出す
    if flag:
        break