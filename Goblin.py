class Goblin(object):
	def __init__(self):
		self.name = "Goblin"
		self.health = 6
		self.power = 2
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
	def take_damage(self, amount_of_damage):
		self.health -= amount_of_damage
	def is_alive(self):
		return self.health > 0
	def reduce_strength(self, power_decrease):
		self.power -= power_decrease