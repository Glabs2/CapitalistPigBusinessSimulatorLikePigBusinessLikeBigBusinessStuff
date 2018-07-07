# Formulars and Calulations used by the game
import random as r
class cap_math:

	def __init__(self):
		#Debug!!!
		print("import successful")


    def calculate_customers(self,pr_val,employees):
    	customers = (pr_val + employees * r.uniform(0.8,1.3)) * r.uniform(0.9,1.2)
    	return customers
	def calculate_moral(self,):
		#Debug!!!
		moral = 1
		return moral
	def calculate_rate(self,sum,intrest,duration):
		rate = (sum+intrest)/duration
		return rate
	def calculate_duration(self,sum,intrest,rate):
		duration = (sum+intrest)/rate
		#implement dealing with offset here

		return duration
	def calcuate_material_cost(self):
		pass
