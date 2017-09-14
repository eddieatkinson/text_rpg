from Items import Items

class Sword(Items):
	def __init__(self):
		super(Sword, self).__init__("sword", 4, """
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
""")
		self.power_boost = 3