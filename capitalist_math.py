#Formulars and Calulations used by the game
import random as r

class CapMath:

	def __init__(self):
		#Debug!!!
		print("import successful")


    def calculate_customers(self,pr_val,employees):
    	customers = (pr_val + employees * r.uniform(0.8,1.3)) * r.uniform(0.9,1.2)
    	return customers
