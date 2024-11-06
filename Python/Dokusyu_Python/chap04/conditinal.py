# 条件分岐


## 条件式を指定する場合の注意点


# 条件式が長いときは改行する
hoge = 100
foo = 200
piyo = 500
if (hoge == 100
 and foo == 200
 and piyo == 500):
    print('全て同じです。')


# bool型は変数だけ
flag = True
# flagがTrueなら実行
if flag:
    print('Only "flag"')
# flagがFalseなら実行
if not flag:
    print('Only "not flag"')


# 条件式はできるだけ否定を入れない
'''
ド・モルガンの法則
not A and not B == not (A or  B)
not A or  not B == not (A and B)
'''
flag1 = False
flag2 = False

# 改良前
if not flag1 and not flag2:
    print('どちらもFalseならば実行')
# 改良後
if not (flag1 or flag2):
    print('どちらもTrueでなければ実行')
# 処理をelseブロックに移動
if flag1 or flag2:
    pass
else:
    print('どちらもTrueでなければ実行')