# 文字列操作 - 予約語の判別


# keyword.iskeyword : 予約語かどうかを判別
# isidentifier : 識別子に使えるかどうかを判別

import keyword
id1 = 'tiff'
id2 = 'if'

# 予約語かどうか
print(keyword.iskeyword(id1)) # True
print(keyword.iskeyword(id2)) # False

# 識別子に使えるかどうか
print(id1.isidentifier())     # True
print(id2.isidentifier())     # True