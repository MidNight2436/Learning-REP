x = int(input("Введите длину списка: "))
spisok = list()
for i in range(x + 1):
    if i % 5 == 3:
        spisok.append(i)
print(spisok)
print(list(reversed(spisok)))