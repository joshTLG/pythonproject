from collections import OrderedDict
from player import Player
import world
import time 

def play():
    print(r""" 



    
................................................,,..................................................
...............................................:;;;,................................................
..............................................,*++*:................................................
..............................................:****+................................................
...........................................,,,+?++**:,,.............................................
.........................................,:+*+;;;;+++**;,,..........................................
....................................,,,:++***+++;;+++***++:,,,......................................
................................,,:;+++****?**********?****+++;;:,..................................
..............................,;++**???????**?????????????????***+;:,...............................
............................,+***??%%??????*?????????????????%%???**+:,.............................
...........................:*???%%%%%?????***++++++****??????%%%%%??**;,............................
..................,.......;*???%%%%%%%???*++++;;;;;++****????%%%%%%%??*+,...........................
................:;;+;....:*???%%%%%%%%???**********????**???%%%%%%%%%%?*;....,;;;:..................
................;*+;*;,.:;+?%?%%%%%%%%%%??????????????????%%%%%%%%%%%%?++:..,+*;++,.................
................,:;:,;++++;+%%%%%%%%%%%%???????*;;*???????%%%%%%%%%%%%+;++++;::;;:..................
...................,:..,;???+*%%%%%%%%%%?????%?*++*?%%????%%%%%%%%%%?+??*+:,.::.....................
....................,:;;*?****+*??%%%%%%??%%%*+????**?%???%%%%%%?**++**?*?;;:,......................
.....................,;????????*+**%%%%%?%%%**********?%%%%%%%%?+++*???????+,.......................
......................:**?????????****?????????????????????????**????????*+:........................
.....................,;??*************+*********************++*************;,,......................
.................,,:::;*%%%%???********++++++;;;;+;;+++++****++++****???%%?;;:::,,..................
..............,,::;;;;;;+***????????%%%????????????????????????????*******++;;;;;::,,...............
...........,,:;;;;;;;;;+++++++++++*++++++++++++++**+++++***+**+++++++++++++++++;;;;;;:,.............
.........,:;;;;;;;;;++++++++++++++*+++*++++++++++++++****************+++++++++++++;;;;;;:,..........
.......,:;;;;;;+++++++++++++++++++++++++++++++++++++++++***************++++++++++++++;;;;;:.........
......:;;;;++++++++++++++++++*+++++++++++++++++++++++++++++*++*+*********++++++++++++++++;;;,.......
....,:;;++++++++++++++++++****+++++++++++;:::,:;;;;:::::;+++++++++*********+++++++++++++++++;:......
...,:;++++++++++++++*********++++++++;;;:.+##;.:;+:.%#S:.;++++++++++**********++++++++++++++++:.....
...:;+++++*+*+***+*******++++++;;++;;;;;;,:;;,:;;;;::;;,:;++++;;;++++++************++++++++++++:....
..:;+++++***************++++;;;::;+++++;;;;:;;;;;;;;;;;;++++*++;:;;;++++++***************+++++++,...
.,;++++++************++*++++;;;;;++*?%?**+++++++++++++++***?%?++;;+++++++********************+++;...
.:+++++*************************+**?S#S%?????*******??????%S@%*******************************++++,..
.;++********************************%???????********??????????+*******************************+++;..
,;++******************************+;;++**???????????????***++;++*********??*******************+++;..
,+++*********************************+++;;;;+++++++++++++++************************************+++,.
,+++*******************************************************************************************+++,.
,;++******************************************************************************************+++;..
.;++******************************************************************************************+++:..
.:++******************************************************************************************+++,..
..;++*******************************************************************?*****?***************++:...
..,;+*****************************************************************?????????**************++;,...
...,++*********************************************************???????????????????**********++;,....
....:++*********????????????????***********************?????????????????????????????*******++;,.....
.....,;+*********????????????????????*??**????????*???????????????????????????????********++;,......
......,;+*********???????????????????????????????????????????????????????????????********++:........
........:;+********????????????????????????????????????????????????????????????*********+;,.........
.........,:;++**********????????????????????????****????????????????????????**********+;,...........
...........,:;+++***********??????????????????**********?????????????????***********+;,.............
.............,:;+++***************??????????**********??*??????????**************+;:,...............
................,:;++*******************?*************************************+;:,..................
...................,,:;++************************************************++;:,,.....................
........................,,:;;+++**********************************+++;::,,..........................
..............................,,,,:::;;;;;++++++++++++;;;;;;:::,,,,.................................
....................................................................................................
                                         
           
                       An Adventure by Josh Paige (2022)
                                                                                              """)     

    time.sleep(2)
    print("You wake up with no memory of how you got here")
    time.sleep(2)
    print("                       ")                                 
    world.parse_world_dsl()
    player=Player()  
    while player.is_alive()and not player.win:
        room=world.tile_at(player.x, player.y)  
        print(room.intro_text())                 
        room.modify_player(player)  
        if player.is_alive()and not player.win:
            choose_action(room,player)
        elif not player.is_alive():
            print("You are dead.")
            input("Press enter to exit")

        
def choose_action(room, player):
    action = None
    while not action:
        available_actions = get_available_actions(room, player)
        action_input = input("Action: ")
        action = available_actions.get(action_input)
        if action:
            action()
        else:
            print("Invalid action!")
    
def get_available_actions(room, player):
    actions = OrderedDict()
    print(" Choose an action:")
    if player.inventory:
        take_action(actions, 'i', player.print_inventory, "Inventory/Stats")
    if player.inventory:
        take_action(actions, 'u', player.equip, "Equip Weapon")
    if isinstance(room, world.BossTile) and room.enemy.is_alive():
        take_action(actions, 'a', player.attack, "Attack")        
    if isinstance(room, world.TraderTile):
        take_action(actions, 't', player.trade, "Trade")  
    if isinstance(room, world.EnemyTile) and room.enemy.is_alive():
        take_action(actions, 'a', player.attack, "Attack")
    
    
    else:
        if world.tile_at(room.x, room.y - 1):
            take_action(actions, 'n', player.move_north, "Go north")
        if world.tile_at(room.x, room.y + 1):                       
            take_action(actions, 's', player.move_south, "Go south")
        if world.tile_at(room.x + 1, room.y):
            take_action(actions, 'e', player.move_east, "Go east")
        if world.tile_at(room.x - 1, room.y):
            take_action(actions, 'w', player.move_west, "Go west")
    if player.hp < player.fullhp:
        take_action(actions, 'h', player.heal, "Heal")

    return actions

def take_action(action_dict, hotkey, action, name):
    action_dict[hotkey.lower()] = action
    action_dict[hotkey.upper()] = action
    print(f"{hotkey}: {name}")



    

play()
