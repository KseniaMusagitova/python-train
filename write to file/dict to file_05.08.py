with open('dictionary.txt', 'w') as f:
    information = dict()
    for i in range(5):
        keys = input('Введите вопрос:')
        values = input('Введите ответ:')
        information[keys] = values
        print(information)
    f.write(str(information))








