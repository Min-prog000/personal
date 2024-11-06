# ループ制御


# break : その場でループを中止して抜け出す
sum = 0
for i in range(1, 101):
    sum += i
    if sum > 1000:
        break
print('合計が1000を超えるのは、1~', i, 'を加算したときです。')


# continue : そのループのみ中止して次のループに移る
sum = 0
for i in range(1, 101):
    if i % 2 != 0:
        continue
    sum += i
print('合計値は', sum, 'です。')