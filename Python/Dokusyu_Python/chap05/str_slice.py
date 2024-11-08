# 文字列操作 - スライス


# スライス構文 : 文字列の部分取得
'''
txt[index]
txt[start:end:step]

txt : 文字列
index : インデックス番号
start : 開始番号
end : 終端番号
step : 増減
'''

# exp.1
title = 'あいうえおかきくけこ'
# インデックス番号のみ : 一要素取得
print(title[2])     # う
# コロン(:) : 範囲取得
print(title[1:4])   # いうえ
# 2番目以降取得
print(title[2:])    # うえおかきくけこ
# 8番目まで取得
print(title[:8])    # あいうえおかきく
# 負の数 : リストの最後から取得
print(title[-1])    # こ
# 全て取得
print(title[:])     # あいうえおかきくけこ
# 3番目以降取得
print(title[-7:])   # えおかきくけこ
# 3番目から4番目まで取得
print(title[-7:-5]) # えお
# 0番目から1つ飛ばしで取得
print(title[::2])   # あうおきけ
# 1番目から1つ飛ばしで取得
print(title[1::2])  # いえかくこ
# 逆順に取得
print(title[::-1])  # こけくきかおえういあ

# sliceオブジェクト
title = 'あいうえおかきくけこ'
# slice : 内的インデックス表現の出力
# exp. 返り値 : (-5, -1, -1)
#      -> -5 : start, -1 : end, -1 : step
#      -> 6番目(-5)から10番目(-1)を逆順(-1)に表示
print(slice(-5, None, -1).indices(len(title)))