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
list_of_unemployed_employees = [employee()] * 25
for raw_employee in list_of_unemployed_employees:
    raw_employee.randomise_skills()

#Default Bank setup
npc_bank = business()
npc_bank.open("NPC Bank","Bank")
npc_bank.type = "NPC"
npc_bank.funds = 0
npc_bank.inventory_space = 1000
npc_bank.Inventory = []

#Debug!!! Default selection for Test Save
local_player = capitalist_pig.player()
local_player.business.open("debug_business","debug_branche")
local_player.business.Funds = 5000.00
capitalist_staff.employee().hire(local_player.business,"Guard",1000)
capitalist_finance.loan.take(local_player,npc_bank,5000,0,500)
game_state = 1

#Game Loop
while game_state:
    game_state = 0

#Debug!!! Test Save
debug_save = capitalist_savefile_manager.capitalist_savefile()
debug_save.players = [local_player];
debug_save.save()
#Exit Game
exit(game_state)
