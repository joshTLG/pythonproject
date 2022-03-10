import items
import world 

class Player:
    def __init__(self):
        self.inventory= [items.Rock(),
                        items.Dagger(),                
                        items.RottenBread(),
                        items.SmallBandage(),                        
                        items.SmallBandage(),
                        items.FirstAidKit()]
                        
        self.x = world.start_tile_location[0]
        self.y = world.start_tile_location[1]
        self.hp = 100
        self.gold= 10
        self.power = 2
        self.win= False
        self.exp=0
        self.strength_up=1
        self.fullhp = 100
        self.level_2 = True
        self.level_3 = True
        self.level_4 = True
        self.level_5 = True
        self.level_6 = True
        self.level_7 = True
        self.level_8 = True
        self.level_9 = True
        self.level_10 = True
        
    def is_alive(self):
        return self.hp >0
     
    def print_inventory(self):
        print("Inventory/Stats:")
        for item in self.inventory: 
            print(" "+ str(item))
        print(f"Gold: {self.gold}")
        print(f"Experience:{self.exp}")
        print(f"Hp:{self.hp}")
        attackpower=self.strength_up+self.power        
        print(f"Attack:{attackpower}")
        
    
    def heal(self):
        health = [item for item in self.inventory
                       if isinstance(item, items.Health)]  
        if not health:                                     
            print("You're out of healing items, seek shelter.")
            return

        for i, item in enumerate(health, 1):
            print("Use a healing item?: ")
            print(f"{i}. {item}")
        
        valid = False
        while not valid:
            choice = input("")
            try:
                to_eat = health[int(choice) - 1]   
                self.hp = min(self.fullhp, self.hp + to_eat.healing_value)
                self.inventory.remove(to_eat)
                print(f"Current HP: {self.hp}")
                valid = True
            except (ValueError, IndexError):
                print("You don't have that. Choose again.") 
     
    def equip(self):
        
        Weapons= [item for item in self.inventory
               if isinstance(item, items.Weapon)]  
        if not Weapons:                                     
            print("Nothing to equip!")
            return
        
        print("Equip: ")
        for i, item in enumerate(Weapons, 1):
            
            print(f"{i}. {item}")

        valid = False
        while not valid:
            choice = input("")
            try:
                best_weapon= Weapons[int(choice) - 1]   
                self.power=best_weapon.damage
                print(f"Current Weapon damage: {best_weapon.damage}")
                valid = True
            except (ValueError, IndexError):
                print("Invalid choice, try again.")
     
                            
    def move(self,mx,my):   
        self.x += mx        
        self.y += my         
                            
    def move_north(self):
        self.move(mx=0, my=-1)
        
    def move_south(self) :
        self.move(mx=0, my=1)
     
    def move_east(self):
        self.move(mx=1, my=0)

    def move_west(self):
        self.move(mx=-1, my=0)  


    def attack(self):
        room = world.tile_at(self.x, self.y)  
        enemy = room.enemy
        print (f"You attack the {enemy.name}!")    
        enemy.hp-=self.power+self.strength_up 
        if not enemy.is_alive():
            print (f"You killed {enemy.name}!")
            self.gold=self.gold+enemy.gold
            self.exp=self.exp+enemy.exp
            print (f"You gain {enemy.gold} gold! ")
            
            print (f"You gain {enemy.exp} experience! ")
            
            
            
            
            if self.exp>50 and self.level_2:
                self.strength_up=4
                self.hp= 120 
                self.fullhp=120
                print("You're now level 2")
                print(f"Current HP: {self.hp}")
                self.level_2 = False
                
                         
            if self.exp>100 and self.level_3:
                self.strength_up=6  
                self.hp= 130
                self.fullhp=130
                print("You're now level 3")
                print(f"Current HP: {self.hp}")
                self.level_3 = False
                
            if self.exp>150 and self.level_4:
                self.strength_up=8  
                self.hp= 140 
                self.fullhp=140
                print("You're now level 4")
                print(f"Current HP: {self.hp}")
                self.level_4 = False 
                
            if self.exp>200 and self.level_5:
                self.strength_up=10
                self.hp= 150 
                self.fullhp=150
                print("You're now level 5")
                print(f"Current HP: {self.hp}")
                self.level_5 = False
                
                
            if self.exp>250 and self.level_6:
                self.strength_up=12 
                self.hp= 160
                self.fullhp=160
                print("You're now level 6")
                print(f"Current HP: {self.hp}")
                self.level_6 = False
           
            if self.exp>350 and self.level_7:
               self.strength_up=14 
               self.hp= 170
               self.fullhp=170
               print("You're now level 7")
               print(f"Current HP: {self.hp}")
               self.level_7 = False 
               
            if self.exp>500 and self.level_8:
               self.strength_up=16 
               self.hp= 180
               self.fullhp=180
               print("You're now level 8")
               print(f"Current HP: {self.hp}")
               self.level_8 = False    
             
            if self.exp>650 and self.level_9:
               self.strength_up=18 
               self.hp= 200
               self.fullhp=200
               print("You're now level 9")
               print(f"Current HP: {self.hp}")
               self.level_9 = False              

            if self.exp>800 and self.level_10:
               self.strength_up=20 
               self.hp= 220
               self.fullhp=220
               print("You're now level 10")
               print(f"Current HP: {self.hp}")
               self.level_10 = False                             
              
        else:
            print(f"{enemy.name} has {enemy.hp} Hit Points.")
            
    def trade(self):
        room = world.tile_at(self.x, self.y)
        room.check_if_trade(self)            
