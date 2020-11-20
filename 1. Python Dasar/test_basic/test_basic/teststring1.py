#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0


# Latihan String Dasar
# Lengkapi kode dari fungsi2 berikut. Fungsi main() dan test() sudah disiapkan 
# untuk mengetes code anda.
# Fungsi tersebut akan menampilkan OK ketika code anda benar


# A. donuts
# Diberikan parameter count dengan tipe data int. Buatlah return menjadi
# 'Number of donuts: <count>', dimana <count> adalah diambil dari parameter
# Sementara itu, jika count ini 10 atau lebih, maka tampilkan 'many'
# Contoh: donuts(5) akan return 'Number of donuts: 5', dan 
# donuts(23) akan return 'Number of donuts: many'
def donuts(count):
  # +++tulis code anda disini+++
  if(count >= 10):
    number = "many"
  else:
    number = count
  return "Number of donuts: %s" % str(number)


# B. both_ends
# Diberikan parameter s (string), buat code agar memiliki return terdiri dari 
# 2 karakter awal dan 2 karakter terakhir dari string tersebut. Dan kalau
# panjang string kurang dari 2, maka tampilkan string kosongan
# Contoh: both_ends('spring') maka akan memiliki return 'spng', dan
# both_ends('s') maka akan memiliki return ''
def both_ends(s):
  # +++tulis code anda disini+++
  if(len(s) < 2):
    return ''
  else:
    return (s[:2] + s[-2:])

# C. fix_start
# Diberikan string s, buat code agar memiliki return string yang mana hurup
# (char) yang sama dengan hurup pertama diganti menjadi '*', kecuali hurup
# pertama tersebut.
# Contoh: fix_start('babble') akan menampilkan 'ba**le'
# Petunjuk: gunakan fungsi replace bawaan dari string, s.replace(awal, akhir)
# akan mengganti awal menjadi akhir
def fix_start(s):
  # +++tulis code anda disini+++
  awal = s[0]
  # print(awal)
  s = s.replace(awal, '*')
  # print(s)
  s = awal + s[1:]
  # print(s)
  return s


# D. MixUp
# Diberikan 2 parameter a dan b, buat kembalian sebuah string dengan a dan b
# dijadikan 1 dan dipisahkan dengan spasi, dan juga tukar dua hurup pertama
# dari masing2 string tersebut
# contoh:
#   'mix', 'pod' -> 'pox mid'
#   'dog', 'dinner' -> 'dig donner'
# Asumsikan bahwa yang dimasukkan a dan b, lebih dari 2 karakter
def mix_up(a, b):
  # +++tulis code anda disini+++
  s1 = b[:2] + a[2:]
  s2 = a[:2] + b[2:]
  return s1 + " " + s2


"""
fungsi test() dan main() tidak usah dirubah, ini hanya untuk ngetes
"""
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


def main():
  print('donuts')
  # Each line calls donuts, compares its result to the expected for that call.
  test(donuts(4), 'Number of donuts: 4')
  test(donuts(9), 'Number of donuts: 9')
  test(donuts(10), 'Number of donuts: many')
  test(donuts(99), 'Number of donuts: many')

  print('both_ends')
  test(both_ends('spring'), 'spng')
  test(both_ends('Hello'), 'Helo')
  test(both_ends('a'), '')
  test(both_ends('xyz'), 'xyyz')

  print('fix_start')
  test(fix_start('babble'), 'ba**le')
  test(fix_start('aardvark'), 'a*rdv*rk')
  test(fix_start('google'), 'goo*le')
  test(fix_start('donut'), 'donut')

  print('mix_up')
  test(mix_up('mix', 'pod'), 'pox mid')
  test(mix_up('dog', 'dinner'), 'dig donner')
  test(mix_up('gnash', 'sport'), 'spash gnort')
  test(mix_up('pezzy', 'firm'), 'fizzy perm')


# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()
