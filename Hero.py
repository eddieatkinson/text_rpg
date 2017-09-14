class Hero(object):
	def __init__(self, name = "Ingognito"): # In case we aren't passed a name.
		# Set up the object to remember it's name.
		self.name = name
		self.health = 10
		self.power = 5
		self.coins = 10
	def take_damage(self, amount_of_damage):
		self.health -= amount_of_damage
	def cheer_for_hero(self):
		print "Fight hard, valient %s!" % self.name
	def is_alive(self):
		return self.health > 0
	def spend_coins(self, cost):
		self.coins -= cost
	def boost_health(self, health_boost_amount):
		self.health += health_boost_amount
	def boost_power(self, power_boost_amount):
		self.power += power_boost_amount
	def collect_loot(self, loot_amount):
		self.coins += loot_amount