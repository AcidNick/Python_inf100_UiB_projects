rad1 = input('Første raden:\n')
rad2 = input('Andre raden:\n')
rad3 = input('Tredje raden:\n')

# lengst = max(len(rad1),len(rad2),len(rad3))

lengst = len(max(rad1,rad2,rad3, key=len))
print('')

print(f"{'@'*(4+lengst)}")
print(f"@ {' '*(lengst-len(rad1))+rad1} @")
print(f"@ {' '*(lengst-len(rad2))+rad2} @")
print(f"@ {' '*(lengst-len(rad3))+rad3} @")
print(f"{'@'*(4+lengst)}")
