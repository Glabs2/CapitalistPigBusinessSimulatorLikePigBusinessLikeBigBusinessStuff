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
npc_bank = capitalist_business.business()
npc_bank.open("NPC Bank","Bank")
npc_bank.type = "NPC"
npc_bank.funds = 0
npc_bank.inventory_space = 1000
npc_bank.Inventory = []

#Debug!!! Default selection for Test Save
local_player = capitalist_pig.player()
local_player.business.open("debug_business","debug_branche")
local_player.business.Funds = 5000
capitalist_staff.employee().hire(local_player.business,"Guard",1000)
#Move take function out of loan?
local_player.business.loans = [capitalist_finance.loan()]
local_player.business.loans[0].take(borrower=local_player,giver=npc_bank,sum=5000,intrest=0,rate=500)
game_state = 1

#Game Loop
while game_state > 0:
    game_state = 0

#Debug!!! Test Save
debug_save = capitalist_savefile_manager.save_file()
debug_save.unemployed_employees = list_of_unemployed_employees
debug_save.npc_bank = npc_bank
debug_save.players = [local_player]
debug_save.save()

#Exit Game
exit(game_state)
