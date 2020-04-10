
# 6 p -----------------------------------------------------------------------------

while True:
    a = input("Результат спортсмена в первый день:\n")
    if a.isdigit() == True:
        a = int(a)
        break
    else:
        print("Неверно!")

while True:
    b = input("Результат спортсмена в последний день:\n")
    if b.isdigit() == True:
        b = int(b)
        break
    else:
        print("Неверно!")

day = 1
print(f'1-й день: {a}')
while a < b:
    day += 1
    a += a/10
    print(f'{day}-й день: {"%.2f" % a}')

print()
print(f'на {day}-й день спортсмен достиг результата — не менее {b} км.')
