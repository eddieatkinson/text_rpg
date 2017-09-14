# Contrib modules
# Core
import os
from random import randint
# 3rd party (we don't have any)
# pygame, for example

#Custom modules (we write these)
from Hero import Hero # We made this! File named 'Hero', class 'Hero' within.
from Goblin import Goblin # We made this, too!
from Vampire import Vampire
from Medic import Medic
from Shadow import Shadow
from Zombie import Zombie
from Wizard import Wizard
from Dragon import Dragon
from Sword import Sword
from Shield import Shield
from Potion import Potion

# Now we instantiate a hero object from the Hero class:
the_hero = Hero()
level = 1 # We start on this level.

# Make a list to hold our monsters.
monsters = []

# These are your items.
sword = Sword()
shield = Shield()
potion = Potion()

def monster_attack():
# Goblins turn to attack!! (Only if he's still alive)
	if monster.is_alive():
		monster.print_image()
		# Just like the goblin, the hero should be changing its own stuff.
		# So... call take_damage on the hero.
		the_hero.take_damage(monster.power)
		print "The %s hit you for %d damage!" % (monster.name, monster.power)
		# Goblin has attacked. Now check to see if hero is still alive.
		if not the_hero.is_alive():
			print "You have been killed by the weak %s. Shame on you!" % monster.name
		#if monster.name == "Medic":
		monster.recuperate()
		monster.special_pwr()
	else:
		print "You have defeated the %s! You receive %s coins!" % (monster.name, monster.loot)
		the_hero.collect_loot(monster.loot)

def round_down(number, divisor):
	return number - (number % divisor)
# Ask user for his/her name.
print "What is thy name, brave adventurer?"
the_hero.name = raw_input("> ")
the_hero.cheer_for_hero()

print "How many monsters are you willing to fight, brave %s?" % the_hero.name
number_of_enemies = int(raw_input("> "))

def monster_gen():
	for i in range(0, number_of_enemies):
		rand_num = randint(0, 1)
		if rand_num == 0:
			monsters.append(Goblin())
		else:
			monsters.append(Vampire())

def monster_gen2():
	for i in range(0, number_of_enemies):
		rand_num = randint(0, 1)
		if rand_num == 0:
			monsters.append(Medic())
		else:
			monsters.append(Shadow())

def monster_gen3():
	for i in range(0, number_of_enemies):
		rand_num = randint(0, 2)
		if rand_num == 0:
			monsters.append(Zombie())
		elif rand_num == 1:
			monsters.append(Wizard())
		else:
			monsters.append(Dragon())

monster_gen()

# print monsters

# We need to loop through all of the monsters.
for monster in monsters:
	# Run the game as long as BOTH characters have health (are alive)
	while monster.is_alive() and the_hero.is_alive() and level < 4:
		# game is on!
		print "You have %d health and %d power." % (the_hero.health, the_hero.power)
		print "The %s has %d health and %d power." % (monster.name, monster.health, monster.power)
		# print "%s" % monster.image
		print "What do you want to do?"
		print "1. fight %s" % monster.name
		print "2. do nothing"
		print "3. flee"
		print "4. go to the store"
		user_input = raw_input("> ")
		if user_input == "1":
			# User has chosen to attack.
			# Take away health from the goblin based on hero power.
			# The Goblin class should be managing the goblin's health.
			# The hero is going to do the_hero.power damage to the goblin.
			monster.take_damage(the_hero.power)
			monster_attack()
			brave = True
		elif user_input == "2":
			# Hero is going to stand there like an idiot
			monster_attack()
			brave = True
		elif user_input == "3":
			print "You coward! You remind me of my ex-wife."
			brave = False
			# Call break to end the while loop.
			break
		elif user_input == "4":
			if the_hero.coins < sword.price:
				print "You do not have enough coins to purchase anything, %s." % the_hero.name
			else:
				print "What would you like to purchase, %s? You have %s coins remaining." % (the_hero.name, the_hero.coins)
				print "1. A %s for %s coins. This will increase your power by %s." % (sword.name, sword.price, sword.power_boost)
				print "2. A %s for %s coins. This will reduce your enemy's damage by %s." % (shield.name, shield.price, shield.enemy_power_decrease)
				print "3. A %s for %s coins. This will increase your health by %s." % (potion.name, potion.price, potion.health_boost)
				item_input = raw_input("> ")
				if item_input == "1":
					if sword.price > the_hero.coins:
						print "You do not have enough coins for that!"
					else:
						sword.print_image()
						print "Excellent choice! You are more powerful now!"
						the_hero.boost_power(sword.power_boost)
						the_hero.spend_coins(sword.price)
				elif item_input == "2":
					if shield.price > the_hero.coins:
						print "You do not have enough coins for that!"
					elif monster.power <= shield.enemy_power_decrease:
						print "The %s is too weak for your %s!" % (monster.name, shield.name)
					else:
						shield.print_image()
						print "Excellent choice! You are less prone to damage now!"
						monster.reduce_strength(shield.enemy_power_decrease)
						the_hero.spend_coins(shield.price)
				elif item_input == "3":
					if potion.price > the_hero.coins:
						print "You do not have enough coins for that!"
					else:
						potion.print_image()
						print "Excellent choice! You are have greater health now!"
						the_hero.boost_health(potion.health_boost)
						the_hero.spend_coins(potion.price)
				else:
					print "Invalid input %s" % user_input

		else:
			print "Invalid input %s" % user_input
		if the_hero.coins >=20 and round_down(the_hero.coins, 10) / (10 * (level + 1)) == 1:
			print ""
			print "*" * 45
			print "* Congratulations! You have passed Level %s! *" % level
			print "*" * 45
			level += 1
			if level > 3:
				print "You have achieved the highest level, %s! You have won!" % the_hero.name
				brave = False
			else:
				print "\nYou will receive 5 health!\n"
				print "..."
				print "...and some new MONSTERS!"
				the_hero.boost_health(5)
			if level == 2:
				monster_gen2()
			elif level == 3:
				monster_gen3()
if brave:
	print "You have killed all of your enemies! Well done, skilled %s!" % the_hero.name
