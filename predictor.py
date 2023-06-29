import re

import random

min_str_len = 100

full_list = []


def str2list(string):
    return list(string)


def list2str(lst):
    new_str = ''
    for item in lst:
        new_str += str(item)
    return new_str


print('Please provide AI some data to learn...')
print('The current data length is 0, 100 symbols left')

while len(full_list) < min_str_len:
    input_str = str(input('Print a random string containing 0 or 1:'))
    num_list = str2list(input_str)

    for number in num_list:
        if number == '1' or number == '0':
            full_list.append(number)
        else:
            continue

    if len(full_list) >= min_str_len:
        break
    else:
        print(f'Current data length is {len(full_list)}, {min_str_len - len(full_list)} symbols left')

full_str = list2str(full_list)

print('')
print('Final data string:')
print(full_str)

triads_num = 2**3


def num2triad(num):
    binary_triad = bin(num)[2:].zfill(3)
    return binary_triad


triads_lst = []

for number in range(triads_num):
    triad = num2triad(number)
    triads_lst.append(triad)

triad_count = {triad: 0 for triad in triads_lst}
adjacent_0_count = {triad: 0 for triad in triads_lst}
adjacent_1_count = {triad: 0 for triad in triads_lst}


for triad in triads_lst:
    triad_count[triad] = len(re.findall(f'(?={triad})', full_str))
    adjacent_0_count[triad] = len(re.findall(f'(?={triad}0)', full_str))
    adjacent_1_count[triad] = len(re.findall(f'(?={triad}1)', full_str))

print('\nYou have $1000. Every time the system successfully predicts your next press, you lose $1.'
      '\nOtherwise, you earn $1. Print "enough" to leave the game. Let\'s go!')

balance = 1000



position_count = 2

while True:
    prediction = []
    test_str = input('\nPrint a random string containing 0 or 1:')

    if test_str == 'enough':
        print('Game over!')
        break

    test_lst = str2list(test_str)

    while len(test_str) < 4:
        test_str = input('\nPrint a random string containing 0 or 1:')
        if len(test_str) >= 4:
            break

    for i in range(len(test_str) - 3):
        triad = test_str[i:i+3]
        if adjacent_0_count[triad] > adjacent_1_count[triad]:
            prediction.append('0')
        elif adjacent_1_count[triad] > adjacent_0_count[triad]:
            prediction.append('1')
        else:
            prediction.append(str(random.randint(0, 1)))

    position_count_2 = 0

    rights_count = sum(a == b for a, b in zip(test_str[3:], prediction))
    wrongs_count = len(test_str) - 3 - rights_count

    acc = (rights_count/(len(test_str)-3))*100.00

    print('\npredictions:')
    print(f'{list2str(prediction)}')

    print(f'\nComputer guessed {rights_count} out of {len(test_str)-3} symbols right ({round(acc,2)} %)')
    balance = balance-(rights_count-wrongs_count)
    print(f'Your balance is now ${balance}')

