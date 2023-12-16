from datetime import date
w = input("введите возраст:")
w = int(w)

today = date.today().year
print(f"вы родились в {today - w}")
