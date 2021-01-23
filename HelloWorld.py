class clase :
	a = 1
	def __init__(self):
		self.a = 5
	def suma1(self): 
		"""Esta función se suma a si mismo"""
		self.a+=self.a
	def muestra(self):
		return self.a
	
clase1 = clase()
clase1.suma1()
print(clase1.muestra())

