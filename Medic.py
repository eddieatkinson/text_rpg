from random import randint
from Character import Character

# Make a subclass.
class Medic(Character):
	def __init__(self):
		super(Medic, self).__init__("Medic", 10, 3, 4, """
              _|/
            ."   ".
        __ /(o)-(o)\\
      /_)||   /     |
      |_)||  '-     |     
      \_)|| '.___.' /   |\/|_
       | / \  \_/  /   _|  '/
       |--\ '.___.'    \ ) /
       \   \_/\__/\__   |==|
        \    \ /\ /\ `\ |  |
         \    \\//     \|  |
          `\   /\   |  /   |
            ;  ||   |\____/
            |  ||   |     

			""")
	def recuperate(self):
		recup_assign = randint(1, 10)
		if recup_assign > 8: # Will regain 2 health points with probability 20%
			self.health += 2
			print "That resourceful %s has regained 2 health!" % self.name


