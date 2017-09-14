class Sword(object):
	def __init__(self):
		self.name = "sword"
		self.power_boost = 3
		self.price = 4
		self.image = """
  ,.
  \%`.
   `.%`.
     `.%`.
       `.%`.
         `.%`.
           `.%`.    __
             `.%`.  \ \\
               `.%`./_/
                 `./ /.
                __/\/:/;.
                \__/  `:/;.
                        `:/;.,    
                          `:/ ;
                            `'
"""

class Shield(object):
	def __init__(self):
		self.name = "shield"
		self.enemy_power_decrease = 1
		self.price = 6
		self.image = """\_              _/
] --__________-- [
|       ||       |
\       ||       /
 [      ||      ]
 |______||______|
 |------..------|
 ]      ||      [
  \     ||     /
   [    ||    ]
   \    ||    /
    [   ||   ]
     \__||__/
        --"""

class Potion(object):
	def __init__(self):
		self.name = "potion"
		self.health_boost = 2
		self.price = 5
		self.image = """     `.___,'
      (___)
      <   >
       ) (
      /`-.\\
     /     \\
    / _    _\\
   :,' `-.' `:
   |         |
   :         ;
    \       /
     `.___.'"""