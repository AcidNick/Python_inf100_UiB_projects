from hashlib import sha256
from time import perf_counter
import re
from itertools import product

def getHash(passwd = input('Write password with format "UUUdddd" example:"ABC1234":\n')):
  passwd = passwd.upper()
  pattern = r'^[A-Z]{3}\d{4}$' #Setting up a pattern for the password.
  while re.match(pattern, passwd) is None: #Checks if input is in the correct format.
    passwd = input('Please use correct format "UUUdddd" example:"ABC1234":\n')
    passwd = passwd.upper()
  # convert string to bytes so it can be used in a hashing funtion.
  # encrypt the password with sha256 and convert the hash to hexadecimal
  hash = sha256(passwd.encode('utf-8')).hexdigest()
  return hash

def bruteforce(hash):
  start = perf_counter()
  alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  numbers = '0123456789'
  attempts = 0
  print('Cracking password ...')
  for letter in product(alphabet, repeat=3):
    for number in product(numbers, repeat=4):
      possible_passwd = ''.join(letter)+''.join(number)
      possible_hash = getHash(possible_passwd)
      attempts += 1
      if attempts % 5123 == 0: #Prints only some of the attempts to not slow down the process to much and create a scrolling effect.
        print(f'#{attempts:,} | {possible_passwd} | {possible_hash}')

      if possible_hash == hash:
        print(f'\n#{attempts:,} | {possible_passwd} | {possible_hash}')
        print(f'\nPassword is {possible_passwd}')
        print(f'Hash: {possible_hash}')
        print(f'Succesfully cracked in {attempts:,} attempts || nilau0421')

        end = perf_counter()
        elapsed_time = end-start
        print(f'\nCracking {possible_passwd} took {(elapsed_time // 60):.0f} minutes and {(elapsed_time % 60):.2f} seconds\n\n')
        return possible_passwd
      # print(passwd)
  return None

passwd_hash = getHash()
print(passwd_hash)

plain_passwd = bruteforce(passwd_hash)
