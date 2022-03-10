import enemies
import npc
import random



# map tile is the parent class and just sets up the children's inheritance
class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError("Create a subclass instead!")

    def modify_player(self, player):
        pass


# Where you're dropped into the map
class StartTile(MapTile):
    def intro_text(self):
        return """
        It's dark in here. Try to get out of this place.
        """

# randomly generated enemies on the map
class EnemyTile(MapTile):
    def __init__(self, x, y):
        r = random.random()
        if r < 0.50:
            
            self.enemy = enemies.Slime()
            

            
            self.alive_text = "Look at that! It's a blue slime. \n" \
                              "Lets see if they're as weak as anime let you believe"\
                              "\n "\
                              "\n "        
            self.dead_text = "All that's left is the stain on your weapon."\
                             "\n "   
                             
        elif r < 0.80:
            self.enemy = enemies.Wizard()
            
            
            self.alive_text = "A guy in some robes is staring at you menacingly " \
                              "\n "\
                              "\n " 
            self.dead_text = "He should have left you alone. "\
                              "\n "
        elif r < 0.95:
            self.enemy = enemies.Sabre_Cub()
            
            
            self.alive_text = "Awww. Looks like a sweet kitten. \n" \
                              "Oh no! It's attacking "\
                              "\n "\
                              "\n "                       
            self.dead_text = "You're saddened by what you had to do. "\
                             "\n "
        else:
            self.enemy = enemies.Tank()
            
            
            self.alive_text = "This tank means business \n" \
                              "Time to show him how you fight!"\
                              "\n "\
                              "\n "
            self.dead_text = "The fires of its engine were extinguished " \
                             "\n "                    
        super().__init__(x, y)

    def intro_text(self):
        text = self.alive_text if self.enemy.is_alive() else self.dead_text
        return text

    def modify_player(self, player):
        if self.enemy.is_alive():
            player.hp = player.hp - self.enemy.damage
            print(f"{self.enemy.name} does {self.enemy.damage} damage. You have {player.hp} HP remaining.")

# Different from an enemy tile because it's the stage before the end (should be more difficult than a regular foe)
class BossTile(MapTile):
    def __init__(self,x, y):
        self.enemy = enemies.boss()
        self.alive_text = "You know all those slimes you faced earlier? \n" \
                          "Well, they got together and made this King Slime. \n" \
                          "Best of luck!"\
                          "\n"\
                          "\n"
        self.dead_text = "Wow. You made it a puddle of goo!"\
                         "\n"

        super().__init__(x, y)

    def intro_text(self):
        text = self.alive_text if self.enemy.is_alive() else self.dead_text
        return text
    
    def modify_player(self, player):
        if self.enemy.is_alive():
            player.hp = player.hp - self.enemy.damage
            print(f"The King Slime does {self.enemy.damage} damage. You have {player.hp} HP remaining.")

        
# this is the endpoint of the game
class WinTile(MapTile):
    def modify_player(self, player):
        player.win = True

    def intro_text(self):
        return """
        You made it to safety! Good work.
        """

# A place that doesn't contain a monster. Just some money
class GoldTile(MapTile):
    def __init__(self, x, y):
        self.gold = random.randint(1, 50)
        self.gold_claimed = False
        super().__init__(x, y)

    def modify_player(self, player):
        if not self.gold_claimed:
            self.gold_claimed = True
            player.gold = player.gold + self.gold
            print(f"{self.gold} gold added.")

    def intro_text(self):
        if self.gold_claimed:
            return """
            Nothing but stone and misery.
            """
        else:
            return """
            There is a treasure chest. You open it and find some gold!
            """


# Taking the NPC and putting his scenario in the Trader Tile. His child object of NPC is in the npc.py 
class TraderTile(MapTile):
    def __init__(self, x, y):
        self.trader = npc.Trader()
        super().__init__(x, y)

    def check_if_trade(self, player):
        while True:
            print("What're ya buyin?: (B)uy, (S)ell, or (Q)uit?")
            user_input = input()
            if user_input in ['Q', 'q']:
                return
            elif user_input in ['B', 'b']:
                print("Buy: ")
                self.trade(buyer=player, seller=self.trader)
            elif user_input in ['S', 's']:
                print("Sell: ")
                self.trade(buyer=self.trader, seller=player)
            else:
                print("Invalid choice!")

    def trade(self, buyer, seller):
        # enumerate makes it easy for me to keep track of the iterables (items)
        for i, item in enumerate(seller.inventory, 1):
            print(f"{i}. {item.name} - {item.value} Gold")
        while True:
            user_input = input("Press Q to exit: ")
            if user_input in ['Q', 'q']:
                return
            else:
                try:
                    choice = int(user_input)
                    to_swap = seller.inventory[choice - 1]
                    self.swap(seller, buyer, to_swap)
                except ValueError:
                    print("Try again!")

    def swap(self, seller, buyer, item):
        if item.value > buyer.gold:
            print("Too expensive")
            return
        seller.inventory.remove(item)
        buyer.inventory.append(item)
        seller.gold = seller.gold + item.value
        buyer.gold = buyer.gold - item.value
        print("THANK YOU!")

    def intro_text(self):
        return """
        Weird. Why is there another person here? And they want to trade? I guess capitalism exists in this place too.
        """
# using Domain specific language here (dsl) to be flexible and allow me to make a world map
# empty tiles are like walls - player cannot enter those areas
world_dsl = """
|ET|  |WT|  |ET|
|ET|GT|BT|TT|ET|
|ET|GT|ET|  |ET|
|TT|  |ST|GT|ET|
|GT|  |ET|  |GT|
"""

# This is checking 3 things 
# 1: Is there one starting area?
# 2: Is there one area where the player wins?
# 3: Does each row contain the same number of cells?

def is_dsl_valid(dsl):
    if dsl.count("|ST|") != 1:
        return False
    if dsl.count("|WT|") == 0:
        return False
    lines = dsl.splitlines()
    lines = [l for l in lines if l]
    pipe_counts = [line.count("|") for line in lines]
    for count in pipe_counts:
        if count != pipe_counts[0]:
            return False

    return True


# Dictionary dedicated to the areas the player will explore
tile_type_dict = {"WT": WinTile,
                  "ET": EnemyTile,
                  "ST": StartTile,
                  "GT": GoldTile,
                  "TT": TraderTile,
                  "BT": BossTile,
                  "  ": None}


world_map = []

start_tile_location = None



def parse_world_dsl():
    if not is_dsl_valid(world_dsl):
        raise SyntaxError("DSL is invalid!")

    dsl_lines = world_dsl.splitlines()
    dsl_lines = [x for x in dsl_lines if x]

    # iterate over each line in the DSL
    # instead of i, I'm using y because we're working with an x,y grid
    for y, dsl_row in enumerate(dsl_lines):
        # object to store the tiles
        row = []
        # split method allows abbreviations 
        dsl_cells = dsl_row.split("|")
        # split includes beginning and end of the line so to remove nonexistent cells
        dsl_cells = [c for c in dsl_cells if c]
        # using x and iterating over the cells in DSL line
        for x, dsl_cell in enumerate(dsl_cells):
            # look up abbreviation
            tile_type = tile_type_dict[dsl_cell]
            # looks for the starting point and makes that the coordinates the player starts at
            if tile_type == StartTile:
                global start_tile_location
                start_tile_location = x, y
            row.append(tile_type(x, y) if tile_type else None)

        world_map.append(row)


def tile_at(x, y):
    if x < 0 or y < 0:
        return None
    try:
        return world_map[y][x]
    except IndexError:
        return None