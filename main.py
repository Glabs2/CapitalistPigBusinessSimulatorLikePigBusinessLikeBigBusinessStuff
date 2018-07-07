import capitalist_business
import capitalist_finance
import capitalist_math
import capitalist_menus
import capitalist_networking
import capitalist_pig
import capitalist_savefile_manager
import capitalist_staff
game_state = 0
#INIT Game

#Work market setup
list_of_unemployed_employees = [capitalist_staff.employee()] * 25
for raw_employee in list_of_unemployed_employees:
    raw_employee.randomise_skills()

#Default Bank setup
npc_bank_manager = capitalist_pig.player()
npc_bank_manager.name = "Mr. Money Pig"
npc_bank_manager.business.open("NPC Bank","Bank")
npc_bank_manager.business.funds = 0
npc_bank_manager.business.inventory_space = 1000
npc_bank_manager.business.Inventory = [] #implement treasure type objects

#Default player setup
local_player = capitalist_pig.player()
#Create function to set name and console_type?
local_player.name = "Local Capitalist"
local_player.console_type = "Local"
local_player.business.open("debug_business","debug_branche")
local_player.business.Funds = 5000
capitalist_staff.employee().hire(local_player.business,"Guard",1000)
#Move take function out of loan class?
local_player.business.loans = [capitalist_finance.loan()]
local_player.business.loans[0].take(local_player.business,npc_bank_manager.business,5000,0,rate=500)
game_state = 1

#Game Loop
while game_state > 0:
    game_state = 0

#Debug!!! Test Save!
debug_save = capitalist_savefile_manager.save_file()
debug_save.unemployed_employees = list_of_unemployed_employees
debug_save.npcs = [npc_bank_manager]
debug_save.players = [local_player]
debug_save.save()

#Exit Game
exit(game_state)
