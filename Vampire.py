# Get the super.
from Character import Character

# Make a subclass.
class Vampire(Character):
	def __init__(self):
		super(Vampire, self).__init__("Vampire", 15, 1, 3)
		# self.name = "Vampire"
		# self.health = 6
		# self.power = 2
		self.image = """
                     __.......__
                  .-:::::::::::::-.
                .:::''':::::::''':::.
              .:::'     `:::'     `:::. 
         .'\  ::'   ^^^  `:'  ^^^   '::  /`.
        :   \ ::   _.__       __._   :: /   ;
       :     \`: .' ___\     /___ `. :'/     ; 
      :       /\   (_|_)\   /(_|_)   /\       ;
      :      / .\   __.' ) ( `.__   /. \      ;
      :      \ (        {   }        ) /      ; 
       :      `-(     .  ^"^  .     )-'      ;
        `.       \  .'<`-._.-'>'.  /       .'
          `.      \    \;`.';/    /      .'
            `._    `-._       _.-'    _.'
             .'`-.__ .'`-._.-'`. __.-'`.
           .'       `.         .'       `.
         .'           `-.   .-'           `.
"""
	# def take_damage(self, amount_of_damage):
	# 	self.health -= amount_of_damage
	# def is_alive(self):
	# 	return self.health > 0
	def reduce_strength(self, power_decrease):
		self.power -= power_decrease
