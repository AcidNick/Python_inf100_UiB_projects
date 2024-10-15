# Given values
m = 111
e = 5
n = 437

# Encryption: c = m^e mod n
ciphertext = pow(m, e, n)

# Given values for decryption
c = 222
d = 317

# Decryption: m = c^d mod n
plaintext = pow(c, d, n)

print(ciphertext, plaintext)
