x = int(input("Введите длинну списка степеней двойки: "))
spisok = []
for i in range(1, x + 1):
    spisok.append(2 ** i)
print(spisok)