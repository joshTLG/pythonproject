import random


class Enemy:
    def __init__ (self):
        raise NotImplementedError("Do not create raw Enemy classes")
    
    def __str__(self):
        return self.name
    
    def is_alive(self):
        return self.hp > 0
        
        # all of my enemies are weak for the sake of the demonstration. Watching me fight them with any strategy wouldn't be fun in text
class boss (Enemy):
    def __init__(self):
        self.name = "King Slime"
        self.hp = 10
        self.damage= 1
        self.gold=random.randint(20,40)
        self.exp =100

class Wizard (Enemy):
    def __init__(self):
        self.name = "Wizard"
        self.hp = 10
        self.damage= 1
        self.gold=random.randint(20,40)
        self.exp =15
        
class Slime (Enemy):
    def __init__(self):
        self.name = "Blue Slime"
        self.hp = 10
        self.damage = 1
        self.gold=random.randint(40,60)
        self.exp =20
        
class Sabre_Cub (Enemy):
    def __init__(self) :
        self.name = "Sabre Cub"
        self.hp = 10
        self.damage = 1
        self.gold=random.randint(60,80)
        self.exp =30
        
class Tank(Enemy):
    def __init__ (self):
        self.name =" Big-old Tank "
        self.hp =10
        self.damage=1 
        self.gold=random.randint(80,100)
        self.exp =40
