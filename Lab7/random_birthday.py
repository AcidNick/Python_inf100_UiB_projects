import random
from datetime import datetime, timedelta
from leapyear import is_leap_year


def random_birthday(year: int) -> str:
    random_day = random.randrange(366 if is_leap_year(year) else 365)
    random_date = datetime(year=year, month=1, day=1) + timedelta(days=random_day)
    return random_date.strftime('%d.%m.%Y')

print(random_birthday(2023))