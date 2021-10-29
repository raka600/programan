def odd(n):
 hasil = n % 2
 if hasil != 0:
     hasilnya=True
 else:
     hasilnya=False
 return hasilnya


def pelangi (warna):
  print(f'Salah satu warna pelangi adalah {warna}')

class Garuda():
    def __init__(self):
        print("Garuda bulu coklat, kaki kuning kuku hitam")
tampilkan = Garuda()

class Kelulusan():

    def __init__(self, masukan_nama):
        self.nama = masukan_nama

    def nilai(self, nilai):
        if nilai >= 70:
            print(self.nama,'Selamat anda telah lulus',nilai)
        else:
            print(self.nama,'Mohon maaf anda belum lulus',nilai)

mhs=Kelulusan("RAKASONA")
print(mhs.nama)
mhs.nilai(80)



