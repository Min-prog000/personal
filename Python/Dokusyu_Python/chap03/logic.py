# 論理演算子


x = True
y = False
# and : 論理積
print(x and y)
# or : 論理和
print(x or y)
# ^ : 排他的論理和
print(x ^ y)
# not : 否定
print(not x)


# ショートカット演算
# 一つ目の式の真偽で全体の真偽が決まる場合二つ目の式を評価せず次の行に移る
#   論理積 -> 一つ目が偽の場合次行へ（真の場合は二つ目の式を評価）
#   論理和 -> 一つ目が真の場合次行へ（偽の場合は二つ目の式を評価）
# 二つ目の式を評価するかどうかの条件分岐（if文）として動作する
# （ただし可読性が下がるし動作が分かりづらい）
# &（論理積）と|（論理和）にはショートカットがない

x = 1
# if文の場合
if x != 2:
    print('実行されました。')
# ショットカットを使う場合
x == 2 or print('実行されました。')

# 実例
print(True and 1)   # 1
print(False and 2)  # False
print(True or 3)    # True
print(False or 4)   # 4

def hoge():
    pass
print(hoge() or 'default')  # default


# 比較演算子の結合

x = 60
# 結合なし（二つの式で論理積を挟む）
print(x >= 50 and x <= 100)
# 結合あり（変数を二つの基準で挟む）
print(50 <= x <= 100)