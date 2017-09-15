# Get the super class.
from Character import Character

# Make Goblin a subclass of Character.
class Goblin(Character):
    def __init__(self):
        super(Goblin, self).__init__('Goblin', 6, 2, 2, """
           .:\:/:.
         .:\:\:/:/:.
        :.:\:\:/:/:.:
       :=.' -   - '.=:
       '=(\ 9   9 /)='
          (  (_)  )
          /`-vvv-'\\
         /         \\
        / /|,,,,,|\ \\
       /_//  /^\  \\\_\\
       WW(  (   )  )WW
        __\,,\ /,,/__
       (______Y______)
            """)