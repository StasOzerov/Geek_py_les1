# 1 p -----------------------------------------------------------------------------

operand_int = 5
print(operand_int)
operand_fl  = 2.67
print(operand_fl)
operand_str = "hello world"
print(operand_str)

while True:
    user_digit1 = input("Введите 1-е положительное число:\n")
    if user_digit1.isdigit() == True:
        user_digit1 = int(user_digit1)
        print("Здорово!")
        user_digit2 = input("Теперь, введите 2-е положительное число\n")
        if  user_digit2.isdigit() == True:
            user_digit2 = int(user_digit2)
            print("Супер!")
            break
        else:
            print("Эх, почти( Придётся пройти круг Ада сначала")
    else:
        print("Неверно!")

print("Ваши положительные числа:", user_digit1, "и", user_digit2, "\n")

while True:
    user_string1 = input("Введите 1-ю строку:\n")
    if user_string1.isdigit() == False:
        print("Здорово!")
        user_string2 = input("Теперь, введите 2-ю строку\n")
        if  user_string2.isdigit() == False:
            print("Супер!")
            break
        else:
            print("Эх, почти( Придётся пройти круг Ада сначала")
    else:
        print("Неверно!")

print("Ваши строки:\n", user_string1,"\n", user_string2, "\n")
