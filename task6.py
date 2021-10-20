def int_func(text):
    return text.title()


#мой вариант функции title
def my_title(text):
    listed_text = list(text)
    listed_text[0] = listed_text[0].upper()
    return ''.join(listed_text)


output_1 = []
output_2 = []
for word in input('Введите строку, слова в которой разделены пробелами: ').split(' '):
    output_1.append(int_func(word))
    output_2.append(my_title(word))

print(f'Вариант1 Строка получается вот такая: {" ".join(output_1)}')
print(f'Вариант2 Строка получается вот такая: {" ".join(output_2)}')