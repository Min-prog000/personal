# 文字列型（str） - 特殊な文字列表現

# 複数行文字列
print("""こんにちは、
あかちゃん""")

# 連続した文字列リテラルは自動連結される
msg = 'こんにちは、''あかちゃん！'
print(msg)

# ()[]{}内では改行可（複数行での表現が可能）
msg = (
    'こんにちは、'
    'あかちゃん！'
)
print(msg)


# raw文字列（エスケープシーケンスの無効化）
# 文字列の前にr, R
print("C:\\Windows\\AppPatch\\en-US")
print(r"C:\Windows\AppPatch\en-US")


# フォーマット文字列（変数の埋め込み）
# 文字列の前にf, F
name = "山田"
print(f"こんにちは、{name}さん！")
# 式・関数も使用可
print(f"2 + 4 = {2+4}")
print(f"-5の絶対値は{abs(-5)}")


# 特殊な表現の同時使用
name = "山田"
print(fr'''おはよう、{name}さん！
パスは「C:\Windows\AppPatch\en-US」です！''')
# fr構文内での{}は"{{}}"で表す
print(fr'''{{}}''')