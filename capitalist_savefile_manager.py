# Contains functions for saveing loading and general user data management
import csv
import collections
# To be added with LAN multiplayer support
#import capitalist_networking
class save_file:
    year = 1982
    month = 6
    #day = 4
    difficulty = 1
    players = [capitalist_pig.player()]
    def save(self):
        file = open("saves.csv","w")
        writer = csv.writer(file,delimiter=";kill_that_capitalist_pig;")
        csv.wrterow("year","month","difficulty","player_data")
        writer.writerow([self.year,self.month,self.difficulty,self.players])
    def load(self):
        file = open("saves.csv","r")
        reader = csv.reader(file,delimiter=";kill_that_capitalist_pig;")
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
