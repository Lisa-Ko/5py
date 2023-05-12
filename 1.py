def Pow(a,b):
    if b == 0:
        return 1
    return a*Pow(a, b-1)
a =int(input('Введите число: '))
b = int(input('Введите степень числа(целое неотрицательно число): '))
print(Pow(a,b))
