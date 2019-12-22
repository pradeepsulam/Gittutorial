# This is a tic toc game, with two uses
# Global Variables declaration.

import random

tic_toc_list = random.sample(range(1, 10), 9)


def printing_tic_toc(input_list):
    k = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if j is not 2:
                print(f"  {input_list[k]}  |", end=" ")
            else:
                print(f" {input_list[k]} ", end=" ")
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
    while 1:
        person1_input = int(input("\nPerson 1 Enter your number - (1 - 9) : "))
        if person1_input not in tic_toc_list:
            print("Invalid number")
            person1_input = int(input('Person 1 Re-Enter your number - (1 - 9) : '))
        number_index = tic_toc_list.index(person1_input)
        person1_Tic_Toc_List[number_index] = person1_symbol
        printing_tic_toc(person1_Tic_Toc_List)
        if (person1_Tic_Toc_List[0] == person1_symbol and person1_Tic_Toc_List[1] == person1_symbol and
            person1_Tic_Toc_List[2] == person1_symbol) or (
                person1_Tic_Toc_List[3] == person1_symbol and person1_Tic_Toc_List[4] == person1_symbol and
                person1_Tic_Toc_List[5] == person1_symbol) or (
                person1_Tic_Toc_List[6] == person1_symbol and person1_Tic_Toc_List[7] == person1_symbol and
                person1_Tic_Toc_List[8] == person1_symbol) or (
                person1_Tic_Toc_List[0] == person1_symbol and person1_Tic_Toc_List[4] == person1_symbol and
                person1_Tic_Toc_List[8] == person1_symbol) or (
                person1_Tic_Toc_List[2] == person1_symbol and person1_Tic_Toc_List[4] == person1_symbol and
                person1_Tic_Toc_List[6] == person1_symbol) or (
                person1_Tic_Toc_List[0] == person1_symbol and person1_Tic_Toc_List[3] == person1_symbol and
                person1_Tic_Toc_List[6] == person1_symbol) or (
                person1_Tic_Toc_List[1] == person1_symbol and person1_Tic_Toc_List[4] == person1_symbol and
                person1_Tic_Toc_List[7] == person1_symbol) or (
                person1_Tic_Toc_List[2] == person1_symbol and person1_Tic_Toc_List[5] == person1_symbol and
                person1_Tic_Toc_List[8] == person1_symbol):
            print("\nPerson 1 Won the Game")
            break
        person2_input = int(input("\nPerson 2 Enter your number - (1 - 9) : "))
        if person2_input not in tic_toc_list:
            print("Invalid number")
            person2_input = int(input("\nPerson 2 Re-Enter your number - (1 - 9) : "))
        number_index = tic_toc_list.index(person2_input)
        person2_Tic_Toc_List[number_index] = person2_symbol
        printing_tic_toc(person2_Tic_Toc_List)
        if (person2_Tic_Toc_List[0] == person2_symbol and person2_Tic_Toc_List[1] == person2_symbol and
            person2_Tic_Toc_List[2] == person2_symbol) or (
                person2_Tic_Toc_List[3] == person2_symbol and person2_Tic_Toc_List[4] == person2_symbol and
                person2_Tic_Toc_List[5] == person2_symbol) or (
                person2_Tic_Toc_List[6] == person2_symbol and person2_Tic_Toc_List[7] == person2_symbol and
                person2_Tic_Toc_List[8] == person2_symbol) or (
                person2_Tic_Toc_List[0] == person2_symbol and person2_Tic_Toc_List[4] == person2_symbol and
                person2_Tic_Toc_List[8] == person2_symbol) or (
                person2_Tic_Toc_List[2] == person2_symbol and person2_Tic_Toc_List[4] == person2_symbol and
                person2_Tic_Toc_List[6] == person2_symbol) or (
                person2_Tic_Toc_List[0] == person2_symbol and person2_Tic_Toc_List[3] == person2_symbol and
                person2_Tic_Toc_List[6] == person2_symbol) or (
                person2_Tic_Toc_List[1] == person2_symbol and person2_Tic_Toc_List[4] == person2_symbol and
                person2_Tic_Toc_List[7] == person2_symbol) or (
                person2_Tic_Toc_List[2] == person2_symbol and person2_Tic_Toc_List[5] == person2_symbol and
                person2_Tic_Toc_List[8] == person2_symbol):
            print("\nPerson 2 Won the Game")
            break


while 1:
    person1_Tic_Toc_List = ['', '', '', '', '', '', '', '', '']
    person2_Tic_Toc_List = ['', '', '', '', '', '', '', '', '']
    game_state = input("Do you guys want to  bvf play y or n : ").upper()
    if game_state == 'Y':
        tic_toc_main()
    elif game_state == 'N':
        break
    else:
        print("Invalid input \n Please re-enter correct input")
