import csv 
from pprint import pprint

with open ("owid-covid-data.csv","r") as csv_file:
	csv_reader = csv.reader(csv_file)
	list=list(csv_reader)



class counter_covid:
	"""
		#counter of case covid 
	"""
	list=list

	def __init__(self,*countries):
		if countries is not None:
			if len(countries) == 2:
				self.country1=countries[0]
				self.country2=countries[1]
			elif len(countries) == 1:
				self.country1=countries[0]


	def average_deaths_by_day(self):
		"""
			Average number of deaths per day in each country

			average: suma de muertes / numero de dias
		"""

		for columna in range(len(self.list[0])):
			suma=0
			for fila in range(1,len(self.list)):
				if self.list[fila][2]==self.country1 or self.list[fila][2]==self.country2 and len(self.list[fila][5])>0 and self.list[fila][5] !=None:
					suma+=float(self.list[fila][5])

		print(suma)

				
		

contador = counter_covid("Afghanistan","Russia")

print(contador.average_deaths_by_day())

