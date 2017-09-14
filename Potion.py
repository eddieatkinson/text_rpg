from Items import Items

class Potion(Items):
	def __init__(self):
		super(Potion, self).__init__("potion", 5, """
     `.___,'
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
     `.___.'
			""")
		self.health_boost = 2