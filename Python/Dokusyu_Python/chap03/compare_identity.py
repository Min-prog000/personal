# 同一性と同値性


# 同一性 : 同じオブジェクトを参照していること（アドレス比較）
# 同値性 : オブジェクトが同じ値を格納していること（値比較）

data1 = [1, 2, 3]
data2 = [1, 2, 3]

# is : 同一性確認（アドレス比較）
#      値の格納場所が同じかどうか
print(data1 is data2)   # False
# "data2 = data1" と記述していれば同一性が確保される

# == : 同値性確認（値比較）
#      格納された値が同じかどうか
print(data1 == data1)   # True


# イミュータブル型の同一性

# （下のdata1, data2のように）同じ値を別々に格納したとき
#   ミュータブル : 別々のアドレスに格納
#                     -> 参照先は別
#                     -> 同一性なし
#   イミュータブル : 同じ値が格納されたアドレスを参照
#                     -> 参照先は同じ
#                     -> 同一性あり
data1 = 'あいう'
data2 = 'あいう'

print(data1 is data2)   # True
print(data1 == data2)   # True


# Noneの比較はis
hoge = None         # 型・値がNone
print(hoge is None) # True
hoge = []           # 中身はないけどリスト -> Noneではない
print(hoge is None) # False