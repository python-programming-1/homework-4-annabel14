#rock paper scissors

import random
computer_move_text = 'a'
user_score = 0
computer_score = 0
while True:
    computer_move = random.randint(1,3)
    user_move = input ("Make a move! (r/p/s)")
    if user_move == 'sc':
        print("human: " + str(user_score) + ", computer: " + str(computer_score))
        user_move = input ("Make a move! (r/p/s)")
    if computer_move == 1:
        computer_move_text = 'r'
    elif computer_move == 2:
        computer_move_text = 'p'
    else:
        computer_move_text = 's'
    while user_move == 'r':
        if computer_move_text == 'r':
            print ("You chose rock and the computer chose rock. It's a draw!")
            break
        elif computer_move_text == 'p':
            print ("You chose rock and the computer chose paper. You lose!")
            computer_score+=1
            break
        elif computer_move_text == 's':
            print ("You chose rock and the computer chose scissors. You win!")
            user_score+=1
            break
    while user_move == 's':
        if computer_move_text == 'r':
            print ("You chose scissors and the computer chose rock. You lose!")
            computer_score+=1
            break
        elif computer_move_text == 'p':
            print ("You chose scissors and the computer chose paper. You win!")
            user_score+=1
            break
        elif computer_move_text == 's':
            print ("You chose scissors and the computer chose scissors. It's a draw!")
            break
    while user_move == 'p':
        if computer_move_text == 'r':
            print ("You chose paper and the computer chose rock. You win!")
            user_score+=1
            break
        elif computer_move_text == 'p':
            print ("You chose paper and the computer chose paper. It's a draw!")
            break
        elif computer_move_text == 's':
            print ("You chose paper and the computer chose scissors. You lose!")
            computer_score+=1
            break
    play_again = input ("Do you want to play again? y/n ")
    if play_again == 'sc':
        print("human: " + str(user_score) + ", computer: " + str(computer_score))
        play_again = input ("Do you want to play again? y/n ")
        if play_again == 'n' or play_again == 'N':
            print ("Thanks, bye!")
            break
    elif play_again == 'y' or play_again == 'Y':
        True
    elif play_again == 'n' or play_again == 'N':
        print ("Thanks, bye!")
        break