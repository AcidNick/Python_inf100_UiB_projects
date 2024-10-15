def compress(raw_binary):
  compressed = []
  if raw_binary[0] == '1':
    compressed.append(0)
  counter = 1
  for i in range(len(raw_binary)-1):
    if raw_binary[i] == raw_binary[i+1]:
      counter += 1
    else:
      compressed.append(counter)
      counter = 1
  compressed.append(counter)
  return compressed

def decompress(compressed_binary):
  decompressed = ''
  for i in range(len(compressed_binary)):
    decompressed += str(i%2)*compressed_binary[i]
  return decompressed


def test_compress():
    print('Tester compress... ', end='')
    assert([2, 3, 4, 4] == compress('0011100001111'))
    assert([0, 2, 1, 8, 1] == compress('110111111110'))
    assert([4] == compress('0000'))
    print('OK')

def test_decompress():
    print('Tester decompress... ', end='')
    assert('0011100001111' == decompress([2, 3, 4, 4]))
    assert('110111111110' == decompress([0, 2, 1, 8, 1]))
    assert('0000' == decompress([4]))
    print('OK')

if __name__ == '__main__':
  test_compress()
  test_decompress()