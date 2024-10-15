def silence(sentence, n):
  if n == 0:
    return sentence
  if n >= len(sentence):
    return ''
  return sentence[:-n] + '-'

print("Tester silence... ", end="")
assert "Hei på deg!" == silence("Hei på deg!", 0)
assert "Hva skje-" == silence("Hva skjer?", 2)
assert "" == silence("Em.....", 7)
assert "Kan du slutte å avbryte-" == silence("Kan du slutte å avbryte meg?", 5)
assert ".-" == silence("...", 2)
print("OK")
