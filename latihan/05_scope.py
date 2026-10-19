x = 10


def demo(x):
    # Parameter x adalah variabel lokal, terpisah dari x di luar fungsi.
    y = x + 5
    print("di dalam fungsi:", x, y)
    return y


hasil = demo(20)
# Pemanggilan demo(20) memakai x lokal bernilai 20; x global tetap 10.
print("di luar fungsi:", x, hasil)