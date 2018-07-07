# Formulars and Calulations used by the game
import random as r
def __init__(self):
	#Debug!!!
	print("import successful")
def calculate_customers(pr_val,employees):
	customers = (pr_val + employees * r.uniform(0.8,1.3)) * r.uniform(0.9,1.2)
	return customers
def calculate_moral():
	#Debug!!!
	moral = 1
	return moral
def calculate_rate(sum,intrest,duration):
	print("Debug!!!")
	print(sum)
	print(intrest)
	print(duration)
	rate = (sum+intrest)/duration
	return rate
def calculate_duration(sum,intrest,rate):
	duration = (sum+intrest)/rate
	#implement dealing with offset here

	return duration
def calcuate_material_cost():
		pass
