import random, time
import cv2
from keras.models import load_model
import numpy as np
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)


class RPS:
  def __init__(self):
    self.user_score = 0
    self.computer_score = 0

    self.choices = ['rock', 'paper', 'scissors', 'nothing']

  def get_prediction(self):
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image 
    cv2.imshow('frame', frame)
    max_index = np.argmax(model.predict(data))
    user_choice = self.choices[max_index]
    print(f'User chose {user_choice}')
    return user_choice

  def get_computer_choice(self):
      # return random.randint(0,2)
      comp_choice = random.choice(self.choices[0:3])
      print(f'Computer chose {comp_choice}')
      return comp_choice

  def get_winner(self, comp_choice, user_choice):
    if user_choice == 'nothing':
      print('\nPlease do a gesture...\n')
    elif comp_choice == user_choice:
      return 'tie'
    elif (comp_choice == 'rock' and user_choice == 'paper') or (comp_choice == 'paper' and user_choice == 'scissors') or (comp_choice == 'scissors' and user_choice == 'rock'):
      return 'user'
    else:
      return 'computer'

  def countdown(self, msgs):
    for x in msgs:
      print(x)
      time.sleep(0.7)
    print('Shoot!\n')
    time.sleep(0.2)

  def start_game(self):
    start_game = input('Enter "y" to start the game : ')
    if start_game == 'y':
      self.game()

  def game(self):
    self.countdown(['\nRock', 'Paper', 'Scissors'])
    
    user_gesture = self.get_prediction()
    computer_gesture = self.get_computer_choice()

    winner = self.get_winner(computer_gesture, user_gesture)
    if winner == 'user':
      print('\nUser wins!\n')
      self.user_score += 1
    if winner == 'computer':
      print('\nComputer wins!\n')
      self.computer_score += 1
    if winner == 'draw':
      print('\nDraw!\n')
    print(f'Computer : {self.computer_score}, User : {self.user_score}\n')

def play_game():
  game = RPS()

  while game.computer_score < 3 and game.user_score < 3:
    game.start_game()
  if game.computer_score == 3:
    print('Game over : Computer wins!')
  else:
    print('Game over : User wins!')

if __name__ == '__main__':
  play_game()

