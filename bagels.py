from random import randint

max_try = 10


def start_game():
    a = (
        '*** GAME OF BAGELS ********************************************************\n'
        '*                                                                         *\n'
        '*  I am thinking of a 3-digit number. Try to guess what it is.            *\n'
        '*  Here are some clues:                                                   *\n'
        '*  When I say:    That means:                                             *\n'
        '*  Pico         One digit is correct but in the wrong position.           *\n'
        '*  Fermi        One digit is correct and in the right position.           *\n'
        '*  Bagels       No digit is correct.                                      *\n'
        '*                                                                         *\n'
        '*  I have thought up a 3-digit number.                                    *\n'
        '*  You have 10 guesses to get it right.                                   *\n'
        '*                                                                         *\n'
        '***************************************************************************'
    )
    return a
print(start_game())


def getSecretNum():
    while True:
        player_number = input("Enter a number: ")
        if not player_number.isdigit() or len(player_number) != 3:
            print("Enter three integers without spaces!")
        else:
            break

    return list(map(int, player_number))


def main():

    wrong_place = "Pico"
    right_place = "Fermi"
    wrong = "Bagels"
    numtry = 1
    target_num = [randint(1, 5), randint(1, 5), randint(1, 5)]
    print(target_num)
    while numtry <= max_try:
        print(f"try №{numtry}: ")
        player_number = getSecretNum()
        numtry += 1
        answer = []


        for i in range(3):

            if target_num[i] == player_number[i]:
                answer.append(right_place)
            elif player_number[i] in target_num:
                answer.append(wrong_place)


        if len(answer) == 0:
            answer.append(wrong)

        print(answer)


        if target_num == player_number:
            print('Congratulations! You have won!')
            break


    response = input("Do you want to play again? Yes or No: ").upper()
    if response == "YES":
        start_next = start_game()
        print(start_next)
        main()
    else:
        print(f"Thank you! The number that was asked was: {target_num}")
        return

main()