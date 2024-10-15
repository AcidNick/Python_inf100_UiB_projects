def human_to_dog_years(human_yrs):
  if human_yrs <= 2:
    dog_yrs = human_yrs*10.5
    return dog_yrs
  else:
    dog_yrs = (human_yrs-2)*4 + 2*10.5
    return dog_yrs
  
def almost_equals(a, b):
    return abs(a - b) < 0.00000001

print("Tester human_to_dog_years... ", end="")
assert almost_equals(15.75, human_to_dog_years(1.5))
assert almost_equals(21.00, human_to_dog_years(2))
assert almost_equals(57.00, human_to_dog_years(11))
print("OK")
