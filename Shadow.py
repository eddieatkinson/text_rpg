from random import randint
from Character import Character

# Make a subclass.
class Shadow(Character):
    def __init__(self):
        super(Shadow, self).__init__("Shadow", 1, 1, 5, """
                .#####.                
                |_____|                
               (\#/ \#/)               
                |  U  |                
                \  _  /                
                 \___/                 
             .---'   `---.             
            /  #########  \\            
           /  |####|####|  \\           
          /  /\ ####### /\  \\          
         (  \  \  ###  /  /  )         
          \  \  \_###_/  /  /          
           \  \ |\   /| /  /           
            'uuu| \_/ |uuu'            
                |  |  |                
                |  |  |                
                |  |  |                
                |  |  |                
                |  |  |                
                )  |  (                
              .oooO Oooo.  
			""")
    def take_damage(self, amount_of_damage):
        rand_pwr_assign = randint(1, 10)
        if rand_pwr_assign > 9: # Damage will only occur with 20% probability.
            print "You attacked! The %s has received %s damage." % (self.name, amount_of_damage)
            self.health -= amount_of_damage
        else:
            print "%s has evaded your attack!" % self.name