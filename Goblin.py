class Goblin(object):
	def __init__(self):
		self.name = "Goblin"
		self.health = 6
		self.power = 2
	def take_damage(self, amount_of_damage):
		self.health -= amount_of_damage