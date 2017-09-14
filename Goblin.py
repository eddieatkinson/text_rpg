# Get the super class.
from Character import Character

# Make Goblin a subclass of Character.
class Goblin(Character):
    def __init__(self):
        super(Goblin, self).__init__('Goblin', 6, 1, 3)
        self.image = """
           .:\:/:.
         .:\:\:/:/:.
        :.:\:\:/:/:.:
       :=.' -   - '.=:
       '=(\ 9   9 /)='
          (  (_)  )
          /`-vvv-'\\
         /         \\
        / /|,,,,,|\ \\
       /_//  /^\  \\\_\\
       WW(  (   )  )WW
        __\,,\ /,,/__
       (______Y______)
   """
	# def take_damage(self, amount_of_damage):
	# 	self.health -= amount_of_damage
	# def is_alive(self):
	# 	return self.health > 0
    def reduce_strength(self, power_decrease):
        self.power -= power_decrease