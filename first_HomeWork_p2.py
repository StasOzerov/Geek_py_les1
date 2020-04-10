
# 2 p -----------------------------------------------------------------------------

test_2p = 0
'''
if test_2p == 1:
    print("Промежуточные состяния")
'''

while True:
    user_sec = input("Введите время в секундах:\n")
    if user_sec.isdigit() == True:
        user_sec = int(user_sec)
        break
    else:
        print("Неверно!")

operand_day = 0
while user_sec >= 24*60*60:
    operand_day += 1
    user_sec -= 24*60*60
if test_2p == 1:
    print("Количество дней:", operand_day)

operand_hour = 0
while user_sec >= 60*60:
    operand_hour += 1
    user_sec -= 60*60
if test_2p == 1:
    print("Количество часов:", operand_hour)

operand_min = 0
while user_sec >= 60:
    operand_min += 1
    user_sec -= 60
operand_sec = user_sec
if test_2p == 1:
    print("Количество минут:", operand_min)
    print("Количество секунд:", operand_sec)

operand_hour = "%02d" % operand_hour
operand_min = "%02d" % operand_min
operand_sec = "%02d" % operand_sec

print()
print('Первый способ форматирования')
print('{h}:{m}:{s}'.format(h=operand_hour, m=operand_min, s=operand_sec))
print('Второй способ форматирования')
print(f'{operand_hour}:{operand_min}:{operand_sec}')
