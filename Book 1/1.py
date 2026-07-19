# реверс ввода

z = str(input("Введите слово: "))

x = list(z)

reverse = ""

for i in range(len(x)):
    reverse += x.pop()

print(reverse)