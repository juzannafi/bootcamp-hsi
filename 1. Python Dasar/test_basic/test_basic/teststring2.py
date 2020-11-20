#!/usr/bin/python2.4 -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0


# D. verbing
# Diberikan sebuah string s, jika panjang string minimal 3 maka tambahkan `ing`
# dibelakangnya. kecuali string tersebut sudah berakhiran dengan `ing`, maka
# tidak ditambahkan `ing` tp tambahkan `ly`.
# Jika string kurang dari 3, tidak dirubah
# Buat return dari string yang telah diproses tersebut
def verbing(s):
  # +++tulis code anda disini+++
  return


# E. not_bad
# Diberikan sebuah string s, cari substring `not` dan `bad`.
# Jika ada `not` yang diikuti dengan `bad`, maka ganti kalimat yang dari
# `not` ... `bad` menjadi `good`.
# return string yang telah diproses tersebut
# Contoh: `This dinner is not that bad` => `This dinner is good`
# (artinya 'not that bad' hilang ganti 'good')
def not_bad(s):
  # +++tulis code anda disini+++
  return


# F. front_back
# Membagi string menjadi 2 bagian.
# Jika panjangnya genap, maka bagian depan dan belakang sama panjang.
# Jika panjangnya ganjil, maka yang depan yang lebih banyak.
# contoh: 'abcd' => 'ab' dan 'cd', sementara 'abcde' => 'abc' dan 'de'
# Diberikan inputan 2 string yaitu a dan b
# nah, mestinya ketika masing2 dari string tersebut dibagi, maka akan ada 4
# Jadi buat return menjadi: a(depan) + b(depan) + a(belakang) + b(belakang)
def front_back(a, b):
  # +++tulis code anda disini+++
  return


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
  print('verbing')
  test(verbing('hail'), 'hailing')
  test(verbing('swiming'), 'swimingly')
  test(verbing('do'), 'do')

  print('not_bad')
  test(not_bad('This movie is not so bad'), 'This movie is good')
  test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
  test(not_bad('This tea is not hot'), 'This tea is not hot')
  test(not_bad("It's bad yet not"), "It's bad yet not")

  print('front_back')
  test(front_back('abcd', 'xy'), 'abxcdy')
  test(front_back('abcde', 'xyz'), 'abcxydez')
  test(front_back('Kitten', 'Donut'), 'KitDontenut')

if __name__ == '__main__':
  main()
