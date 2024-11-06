# 複素数型（complex）

# 複素数 = 実部 + 虚部 * 虚数単位
# 虚数単位はj, J
data1 = 1.0 + 2.0j
data2 = 1.0j
data3 = 2.1 + 4.0J

print(data1)
print(data2)
print(data3)

c1 = 1 + 2j
c2 = 3 + 4j

print(c1 + c2)  # (4+6j)
print(c1 * c2)  # (-5+10j)

# complex関数
# complex(実部, 虚部)
c = complex(1, 5)
print(c)

# real（実部）
print(c.real)
# imag（虚部）
print(c.imag)