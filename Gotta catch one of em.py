# ----------------functions -------------------
# rules
# main menu
# update_pokemon_file
# show current pokemon
# level up 
# get pokemon info
# candy # generator
# -----------------main code -------------------
# starting menu

import random
right_number = random.randint(100, 999)
digit_one = right_number % 10
number_one = right_number // 10
digit_two = number_one % 10
digit_three = number_one // 10
guess = 0
digit_three_check = 0
digit_two_check = 0
digit_one_check = 0
count = -1
while guess != right_number and count < 10:
    count += 1
    guess = int(input('Please guess a three digit number: '))
    guess_digit_one = guess % 10
    guess_number_one = guess // 10
    guess_digit_two = guess_number_one % 10
    guess_digit_three = guess_number_one // 10
    if guess_digit_three == digit_three:
        output_digit_three = 'O'
        digit_three_check = 1
    else: output_digit_three = 'X'
    if guess_digit_two == digit_two:
        output_digit_two = 'O'
        digit_two_check = 1
    else: output_digit_two = 'X'
    if guess_digit_one == digit_one:
        output_digit_one = 'O'
        digit_one_check = 1
    else: output_digit_one = 'X'
    if (guess_digit_three == digit_two or guess_digit_three == digit_one) and digit_three_check == 0:
        output_digit_three = 'C'
    if (guess_digit_two == digit_three or guess_digit_two == digit_one) and digit_two_check == 0:
        output_digit_two = 'C'
    if (guess_digit_one == digit_two or guess_digit_one == digit_three) and digit_one_check == 0:
        output_digit_one = 'C'
    print(output_digit_three + output_digit_two + output_digit_one)
    print('An X means the number is not in the number, a C means the number is in the wrong place, a O means the number'
          'is in the correct place.')
    digit_three_check = 0
    digit_two_check = 0
    digit_one_check = 0
if count < 10:
    print('Got it!')
else: print('It got away.')
