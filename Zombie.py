from random import randint
from Character import Character

# Make a subclass.
class Zombie(Character):
    def __init__(self):
        super(Zombie, self).__init__("Zombie", 4, 4, 5, """
                    (()))
                   /|x x|
                  /\( - )
          ___.-._/\/
         /=`_'-'-'/  !!
         |-{-_-_-}     !
         (-{-_-_-}    !
          \{_-_-_}   !
           }-_-_-}
           {-_|-_}
           {-_|_-}
           {_-|-_}
           {_-|-_}
       ____%%@ @%%_______
			""")
    def is_alive(self):
        return self.health > -6