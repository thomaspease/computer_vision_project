import random

def play():
  def get_choice():
    ''' 
    Returns a random integer between 0 - 2, which pertain to the different choices in the game
    - 0 = rock
    - 1 = paper 
    - 2 = scissors
    '''
    return random.randint(0,2)

  def get_winner(comp_choice, user_choice):
    '''
    Performs the game logic, returning the winner based on the classic rules of RPS.
    Returns
    -----------
    0 = draw
    1 = user wins
    2 = computer wins
    '''
    if comp_choice - user_choice == -1 or comp_choice - user_choice == 2:
      return 1 #user
    elif comp_choice - user_choice == -2 or comp_choice - user_choice == 1:
      return 2 #computer
    else:
      return 0 #draw

  return get_winner(get_choice(), get_choice())

result = play()
print(result)
