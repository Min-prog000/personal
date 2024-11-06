# 文字列の操作 - 文字列の長さの取得


# len
#  文字列の長さを取得
'''
len(chr)
chr : 任意の文字列
'''

title = 'WINGSプロジェクト'
print(len(title))


# east_asian_width
#  全角か半角かを識別し結果を文字列で返す
#  引数が 全角 -> 全角英数 -> 'F'
#                漢字・全角かな -> 'W'
#                特殊文字 -> 'A'
#        半角 -> 半角英数 -> 'Na'
#                半角カタカナ -> 'H'
#                中立(いずれにも属さない) -> 'N'
'''
east_asian_width(chr)
chr : 任意のUnicode文字
'''

import unicodedata
data = 'WINGSプロジェクト２０２０'
count = 0
for ch in data:
    ch_type = unicodedata.east_asian_width(ch)
    if ch_type in 'FWA':
        count += 2
    else:
        count += 1
print(count)