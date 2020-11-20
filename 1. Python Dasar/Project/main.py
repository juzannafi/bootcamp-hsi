string1 = "Hello"
string2 = "dunia"
string3 = string1 + " " + string2

print(string3)

string4 = "5"
number4 = int(string4)

print(type(string4), "%s" % number4)

#Latihan
nama1 = "Juz'an"
nama2 = "Nafi"
umur = 21

print("Nama saya " + nama1 + " " + nama2 + ", umur saya " + str(umur) + " tahun.")
print("Nama saya %s %s, umur saya %d tahun" % (nama1, nama2, umur))
# print("Nama saya {1} {2}, umur saya {3} tahun").format()

# List
list1 = [4, 2, 3, 7, 8]
print(list1)
print(max(list1))
print(min(list1))
list1.sort()
print(list1)

list1.append(6)

print(list1)
print(list1[1])
print(list1[3])
print(list1[:2])

list_nama = ["Syarif", "Hari", "Ai", "Joko"]
print(list_nama[-2:])

dict1 = {'syarif' : 30, 'Hari' : 33}
dict1['Sukro'] = 50
print(dict1)

data_peserta = []
peserta1 = {'nama' : 'syarif', 'umur' : 30}
peserta1['alamat'] = 'Sleman'
# data_peserta.append(peserta1)
# print(data_peserta)
peserta1['no_hape'] = '0818123456'
data_peserta.append(peserta1)
print(data_peserta)

# Operator
number1 = 1
number2 = 3
jumlah = number1 + number2
print(jumlah)

string1 = "hello"
string2 = "world"

hello = string1 + " " + string2
print(hello.upper())
print(len(hello))
print(hello[:2])

name = "Juz'an\n"
print(name*3)

#Condition
umur = 21

if umur > 17:
    print("%s, Anda sudah bisa bikin KTP" % name)
else:
    print("%s, maaf Anda belum bisa bikin KTP" % name)

if umur > 17 and umur < 50:
    print("17<x<50")

list_peserta = ["nama1", "nama2", "nama3"]
nama_saya = "Syarif"
if nama_saya in list_peserta:
    print("Anda masuk dalam list peserta")
else:
    print("Maaf Anda bukan peserta")

if len(list_nama)>10:
    print("Siap dimulai.")
elif len(list_nama) == 4:
    print("Dimulai aja dulu")
else:
    print("Belum siap dimulai. Menunggu temannya.")

#LOOP
x = 5
for i in range(x):
    print(i)

for i in range(4, 10):
    print(i)

x = 5
while x>0:
    print(x)
    x -= 1

for peserta in list_peserta:
    print(peserta)

# Function
def tampilkan_hello():
    return "Hello"

print(tampilkan_hello())

stringx = tampilkan_hello()
print(stringx)

def penjumlahan(angka1, angka2):
    return angka1 + angka2

print(penjumlahan(2, 4))

def penjumlahan(angka1, angka2, *args):
    jumlah = angka1 + angka2
    for angka in args:
        jumlah += angka
    return jumlah
print(penjumlahan(2, 4, 5, 10))

def set_fullname(nama_depan="", nama_belakang=""):
    return nama_depan + " " + nama_belakang

print(set_fullname("ai", "jogja"))
print(set_fullname(nama_belakang="ai", nama_depan="jogja"))

# def get_fullname(nama_depan="", nama_belakang="", **kwargs):
#     if kwargs.get('nama_tengah'):
#         return nama_depan + " " + nama_tengah + " " + nama_belakang
#     else:
#         return nama_depan + " " + nama_belakang

def pecahan(money):
    out = int(money / 100000)
    print(out)
    money -= out*100000
    out = int(money / 20000)
    print(out)
    money -= out*20000
    out = int(money / 1000)
    print(out)
    money -= out*1000
    out = int(money / 200)
    print(out)
    money -= out*200
    out = int(money / 10)
    print(out)

money = 675350
pecahan(money)

# List comprehension

list_angka = [3, 4, 1, 5, 6, 8, 9, 10, 99, 16, 18]

ganjil = []
for angka in list_angka:
    if angka % 2 != 0:
        ganjil.append(angka)

print(ganjil)

genap = [angka for angka in list_angka if angka % 2 == 0]
print(genap)

#CLASS
class User:
    nama = "Syarif"

    def greeting(self, nama=""):
        if nama:
            self.nama = nama
        return "Hello %s, selamat pagi" % self.nama

user1 = User()
print(user1.nama)
print(user1.greeting())
print(user1.greeting(nama="Ai Jogja"))

#nama class = huruf besar
#init = constructor

class Kendaraan:
    def __init__(self, nama, merk, harga=0, warna=''):
        self.nama = nama
        self.merk = merk
        self.harga = harga
        self.warna = warna

    def harga_jual(self, pajak=True):
        if(pajak):
            nominal_pajak = self.harga * 0.1
            harga_jual = self.harga + nominal_pajak
        else:
            harga_jual = self.harga
        return harga_jual

class Motor(Kendaraan):
    def __init__(self):
        super().__init__(self, nama, merk, harga=0, warna='')

    def harga_jual(self, pajak=True):
        harga_jual = super().harga_jual(self, pajak=True)

        if self.warna == 'hitam':
            harga_jual += 500000
        return harga_jual

# kendaraan =
