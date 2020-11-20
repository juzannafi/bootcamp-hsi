#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Latihan List Dasar

# C. Diberikan list yang isinya numbers. Buat sebuah kembalian dimana yang sama
# dihapuskan.
# Contoh : [1, 2, 2, 3] returns [1, 2, 3]
# Contoh : [2, 2, 3, 3, 3] returns [2, 3]
def remove_adjacent(nums):
  # +++tulis code anda disini+++
  return


# D. Diberikan dua list yang terurutkan. Buat return list tersebut jadi 1 list
# dan sorted (urut).
# Contoh : ['aa', 'xx', 'zz'] dan ['bb', 'cc'] akan menjadi 
# ['aa', 'bb', 'cc', 'xx', 'zz']
def linear_merge(list1, list2):
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
  print('remove_adjacent')
  test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
  test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
  test(remove_adjacent([]), [])

  print('linear_merge')
  test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
       ['aa', 'aa', 'aa', 'bb', 'bb'])


if __name__ == '__main__':
  main()
