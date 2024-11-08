# 文字列操作 - 大文字・小文字変換


data1 = 'Wings Project'
data2 = 'self learn python'
data3 = 'Fußball'

# lower : 小文字変換
print(data1.lower())

# upper : 大文字変換
print(data1.upper())

# swapcase : 大文字と小文字を反転
print(data1.swapcase())

# capitalize : 先頭文字を大文字に、残りを小文字に変換
print(data2.capitalize())

# title : 単語の先頭文字を大文字に、残りを小文字に変換
#         空白区切りで単語とみなす
print(data2.title())

# casefold : 大文字小文字の区別をなくす
#            英語以外の大文字も小文字にする(lowerでは小文字のまま)
print(data3.lower())     # ß 変化なし
print(data3.casefold())  # ß -> ss