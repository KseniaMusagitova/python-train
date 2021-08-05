fine_word = input('Введите слово: ')

with open("home_work_2_05.08.txt") as file:
    for n, line in enumerate(file.readlines(), 1):
        tmp_list = line.split(' ')
        for m, i in enumerate(tmp_list, 1):
            if fine_word in i.lower():
                print(n, m)




