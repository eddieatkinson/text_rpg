from random import randint
from Character import Character

# Make a subclass.
class Dragon(Character):
    def __init__(self):
        super(Dragon, self).__init__("Dragon", 20, 3, 6, """
           .     _///_,
         .      / ` ' '>
           )   o'  __/_'>
          (   /  _/  )_\'>
           ' "__/   /_/\_>
               ____/_/_/_/
              /,---, _/ /
             ""  /_/_/_/
                /_(_(_(_                 \
               (   \_\_\\_               )\
                \'__\_\_\_\__            ).\
                //____|___\__)           )_/
                |  _  \'___'_(           /'
                 \_ (-'\'___'_\      __,'_'
                 __) \  \\___(_   __/.__,'
       b'ger  ,((,-,__\  '", __\_/. __,'
                           '"./_._._-'
            """)
   # def special_pwr(self):
