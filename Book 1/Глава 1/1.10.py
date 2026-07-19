def summ_n(x):
    y = 0
    for i in range(1, x + 1):
        if i % 2 == 1:
            y += i
    return y
x_str = input("Введите число: ")
x_list = [int(num.strip()) for num in x_str.split(",")]

print("Введённый список:", x_list)
print("Сумма нечётных чисел от 1 до", x_list[0], ":", summ_n(x_list[0]))