z = int(input("Введите количество чисел последовательности Фибоначчи: "))

a, b = 1, 1
spisok = []
for i in range(z):
    spisok.append(a)
    a, b = b, a + b

print(spisok)