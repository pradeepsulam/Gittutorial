# This is a tic toc game, with two uses
# Global Variables declaration.

import random

tic_toc_list = random.sample(range(1, 10), 9)


def printing_tic_toc(input_list):
    k = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if j is not 2:
                print("  " + input_list[k] + "  |", end=" ")
            else:
                print(" " + input_list[k] + " ", end=" ")
            k += 1
        if i is not 2:
            print("\n-----------------")


def tic_toc_main():
    person1_symbol = input("Player 1 : Choose which one you want X or O :").upper()
    if person1_symbol != ('X' or 'O'):
        person1_symbol = input("Player 1 : Re-Choose which one you want X or O :").upper()
    if person1_symbol == 'X':
        person2_symbol = 'O'
    else:
        person2_symbol = 'X'
    person_tic_toc_values = []
    # Looping for 9/2 == 5 times
    for loop_counter in range(1, 6):
        person1_input = int(input("\nPerson 1 Enter your number - (1 - 9) : "))
        while (person1_input not in tic_toc_list) or (person1_input in person_tic_toc_values):
            person1_input = int(
                input('"Invalid number or already entered number" Person 1 Re-Enter your number - (1 - 9) : '))
        number_index = tic_toc_list.index(person1_input)
        person_tic_toc_list[number_index] = person1_symbol
        person_tic_toc_values.append(person1_input)
        printing_tic_toc(person_tic_toc_list)
        if (person_tic_toc_list[0] == person1_symbol and person_tic_toc_list[1] == person1_symbol and
            person_tic_toc_list[2] == person1_symbol) or (
                person_tic_toc_list[3] == person1_symbol and person_tic_toc_list[4] == person1_symbol and
                person_tic_toc_list[5] == person1_symbol) or (
                person_tic_toc_list[6] == person1_symbol and person_tic_toc_list[7] == person1_symbol and
                person_tic_toc_list[8] == person1_symbol) or (
                person_tic_toc_list[0] == person1_symbol and person_tic_toc_list[4] == person1_symbol and
                person_tic_toc_list[8] == person1_symbol) or (
                person_tic_toc_list[2] == person1_symbol and person_tic_toc_list[4] == person1_symbol and
                person_tic_toc_list[6] == person1_symbol) or (
                person_tic_toc_list[0] == person1_symbol and person_tic_toc_list[3] == person1_symbol and
                person_tic_toc_list[6] == person1_symbol) or (
                person_tic_toc_list[1] == person1_symbol and person_tic_toc_list[4] == person1_symbol and
                person_tic_toc_list[7] == person1_symbol) or (
                person_tic_toc_list[2] == person1_symbol and person_tic_toc_list[5] == person1_symbol and
                person_tic_toc_list[8] == person1_symbol):
            print("\nPerson 1 Won the Game")
            break
        if loop_counter == 5:
            print("\nNon of you won the game, Please play try-again :)")
            break
        person2_input = int(input("\nPerson 2 Enter your number - (1 - 9) : "))
        while (person2_input not in tic_toc_list) or (person2_input in person_tic_toc_values):
            person2_input = int(
                input("\n'Invalid number or Already entered input' Person 2 Re-Enter your number - (1 - 9) : "))
        person_tic_toc_values.append(person2_input)
        number_index = tic_toc_list.index(person2_input)
        person_tic_toc_list[number_index] = person2_symbol
        printing_tic_toc(person_tic_toc_list)
        if (person_tic_toc_list[0] == person2_symbol and person_tic_toc_list[1] == person2_symbol and
            person_tic_toc_list[2] == person2_symbol) or (
                person_tic_toc_list[3] == person2_symbol and person_tic_toc_list[4] == person2_symbol and
                person_tic_toc_list[5] == person2_symbol) or (
                person_tic_toc_list[6] == person2_symbol and person_tic_toc_list[7] == person2_symbol and
                person_tic_toc_list[8] == person2_symbol) or (
                person_tic_toc_list[0] == person2_symbol and person_tic_toc_list[4] == person2_symbol and
                person_tic_toc_list[8] == person2_symbol) or (
                person_tic_toc_list[2] == person2_symbol and person_tic_toc_list[4] == person2_symbol and
                person_tic_toc_list[6] == person2_symbol) or (
                person_tic_toc_list[0] == person2_symbol and person_tic_toc_list[3] == person2_symbol and
                person_tic_toc_list[6] == person2_symbol) or (
                person_tic_toc_list[1] == person2_symbol and person_tic_toc_list[4] == person2_symbol and
                person_tic_toc_list[7] == person2_symbol) or (
                person_tic_toc_list[2] == person2_symbol and person_tic_toc_list[5] == person2_symbol and
                person_tic_toc_list[8] == person2_symbol):
            print("\nPerson 2 Won the Game")
            break


while 1:
    person_tic_toc_list = ['', '', '', '', '', '', '', '', '']
    game_state = input("Do you guys want to  play y or n : ").upper()
    if game_state == 'Y':
        tic_toc_main()
    elif game_state == 'N':
        break
    else:
        print("Invalid input \n Please re-enter correct input")
