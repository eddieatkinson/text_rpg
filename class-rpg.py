import os

from Hero import Hero # We made this module! File 'Hero', class 'Hero' within.
from Goblin import Goblin # We made this, too!
from Vampire import Vampire
from random import randint

# Now we instantiate a hero object from the Hero class:
the_hero = Hero()
# Ditto
a_goblin = Goblin()
a_vampire = Vampire()

# Make a list to hold our monsters.
monsters = []

# Ask user for his/her name.
print "What is thy name, brave adventurer?"
the_hero.name = raw_input("> ")
the_hero.cheer_for_hero()

print "How many monsters are you willing to fight, brave %s?" % the_hero.name
number_of_enemies = int(raw_input("> "))

for i in range(0, number_of_enemies):
	rand_num = randint(0, 1)
	if rand_num == 1:
		monsters.append(Goblin())
	else:
		monsters.append(Vampire())

print monsters

# We need to loop through all of the monsters.
for monster in monsters:
	# Run the game as long as BOTH characters have health (are alive)
	while monster.is_alive() and the_hero.is_alive():
		# game is on!
		os.system("clear")
		print "You have %d health and %d power." % (the_hero.health, the_hero.power)
		print "The %s has %d health and %d power." % (monster.name, monster.health, monster.power)
		print "What do you want to do?"
		print "1. fight %s" % monster.name
		print "2. do nothing"
		print "3. flee"
		print "> "
		user_input = raw_input()
		if user_input == "1":
			# User has chosen to attack.
			# Take away health from the goblin based on hero power.
			# The Goblin class should be managing the goblin's health.
			# The hero is going to do the_hero.power damage to the goblin.
			monster.take_damage(the_hero.power)
		elif user_input == "2":
			# Hero is going to stand there like an idiot
			pass
		elif user_input == "3":
			print "Goodbye, coward! You remind me of Goober."
			# Call break to end the while loop.
			break
		else:
			print "Invalid input %s" % user_input

		# Goblins turn to attack!! (Only if he's still alive)
		if monster.health > 0:
			# Just like the goblin, the hero should be changing its own stuff.
			# So... call take_damage on the hero.
			the_hero.take_damage(monster.power)
			print "The %s hit you for %d damage!" % (monster.name, monster.power)
			# Goblin has attacked. Now check to see if hero is still alive.
			if the_hero.health <= 0:
				print "You have been killed by the weak %s. Shame on you!" % monster.name