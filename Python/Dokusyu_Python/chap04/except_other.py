# 例外処理 - try...except...else...finally


# else...finally
'''
try:
    例外は発生する可能性のある処理
except:
    例外発生時の処理
else:
    例外が発生しなかったときに実行する処理
finally:
    例外発生の有無に関わらず最後に実行される処理
'''

# 例 : else
while True:
    try:
        num = input('数字を入力してください：')
        print('2倍すると... ', float(num) * 2)
    except:
        print('入力値エラーです。')
    else:
        break

# 例 : finally
try:
    num = input('数字を入力してください：')
    print('2倍すると... ', float(num) * 2)
except:
    print('入力値エラーです。')
finally:
    print('終了します。')