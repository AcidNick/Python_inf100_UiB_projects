from hashlib import sha256
from time import perf_counter
from itertools import product
from itertools import combinations
from itertools import permutations

def getHash(passwd = input('Write password with format "UUUdddd" example:"ABC1234":\n')):
  passwd = passwd.upper()
  # convert string to bytes so it can be used in a hashing funtion.
  # encrypt the password with sha256 and convert the hash to hexadecimal
  hash = sha256(passwd.encode('utf-8')).hexdigest()
  return hash

passwd_hash = getHash('BBB6969')
print(passwd_hash)

def bruteforce(hash):
  passwd = ''
  alfabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  tall = '0123456789'
  print('Cracking password ...')
  for letters in product(alfabet, repeat=3):
    for numbers in product(tall, repeat=4):
      for passwd in combinations(letters + numbers, 7):
        # print(''.join(passwd))
        if getHash(''.join(passwd)) == hash:
          return passwd

  return None

start = perf_counter()
plain_passwd = bruteforce(passwd_hash)
print(f'The password is {plain_passwd}')
end = perf_counter()
print(f'Cracking {plain_passwd} took {(end-start):.2f} seconds')
