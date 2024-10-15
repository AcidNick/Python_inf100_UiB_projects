from hashlib import sha256
from time import perf_counter

def getHash(passwd = input('Write password with format "UUUdddd" example:"ABC1234":\n')):
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
  for letter1 in alphabet:
    for letter2 in alphabet:
      for letter3 in alphabet:
        for number1 in numbers:
          for number2 in numbers:
            for number3 in numbers:
              for number4 in numbers:
                attempts += 1
                possible_passwd = letter1+letter2+letter3+number1+number2+number3+number4
                
                # if attempts % 1_000_000 == 0: #Prints only some of the attempts to not slow down the process to much and create a scrolling effect.
                #   print(f'#{attempts:,} | {possible_passwd}')

                if getHash(possible_passwd) == hash:
                  correct_hash = getHash(possible_passwd)
                  print(f'\n#{attempts:,} | {possible_passwd} | {correct_hash}')
                  print(f'\nPassword is {possible_passwd}')
                  print(f'Hash: {correct_hash}')
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
