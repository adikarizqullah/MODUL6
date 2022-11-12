def biodata (tahunLahir, A, B):
    tahun_sekarang = 2020
    umur = tahun_sekarang - tahunLahir
    print("\nPerkenalkan Nama Saya : "+ A)
    print("\nUmur Saya : %d" %(umur))
    print("Saya Adalah Angkatan : ", tahun_sekarang)
    print("Asal Saya dari : "+ B)

    tahunLahir = int(input())
    A = str(input())
    B = str(input())
    biodata(tahunLahir, A, B) 