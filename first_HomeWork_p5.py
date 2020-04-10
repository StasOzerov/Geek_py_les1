
# 5 p -----------------------------------------------------------------------------

while True:
    revenue = input("Запишите выручку фирмы в рублях:\n")
    if revenue.isdigit() == True:
        revenue = int(revenue)
        break
    else:
        print("Неверно!")

while True:
    expenses = input("Запишите издержки фирмы в рублях:\n")
    if expenses.isdigit() == True:
        expenses = int(expenses)
        break
    else:
        print("Неверно!")

if revenue > expenses:
    print("Выручка больше издержек.")
    print("Чистая прибыль =", revenue - expenses, "руб.")
elif revenue < expenses:
    print("Издержки больше выручки.")
else:
    print("Выручка равна издержкам.")

while True:
    personal = input("Запишите кол-во сотрудников в вашей фирме:\n")
    if personal.isdigit() == True:
        personal = int(personal)
        break
    else:
        print("Неверно!")

if revenue > expenses:
    print("Зарплата сотрудников в этом месяце =", (revenue - expenses) // personal, "руб.")
elif revenue < expenses:
    print("Удержание денег с сотрудников в этом месяце =", (expenses - revenue) // personal, "руб.")
else:
    print("В этом месяце сотрудники остаются без зарплаты.")
