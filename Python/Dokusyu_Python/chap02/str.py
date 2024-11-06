# 文字列型（str）

print("You are GREAT teacher!!")

# ダブルクォートを使う場合
# ' "" '（シングルクォートで囲む）
print('You are "GREAT" teacher!!')

# シングルクォートを使う場合
# " '' "（ダブルクォートで囲む）
print("You are 'GREAT' teacher!!")

# どちらも使う場合
# \（エスケープシーケンス）
print('He\'s "GREAT" teacher!!')


# エスケープシーケンス
# \\（バックスラッシュ）
print("\\")
# \`（シングルクォート）
print("\'")
# \"（ダブルクォート）
print('\"')
# \b（バックスペース）
# 直前の1文字を削除 最後だと効果なし
print("Hello,\bWorld")
# \f（フォームフィード）
# ??
print("Hello,\fWorld")
# \n（改行）
print("Hello,\nWorld")
# \r（復帰・キャリッジリターン）
# 以降の文字列のみ出力
print("Hello,\rWorld")
# \改行（バックスラッシュと改行文字を無視）
print("Hello,\
      World")
# \t（水平タブ）
print("Hello,\tWorld")
# \v（垂直タブ）
# 改行してタブ
print("Hello,\vWorld")
# \oXX（8進数の文字XX）
# 使用不可（効果無し）
print("\o11")
# \xXX（16進数の文字XX）
print("\x24")
# \uXXXX（16bitの16進数の文字XXXX）
# UnicodeのXXXXに変換
print("\u0044")
# \UXXXXXXXX（32bitの16進数の文字XXXXXXXX）
# エラー発生
# print("\U18430990")