import random

def get_computer_choice(word_list = ['rock', 'paper', 'scissors']):
    computer_choice = random.choice(word_list)
    return computer_choice

def get_user_choice():
    user_choice = input('Choose rock, paper or scissors: ').lower()
    return user_choice

def get_winner(computer_choice, user_choice):
    #print(f'computer choice: {computer_choice} | user choice: {user_choice}')
    if user_choice == computer_choice:
        print(f"Computer also picked {user_choice}. It's a tie!")
    else:
        if user_choice == "rock":
            if computer_choice == "paper":
                print('Computer picked paper. You lose!')
            else:
                print('Computer picked scissors. You win!')
        elif user_choice == "paper":
            if computer_choice == "rock":
                print('Computer picked rock. You win!')
            else:
                print('Computer picked scissors. You lose!')
        elif user_choice == "scissors":
            if computer_choice == "paper":
                print('Computer picked paper. You win!')
            else:
                print('Computer picked rock. You lose!')
        else:
            print('Input not valid')

def play():
    while True:
        get_winner(get_computer_choice(), get_user_choice())

play()

