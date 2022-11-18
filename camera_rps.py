import cv2
from keras.models import load_model
import numpy as np
import time
import random

model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
#i=0
frame = cap.read()


def get_computer_choice(word_list = ['rock', 'paper', 'scissors']):
    computer_choice = random.choice(word_list)
    return computer_choice

def draw_text(frame, text, x, y, color=(255,0,255), thickness=4, size=3):
            if x is not None and y is not None:
                cv2.putText(
                    frame, text, (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, size, color, thickness)

def get_prediction(frame):
    
    while(cap.isOpened()): 
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        cv2.imshow('Rock Paper Scissors', frame)
        #print(f'prediction: {prediction}')

        # Press q to close the window
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
        max_index = np.argmax(prediction)
        #print(f'index of highest number: {max_index}')
        
        if max_index == 0:
            user_choice = 'rock'
            print('You chose rock. Computer chose...')
            
        elif max_index == 1:
            user_choice = 'paper'
            print('You chose paper. Computer chose...')
            
        elif max_index == 2:
            user_choice = 'scissors'
            print('You chose scissors. Computer chose...')
        
        elif max_index == 3:
            user_choice = 'nothing'
        
        t_zero = time.time()        
        while time.time() - t_zero < 5:
            cv2.imshow('Rock Paper Scissors', frame)            
        
        return user_choice
               
    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
      
def get_winner(computer_choice, user_choice):
    #print(f'computer choice: {computer_choice} | user choice: {user_choice}')
        
    if user_choice == computer_choice:
        print(f"{user_choice}. It's a tie!")
    elif user_choice == 'nothing':
            print('Ready? Choose rock, paper or scissors.')
    else:
        if user_choice == "rock":
            if computer_choice == "paper":
                print('paper. You lose!')
                winner = 'computer'
            else:
                print('scissors. You win!')
                winner = 'user'
        elif user_choice == "paper":
            if computer_choice == "rock":
                print('rock. You win!')
                winner = 'user'
            else:
                print('scissors. You lose!')
                winner = 'computer'
        elif user_choice == "scissors":
            if computer_choice == "paper":
                print('paper. You win!')
                winner = 'user'
            else:
                print('rock. You lose!')
                winner = 'computer'
        
        return winner        
    
def play():
    
    computer_wins = 0
    user_wins = 0
    
    while computer_wins < 3 and user_wins < 3:
        overall_winner = get_winner(get_computer_choice(), get_prediction(frame))  
        #print(f'overall_winner variable = {overall_winner}')
        if overall_winner == 'computer':
            computer_wins += 1
        elif overall_winner == 'user':
            user_wins += 1
        else:
            print("No change to the score... Have another go.")
        
        print(f'Computer: {computer_wins} User: {user_wins}\n')
        
    if computer_wins == 3:
        print(f'FINAL SCORE is Computer: {computer_wins} User: {user_wins}\n')
        print("Sorry, you didn't win")
        
    elif user_wins == 3:
        print(f'FINAL SCORE is Computer: {computer_wins} User: {user_wins}\n')
        print("You won!")
            
    else:
        print('Something went wrong')
            

play()
