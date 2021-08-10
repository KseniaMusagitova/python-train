import random
import string


def generate_random_string(length):
    x = ''.join(random.choice(string.ascii_lowercase) for i in range(length))
    return x


def generate_random_symbols():
    y = ''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(1, 5)))
    return y


with open('test_data.txt', 'w') as f:
    f.write(str(generate_random_string(3)) + '\n')

with open('test_data.txt', 'a') as f:
    f.write(str(generate_random_symbols()))



