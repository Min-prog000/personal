# 例外処理 - try...except


# 例外 : 未然に防げない問題（予想していた値と違う、など）
# 構文エラー : 自分で直せる問題

# try...except命令（例外処理）
'''
try:
    例外が発生する可能性のある処理
except 例外の種類 as 例外変数:
    例外が発生したときの処理
'''

try:
    num = input('数字を入力してください：')
    print('2倍すると... ', float(num) * 2)
except ValueError as ex:
    print('エラー発生：', ex)

# 例外変数
# 参照しない場合（例外変数を使わない）
# -> 'as 例外変数'はなし
'''
except ValueError:
    print('エラーが発生しました！')
'''
# 複数の例外処理で同じ処理をする場合
# -> エラーの種類を()で囲む
'''
except (ValueError, TypeError) as ex:
    print('エラーが発生しました！')
'''
# 全ての例外を捕捉する場合（例外の捕捉ができなくなるので基本は非推奨）
# -> 例外の種類からなし
'''
except:
    print('エラーが発生しました！')
'''