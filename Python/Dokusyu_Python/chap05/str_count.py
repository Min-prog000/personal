# 文字列操作 - 部分文字列のカウント


# count : 検索する文字列の登場回数をカウントする
'''
str.count(sub_str, start, end)

str : 文字列
sub_str : 検索する文字列
start : 検索開始位置
end : 検索終了位置
'''

# e.g.
msg = 'にわにはにわにわとりがいる'
print(msg.count('にわ'))
# 4番目(msg[3])から検索
print(msg.count('にわ', 3))
# 4番目(msg[3])から6番目(msg[5])
print(msg.count('にわ', 3, 6))

# 重複はカウントしない
msg = 'いちいちいちばにいち'
# msg[0]~msg[3] : 1回
# -> msg[4]から検索再開(msg[2]~msg[5]は1回としてカウントされない)
print(msg.count('いちいち')) # 1