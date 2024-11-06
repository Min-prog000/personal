# 条件分岐


# if命令（多岐分岐）
'''
if 条件式1:
    条件式1がTrueのときに実行する処理
elif 条件式2:
    条件式2がFalseのときに実行する処理
else:
    条件式1, 2がどちらもFalseのときに実行する処理
'''

# 最初にTrueになった条件式の処理を実行する
# i > 50が先の場合
i = 100
if i > 50:
    print('変数iは50より大きいです。')
elif i > 30:
    print('変数iは30より大きいです。')
else:
    print('変数iは30以下です。')

# i > 30が先の場合
if i > 30:
    print('変数iは30より大きいです。')
elif i > 50:
    print('変数iは50より大きいです。')
else:
    print('変数iは30以下です。')


# switch（pythonにはないので他の文で代用する）
# 1. if...elif...else
rank = '甲'
if rank == '甲':
    print('大変よいです。')
elif rank == '乙':
    print('よいです。')
elif rank == '丙':
    print('がんばりましょう。')
else:
    print('？？？')

# 2. 辞書型
rank = '甲'
# rankに文章を対応させる
msg = {
    '甲': '大変よいです。',
    '乙': 'よいです。',
    '丙': 'がんばりましょう。'
}
# rankとmsgのキーを照らし合わせる
if rank in msg:
    print(msg[rank])
else:
    print('？？？')