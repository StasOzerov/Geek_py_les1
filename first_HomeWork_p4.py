
# 4 p -----------------------------------------------------------------------------

test_4p = 0
'''
if test_4p == 1:
    print("Промежуточные состяния")
'''

while True:
    us_dgtl = input("Запишите любое положительное число:\n")
    if us_dgtl.isdigit() == True:
        len_dgtl = len(us_dgtl)
        op_dgtl = int(us_dgtl)
        break
    else:
        print("Неверно!")

max_fig = 0
while len_dgtl > 0:
    if test_4p == 1:
        print("new cycle")
        print("    len_dgtl =", len_dgtl)
    tmp_fig = op_dgtl // 10**(len_dgtl-1)
    if test_4p == 1:
        print("    tmp_fig =", tmp_fig)
    op_dgtl -= tmp_fig * 10**(len_dgtl-1)
    if test_4p == 1:
        print("    op_dgtl =", op_dgtl)
    len_dgtl -= 1
    if max_fig < tmp_fig:
        max_fig = tmp_fig
    if test_4p == 1:
        print("    max_fig =", max_fig)

print()
print("Наибольшая цифра в числе =", max_fig)
