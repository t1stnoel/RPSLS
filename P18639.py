import random
from RPSLS_player import RPSLS_player

class P18639(RPSLS_player):
  def __init__(self):
    pass
  def shoot(self):
    return random.choice(('rock', 'paper', 'scissors', 'lizard', 'spock'))
  
  def update(self, result: str, competitor_shot: str):
    pass