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

  def get_prediction(self):
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image 
    cv2.imshow('frame', frame)
    return np.argmax(model.predict(data))

  def get_computer_choice(self):
      return random.randint(0,2)

  def get_winner(self, comp_choice, user_choice):
    if user_choice == 3:
      return 2 #computer
    if comp_choice - user_choice == -1 or comp_choice - user_choice == 2:
      return 1 #user
    elif comp_choice - user_choice == -2 or comp_choice - user_choice == 1:
      return 2 #computer
    else:
      return 0 #draw

  def countdown(self, msgs):
    for x in msgs:
      print(x)
      time.sleep(0.7)
    print('Shoot!')
    time.sleep(0.2)

  def print_and_return_choice(self, gesture, player):
    if gesture == 0:
      print(f'{player} chose rock')
    if gesture == 1:
      print(f'{player} chose paper')
    if gesture == 2:
      print(f'{player} chose scissors')
    if gesture == 3:
      print(f"{player} didn't do anything!")
    return gesture


  def start_game(self):
    start_game = input('Enter "y" to start the game : ')
    if start_game == 'y':
      self.game()

  def game(self):
    self.countdown(['Rock', 'Paper', 'Scissors'])
    user_gesture = self.print_and_return_choice(self.get_prediction(), 'User')
    computer_gesture = self.print_and_return_choice(self.get_computer_choice(), 'Computer')
    winner = self.get_winner(computer_gesture, user_gesture)
    if winner == 1:
      print('User wins!')
      self.user_score += 1
    if winner == 2:
      print('Computer wins!')
      self.computer_score += 1
    if winner == 0:
      print('Draw!')
    print(f'Computer : {self.computer_score}, User : {self.user_score}')

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

