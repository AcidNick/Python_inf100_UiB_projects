from leapyear import is_leap_year

print('Testing is_leap_year...', end=' ')
assert is_leap_year(2026) is False
assert is_leap_year(2024) is True
assert is_leap_year(2000) is True
assert is_leap_year(1900) is False
print('OK')