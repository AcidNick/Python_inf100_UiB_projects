def get_endpoints(i, n, x_lo, x_hi):
  l_tot = x_hi - x_lo
  l_bit = l_tot/n
  x_ilo = x_lo + i*l_bit
  x_ihi = x_ilo + l_bit
  return x_ilo, x_ihi

if __name__ == '__main__':
    x_lo = float(input('x_lo = '))
    x_hi = float(input('x_hi = '))
    n = int(input('n = '))
    for i in range(n):
      start, slutt = get_endpoints(i, n, x_lo, x_hi)
      print(start, slutt)

def almost_equals(a, b):
    return abs(a - b) < 0.0000000001
