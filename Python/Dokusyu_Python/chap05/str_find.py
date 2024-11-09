# 文字列操作 - 検索


# find  : 前方から文字列検索
# rfind : 後方から文字列検索
#         戻り値は検索する文字列の1文字目の位置
#         見つからなかったときは-1
'''
str.find(sub_str, start, end)
str.rfind(sub_str, start, end)

str : 文字列
sub_str : 検索する文字列
start : 検索開始位置
end : 検索終了位置
'''
# start, endはインデックス指定
# exp : 2文字目から調べたい -> start=1
#       1文字目から8文字目まで調べたい -> start=0, end=8


# e.g.
msg = 'にわにはにわにわとりがいる'

print(msg.find('にわ'))
print(msg.find('にも'))
print(msg.rfind('にわ'))
# 4番目(msg[3])から検索
print(msg.find('にわ', 3))
# 4番目(msg[3])から5番目(msg[4])まで検索
print(msg.find('にわ', 3, 5))
# 負数表現も可能
# 7番目(msg[-7] == msg[6])から13番目(msg[-1] == msg[12])まで検索
print(msg.find('にわ', -7, -1))


# 文字列が入っているかどうかだけのときはin演算子
print('にわ' in msg)


# index/rindex : find/rfindと同じ
#                見つからなかったときは例外

# e.g.
print(msg.index('にわ'))
# ValueError
# print(msg.index('にも'))