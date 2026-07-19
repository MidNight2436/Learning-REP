# Капот и Тапок, когда разные слова из одних букв

def anagramma(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    return sorted(s1) == sorted(s2)

s1 = input("Введите первое слово: ")
s2 = input("Введите второе слово: ")

print(anagramma(s1, s2))