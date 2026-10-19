def jumlah_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

for n in [1, 5, 10, 100]:
    hasil_fungsi = jumlah_n(n)
    hasil_rumus = n * (n + 1) / 2
    print(
        f"n={n}: fungsi={hasil_fungsi}, "
        f"rumus={hasil_rumus}, cocok={hasil_fungsi == hasil_rumus}"
    )