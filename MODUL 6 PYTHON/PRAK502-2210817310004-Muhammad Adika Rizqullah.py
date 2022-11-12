def hitung (n1, n2):
    return n1 - n2
def mutlak (angka):
    return abs (angka)

x1, x2, y1, y2 = input().split()
x1, x2, y1, y2 = map(int,(x1, x2, y1, y2))
hasil = hitung(x1, y1) + hitung(x2, y2)
print(mutlak(hasil))