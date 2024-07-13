months = 12
stays = 0 # не изменять
salary = 1
total = 40
wasted = 0 # не изменять
employees = 2

while months > 0 and total - salary * employees >= 0:
    total -= salary * employees
    wasted += salary * employees
    months -= 1
    stays += 1

print(f"На {employees} рабочих было потрачено {wasted} рублей за {stays} месяцев\n"
      f"Остаток денег в компании равен {total} рублей\n"
      f"На всех уходило в месяц {salary * employees} рублей")
