def vowels(s):
  vowels = 0
  for char in s:
    if char.lower() in 'aeiou':
      vowels += 1
  return vowels

print("Tester vowels... ", end="")
assert 5 == vowels("Pingu in the city")
assert 9 == vowels("Frieren: Beyond Journey's End")
assert 3 == vowels("Programming")
assert 0 == vowels("Hmm")
print("OK")
