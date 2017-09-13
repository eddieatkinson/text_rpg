class Vampire(object):
	def __init__(self):
		self.name = "Vampire"
		self.health = 6
		self.power = 2
	def take_damage(self, amount_of_damage):
		self.health -= amount_of_damage
	def is_alive(self):
		return self.health > 0