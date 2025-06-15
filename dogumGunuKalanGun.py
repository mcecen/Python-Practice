# birthday_countdown.py
from datetime import datetime

def days_until_birthday(birthday_str):
    today = datetime.today()
    birthday = datetime.strptime(birthday_str, "%Y-%m-%d").replace(year=today.year)
    if birthday < today:
        birthday = birthday.replace(year=today.year + 1)
    return (birthday - today).days

if __name__ == "__main__":
    date_input = input("Doğum gününüzü girin (YYYY-AA-GG): ")
    kalan = days_until_birthday(date_input)
    print(f"Doğum gününe {kalan} gün kaldı!")