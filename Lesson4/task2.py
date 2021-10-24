def task_2():
    my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
    print(f'Исходный список: {my_list}')

    result_list = [my_list[index] for index in range(1, len(my_list)) if my_list[index] > my_list[index-1]]

    print(f'Результат: {result_list}')


if __name__ == "__main__":
    task_2()
