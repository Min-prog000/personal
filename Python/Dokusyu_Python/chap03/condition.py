# 条件演算子


# 条件式の真偽で処理を変える（ifとelse両方必要）
# True
score = 75
print('合格' if score >= 70 else '不合格...')
# False
score = 60
print('合格' if score >= 70 else '不合格...')

# 条件を2つにすることも可能（ただし可読性が下がる）
print('合格' if score >= 70 else '惜しい、もうちょっと...' if score >= 50 
      else 'もっと頑張ろう')
# 以下と同じ
if score >= 70:
    print('合格')
elif score >= 50:
    print('惜しい、もうちょっと...')
else:
    print('もっと頑張ろう')