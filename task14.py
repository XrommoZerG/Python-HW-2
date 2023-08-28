n = int(input('Введите число '))
brecke = 0
number = 2

for i in range(n):
    if brecke != 1:
        number = number ** i
        if number <= n:
            print(number, end=' ')
            number = 2
        else:
            brecke = 1
    else:
        i = n





