# Salary, Percent to be saved, Cost of dream home.
def saving(s, p, c):
  p = p/100
  equity = 0.25*c
  saved = 0
  yearly_interest = 0.04
  monthly_interest = yearly_interest/12
  montly_savings = s/12*p
  months = 0
  while saved < equity:
    saved += montly_savings + saved*monthly_interest
    months += 1

  return months

print(saving(500000, 20, 300000))
