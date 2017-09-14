# This is our super (parent) class. All other characters will be
# subclasses (children) of this class.
class Character(object):
	def __init__(self, name, health, power, loot):
		self.name = name
		self.health = health
		self.power = power
		self.loot = loot
	def take_damage(self, amount_of_damage):
		self.health -= amount_of_damage
	def is_alive(self):
		return self.health > 0
	def print_image(self):
		print self.image