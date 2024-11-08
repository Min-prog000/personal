# 文字列操作 - 文字の種類判定


# isalnum : 英数字かどうか（全角ひらがな・漢字はTrue）
print('abc123'.isalnum())              # True
print('こんにちは'.isalnum())           # True
print('今日は'.isalnum())              # True
print('a+b+c'.isalnum())               # False

# isalpha : アルファベットかどうか
print('ABCabc'.isalpha())              # True
print('abc123'.isalpha())              # False

# isascii : ASCII文字かどうか
print('Hello'.isascii())               # True
print('こんにちは'.isascii())           # False

# isdecimal : 10進数かどうか
print('123'.isdecimal())               # True
print('0x123A'.isdecimal())            # False

# isdigit : 数値かどうか
print('123'.isdigit())                 # True
print('abc'.isdigit())                 # False

# isnumeric : 数値文字かどうか
print('百万'.isnumeric())              # True
print('million'.isnumeric())           # False

# isidentifier : 有効な識別子か（ハイフンが入るとFalse）
print('X_train'.isidentifier())        # True
print('X-train'.isidentifier())        # False

# islower : 小文字がどうか
print('hello'.islower())               # True
print('Hello'.islower())               # False

# isupper : 大文字がどうか
print('HELLO'.isupper())               # True
print('Hello'.isupper())               # False

# istitle : 単語の先頭文字だけが大文字か
print('Hello World'.istitle())         # True
print('Hello world'.istitle())         # False

# isprintable : 印字可能な文字かどうか（エスケープシーケンスはFalse）
print('Hello, World!!'.isprintable())  # True
print('Hello,\nworld!!'.isprintable()) # False

# isspace : 空白文字かどうか
print(' '.isspace())                   # True
print('***'.isspace())                 # False