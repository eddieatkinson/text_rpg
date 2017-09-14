class Items(object):
	def __init__(self, name, price, image):
		self.name = name
		self.price = price
		self.image = image
	def print_image(self):
		print self.image
		