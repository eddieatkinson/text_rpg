from random import randint
from Character import Character

# Make a subclass.
class Wizard(Character):
    def __init__(self):
        super(Wizard, self).__init__("Wizard", 20, 3, 6, """
                //
                //
              _ //
           .' . // '.
          '_ '_\/_'  `_
          .  .\\\ .  .
         .==. `\\\ .'
  .\|   //bd\\\  \,
  \_'`._\\\__//_.'`.;
    `.__      __,' \\
        |    |      \\
        |    |       `
        |    |
        |    |
        |____|
       =='  '==

			""")
    def special_pwr(self): # Wizard has a 20% probability of power-up spell.
        spell_rnd = randint(1, 10)
        if spell_rnd > 8:
            self.power += 2
            print "%s has performed a power-up spell. He now has %s power!" % (self.name, self.power)
            

