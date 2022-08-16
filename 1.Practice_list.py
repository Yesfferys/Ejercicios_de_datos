import csv 
from pprint import pprint
import matplotlib.pyplot as plt

with open ("owid-covid-data.csv","r") as csv_file:
	csv_reader = csv.reader(csv_file)
	list=list(csv_reader)

class counter_covid:
	"""
		counter of case covid 
	"""
	list=list

	def __init__(self,*countries):
		self.countries=[]
		for country in countries:
			self.countries.append(country)

	def number_case_by_day(self):
		"""
		Solo muestra nuevos casos por dia  "Afghanistan" y "Russia"
		"""
		number_case_by_day_Afghanistan=[]
		number_case_by_day_Afghanistan_float=[]
		number_case_by_day_Afghanistan_accumulated=[]
		day_reported_Afghanistan=[]

		for file in range(1,len(list)):
			if list[file][2]=="Afghanistan" and len(list[file][5])>0:
				number_case_by_day_Afghanistan.append(list[file][5]) 
			if list[file][2]=="Afghanistan" and len(list[file][5])>0:
				day_reported_Afghanistan.append(list[file][3])

		for i in number_case_by_day_Afghanistan:
			if len(i)!=0:
				number_case_by_day_Afghanistan_float.append(float(i))

		suma=0
		for item in number_case_by_day_Afghanistan_float:
			suma+=item
			number_case_by_day_Afghanistan_accumulated.append(suma)


		number_case_by_day_Russia=[]
		number_case_by_day_Russia_float=[]
		number_case_by_day_Russia_accumulated=[]
		day_reported_Russia = []

		data_russia = [number_case_by_day_Russia.append(list[file2][5]) for file2 in range(1,len(list)) if list[file2][2]=="Russia"]
		data_russia_float = [number_case_by_day_Russia_float.append(float(elem)) for elem in number_case_by_day_Russia if len(elem) > 0]
		
		# como llevar toda esta expresion a lista por comprension
		suma=0
		for j in number_case_by_day_Russia_float :
			suma+=j
			number_case_by_day_Russia_accumulated.append(suma) 

		data_day_reported_Russia=[day_reported_Russia.append(list[file1][3]) for file1 in range(1,len(list)) if list[file1][2]=="Russia" and len(list[file1][5])>0]

			
		#grafica
		plt.subplot(2, 1, 1)
		plt.plot(day_reported_Afghanistan,number_case_by_day_Afghanistan_accumulated,marker="o",linestyle="--",color="r",label="Afghanistan")
		plt.xlabel("day_reported_Afghanistan")
		plt.ylabel("number_case_by_day_Afghanistan_accumulated")
		plt.title("day_reported vs  number_case_by_day_accumulated ")
		plt.legend()
		plt.grid()

		plt.subplot(2, 1, 2)
		plt.plot(day_reported_Russia,number_case_by_day_Russia_accumulated,marker="o",linestyle="-",color="g",label="Russia")
		plt.xlabel("day_reported_Russia")
		plt.ylabel("number_case_by_day_Russia_accumulated")
		plt.title("day_reported_R  vs  number_case_by_day_accumulated ")
		plt.legend()
		plt.grid()
		
		plt.suptitle("Dias reportados de casos nuevos")
		plt.show()

	
	def average_deats_by_day(self,*countries_deats):
		"""
		se visualizan el promedio de muerte por dia del pais señalado o de todos los paises
		"""
		if len(countries_deats) == 0:

			countries_deats1=[] # devuelve lista de paises total

			for file in range(1,len(list)):
				if list[file][2] not in countries_deats1:
				 	countries_deats1.append(list[file][2])
			
		else:
			countries_deats1=[] # devuelve los paises dados como argumentos en la funcion
			for c_d in countries_deats:
				countries_deats1.append(c_d)


		def sum_deats(pais):
			data_sum_deats_by_country=[]
			for file in range(1,len(list)):
				if list[file][2]==pais and len(list[file][8])!=0:
					data_sum_deats_by_country.append(float(list[file][8]))
			return sum(data_sum_deats_by_country)

		sum_total_deaths_by_country=[x for x in map(sum_deats,countries_deats1)]

		def dias_reportados(pais):
			day_reported_by_country=[]
			for file in range(1,len(list)):
				if list[file][2]==pais:
					day_reported_by_country.append(list[file][8])
			return len(day_reported_by_country)

		sum_total_day_reported_by_country=[x for x in map(dias_reportados,countries_deats1)]

		average_of_deaths_by_country=[]
		for pais in range(len(countries_deats1)):
			average_of_deaths_by_country.append(sum_total_deaths_by_country[pais]/sum_total_day_reported_by_country[pais])

		for valor_A,valor_B in zip(countries_deats1,average_of_deaths_by_country):
			print("the average of deaths is",valor_B,"in the country",valor_A)


counter = counter_covid("Chile","Russia","Afghanistan")

print(counter.average_deats_by_day())
#print(counter.number_case_by_day())