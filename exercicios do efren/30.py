i_i = input().split()
d_i = int(i_i[1])

h_i = input().split(':')
h_i = int(h_i[0]), int(h_i[1]), int(h_i[2])

i_f = input().split()
d_f = int(i_f[1])

h_f = input().split(':')
h_f = int(h_f[0]), int(h_f[1]), int(h_f[2])

total_s_i = d_i * 24 * 60 * 60 + h_i[0] * 60 * 60 + h_i[1] * 60 + h_i[2]
total_s_f = d_f * 24 * 60 * 60 + h_f[0] * 60 * 60 + h_f[1] * 60 + h_f[2]
diferenca = total_s_f - total_s_i

d = diferenca // (24 * 60 * 60)
diferenca %= (24 * 60 * 60)
h = diferenca // (60 * 60)
diferenca %= (60 * 60)
m = diferenca // 60
s = diferenca % 60

print(f"{d} dia(s)")
print(f"{h} hora(s)")
print(f"{m} minuto(s)")
print(f"{s} segundo(s)")