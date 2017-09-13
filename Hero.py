class Hero(object):
	def __init__(self, name = "Ingognito"): # In case we aren't passed a name.
		# Set up the object to remember it's name.
		self.name = name
		self.health = 10
		self.power = 5
	def take_damage(self, amount_of_damage):
		self.health -= amount_of_damage
	def cheer_for_hero(self):
		print "Fight hard, valient %s!" % self.name
	def is_alive(self):
		return self.health > 0