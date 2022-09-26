# Computer vision project - Rock paper scissors

## Milestone 2

Using Google's 'Teachable machine' (https://teachablemachine.withgoogle.com/) I trained a model which recognises the gestures 'rock', 'paper', 'scissors' and 'nothing'. This was then downloaded for use with Tensorflow.

## Milestone 3

The bulk of this milestone was to set up a conda environment for the project. It was necessary to install OpenCV (an open source computer vision lib), Tensorflow (which will be used to make predictions based on the trained model), and ipykernel.

## Milestone 4

This milestone involved the creation of a manual RPS game. A random integer between 0-2, which pertains to the different choices in the game - 0 = rock - 1 = paper - 2 = scissors

Based on the classic rules of RPS, the get_winner function then works out the winner. The game logic was the most challenging part of this milestone. I found that depending on the result of subtracting one player's choice from the other, a winner is produced:

```python
if comp_choice - user_choice == -1 or comp_choice - user_choice == 2:
      return 1 #user
    elif comp_choice - user_choice == -2 or comp_choice - user_choice == 1:
      return 2 #computer
    else:
      return 0 #draw
```

## Milestone 5

For this milestone I built the camera_rps.py game. A choice I made which diverged from the game spec was to have a countdown in the terminal, which uses time.sleep(), and then at the end of the countdown to call a function which captures the user's gesture at that particular moment, rather than using a while True loop, which means that the other gameplay code cannot run at the same time.

I also chose to make the game into a class, which avoided the use of global variables. I switched from the mathematical and int based method of working out the winner for readibility, based on advice from Bola:

```python
def get_winner(self, comp_choice, user_choice):
    if user_choice == 'nothing':
      print('\nPlease do a gesture...\n')
    elif comp_choice == user_choice:
      return 'tie'
    elif (comp_choice == 'rock' and user_choice == 'paper') or (comp_choice == 'paper' and user_choice == 'scissors') or (comp_choice == 'scissors' and user_choice == 'rock'):
      return 'user'
    else:
      return 'computer'
```

[Gameplay] (/gameplay.png)
