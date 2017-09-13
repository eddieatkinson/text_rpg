import os

from Hero import Hero # We made this module!
from Goblin import Goblin # We made this, too!

# Now we instantiate a hero object from the Hero class:
the_hero = Hero()
# Ditto
a_goblin = Goblin()

# Run the game as long as BOTH characters have health (are alive)
while a_goblin.health > 0 and the_hero.health > 0:
	# game is on!
	os.system("clear")
	print "You have %d health and %d power." % (the_hero.health, the_hero.power)
	print "The goblin has %d health and %d power." % (a_goblin.health, a_goblin.power)
	print "What do you want to do?"
	print "1. fight goblin"
	print "2. do nothing"
	print "3. flee"
	print "> "
	user_input = raw_input()
	if user_input == "1":
		# User has chosen to attack.
		# Take away health from the goblin based on hero power.
		# The Goblin class should be managing the goblin's health.
		# The hero is going to do the_hero.power damage to the goblin.
		a_goblin.take_damage(the_hero.power)
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
	if a_goblin.health > 0:
		# Just like the goblin, the hero should be changing its own stuff.
		# So... call take_damage on the hero.
		the_hero.take_damage(a_goblin.power)
		print "The goblin hit you for %d damage!" % a_goblin.power
		# Goblin has attacked. Now check to see if hero is still alive.
		if the_hero.health <= 0:
			print "You have been killed by the weak goblin. Shame on you!"