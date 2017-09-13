# This is a procedural approach to a text-based RPG game.
# The hero is going to fight a goblin.
# The hero will have the option to:
# 1. Fight the goblin.
# 2. Do nothing (the goblin will still attack the hero).
# 3. Run away.

import os # Will allow us to run Linux command in the game.

hero_health = 10
hero_power = 10
goblin_health = 6
goblin_power = 2

# Run the game as long as BOTH characters have health (are alive)
while goblin_health > 0 and hero_health > 0:
	# game is on!
	os.system("clear")
	print "You have %d health and %d power." % (hero_health, hero_power)
	print "The goblin has %d health and %d power." % (goblin_health, goblin_power)
	print "What do you want to do?"
	print "1. fight goblin"
	print "2. do nothing"
	print "3. flee"
	print "> "
	user_input = raw_input()
	if user_input == "1":
		# User has chosen to attack.
		# Take away health from the goblin based on hero power.
		goblin_health -= hero_power
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
	if goblin_health > 0:
		hero_health -= goblin_power
		print "The goblin hit you for %d damage!" % goblin_power
		# Goblin has attacked. Now check to see if hero is still alive.
		if hero_health <= 0:
			print "You have been killed by the weak goblin. Shame on you!"