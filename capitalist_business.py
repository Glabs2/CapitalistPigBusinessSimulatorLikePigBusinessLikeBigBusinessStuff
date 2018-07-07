# Contains information data and Functions for all Businesses in town
# At the moment this file serves as a container for data and Functions related to the players Business
# At the multiplayer stage of development this file will be used to store and handle business affairs for all players
# NPC Businesses are also a posiblity
import capitalist_projects
import capitalist_math
class business:
    name = "Capitalist pigs glory hole"
    branche = "Night Club"
    type = "LP"
    funds = 1000.00 #Value in Currency units
    credit_worthiness = 0 #Value in Percent use in determaning if loan request will be accepted
    loans = []
    employees = []
    projects = []
    inventory_space = 5
    Inventory = [capitalist_projects.product()] * 5
    def open(self,name,branche):
        self.name = name
        self.branche = branche
    def renovation(self,inventory_space):
        costs = capitalist_math.calculate_renovation_cost(self,inventory_space)
        if costs < self.funds:
            self.funds =- costs
            self.inventory_space = inventory_space
        else:
            #Handle exeption
            pass
