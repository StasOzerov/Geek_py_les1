
# 3 p -----------------------------------------------------------------------------

while True:
    us_dgtl = input("Запишите любое положительное число n:\n")
    if us_dgtl.isdigit() == True:
        break
    else:
        print("Неверно!")

print('Согласно условию "n + nn + nnn" получаем:')
print(int(us_dgtl) + int(us_dgtl+us_dgtl) + int(us_dgtl+us_dgtl+us_dgtl), "первым способом")
print(int(us_dgtl) + int(us_dgtl*2) + int(us_dgtl*3), "вторым способом")
