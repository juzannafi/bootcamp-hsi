#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Latihan List Dasar

# A. match_ends
# Diberikan sebuah list dari string2, buat return count dari panjang string yang mana
# panjangnya 2 atau lebih dan yang karakter pertama dengan karakter terakhir
# sama dari string tersebut
def match_ends(words):
  # +++tulis code anda disini+++
  return


# B. front_x
# Diberikan sebuah list dari string2, buat return list dengan string yang
# telah tersorted, kecuali string yang dimulai dengan `x`.
# Contoh:['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] 
# akan menjadi ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
def front_x(words):
  # +++tulis code anda disini+++
  return


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# Calls the above functions with interesting inputs.
def main():
  print('match_ends')
  test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
  test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
  test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

  print('front_x')
  test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
       ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
  test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
       ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
  test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
       ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])


if __name__ == '__main__':
  main()
