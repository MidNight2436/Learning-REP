try:
    x_str = input("Введите список чисел через запятую: ")
    x_list = [int(num.strip()) for num in x_str.split(",")]
    print(x_list)

    def second_largest(lst):
        unique = sorted(set(lst), reverse=True)
        if len(unique) < 2:
            raise ValueError("В списке должно быть как минимум два разных числа")
        return unique[1]

    print("Второе по величине число:", second_largest(x_list))

except ValueError as e:
    print("Ошибка:", e)