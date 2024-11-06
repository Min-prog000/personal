# リストの比較


data1 = [1, 2, 3]
data2 = [1, 5]
data3 = [1, 2]

# 要素ごとに比較して最初に得られた結果を全体の大小とする
# exp. 1 == 1
#      2 < 5
#      -> data1 < data2
#      -> True
print(data1 < data2)

# 比較が全て等しくどちらかの要素がなくなった場合は
# 要素数の少ない方を小さいと見なす
# exp. 1 == 1
#      2 == 2
#      3 ?? _
#      -> data1 > data3
#      -> False
print(data1 < data3)