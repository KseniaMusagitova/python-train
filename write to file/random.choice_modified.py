import random
import string

letters = string.ascii_lowercase
max_len = ''

with open('test_data.txt', 'w+') as f:
    for m, k in enumerate(range(random.randint(3, 5))):
        line = []
        for n, i in enumerate(range(random.randint(3, 5))):
            word = ''.join(random.choice(letters) for l in range(random.randint(5, 10))) + ' '
            line.append(word)
            if len(word) > len(max_len):
                max_len = word
                max_len_list = [max_len.rstrip()]
                x, y = m, n
            if len(word) == len(max_len):
                if word not in max_len_list:
                    max_len_list.append(word.rstrip())
        line[-1] += '\n'
        f.writelines(line)


print(f"Самое длинное слово {max_len} находится на {x+1} {y+1}")
print(f'Самые длинные слова: {max_len_list}')