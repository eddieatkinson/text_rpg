from Items import Items

class Shield(Items):
	def __init__(self):
		super(Shield, self).__init__("shield", 6, """
\_              _/
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
        --
			""")
		self.enemy_power_decrease = 1