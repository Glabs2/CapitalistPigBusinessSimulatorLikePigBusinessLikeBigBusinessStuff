# Contains functions for saveing loading and general user data management
import csv
import collections
import capitalist_pig
import capitalist_business
import capitalist_staff
# To be added with LAN multiplayer support
#import capitalist_networking
class save_file:
    year = 1982
    month = 6
    #day = 4
    difficulty = 1
    unemployed_employees = []
    #I dont like haveing the npc bank separate like this.
    npc_bank = capitalist_business.business()
    players = [capitalist_pig.player()]
    def set_data(self,new_year,new_month,new_difficulty,new_unemployed_employees,new_npc_bank,new_players):
        self.year = new_year
        self.month = new_month
        self.difficulty = new_difficulty
        self.unemployed_employees = new_unemployed_employees
        self.npc_bank = new_npc_bank
        self.players = new_players
    def save(self):
        file = open("saves.csv","w")
        writer = csv.writer(file,delimiter=";")
        writer.writerow(["year","month","difficulty","player_data"])
        #Does not work with player object needs rework!
        #Error can be viewed in saves.csv.
        writer.writerow([self.year,self.month,self.difficulty,self.players])
    def load(self):
        file = open("saves.csv","r")
        reader = csv.reader(file,delimiter=";")
        print("Debug!!!")
        for save in  reader:
            print("start_of_save")
            print(save[0])
            print(save[1])
            print(save[2])
            print(save[3])
            print("end_of_save")
    def delete(self):
        pass
    # To be added with LAN multiplayer support
    #def post(self,NetworkStuff):
    #    pass
    #def get(self,NetworkStuff):
    #    pass
    #def list(self,NetworkStuff):
    #   pass
