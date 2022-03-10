class Weapon:  
    def __init__(self):
        raise NotImplementedError("Create subclass of Weapon")
        
    def __str__(self):
        return self.name
      
class Rock(Weapon):
    def __init__(self):
        self.name="Rock"
        self.description= "Better than your fists."
        self.damage=5
        self.value= 1
class Dagger(Weapon):
    def __init__(self):
        self.name="Dagger"
        self.description="A small, rusty knife."\
                         "Easily concealable."
        self.damage=10
        self.value= 20

class Axe(Weapon):
    def __init__(self):
        self.name="Axe"
        self.description= "That's right. It's an axe!"\
                          "*Metal Guitar Wails*"
        self.damage=15
        self.value= 100

class Spear(Weapon):
    def __init__(self):
        self.name="Spear"
        self.description= "A sharp blade at the top of a stick,"\
                          "Use the pointy end"
        self.damage=20
        self.value= 250
        
class Sword(Weapon):
    def __init__(self):
        self.name="Bronze sword"
        self.description= "The kind of sword you'd find in the first level of an RPG,"\
                          "You killed all those slimes for this?"
        self.damage=30
        self.value= 150
        
class DawnHammer(Weapon):
    def __init__(self):
        self.name="Hammer of Dawn"
        self.description= "A hulking hammer,"\
                          "forged in a lake of molten mythril"
        self.damage=40
        self.value= 100        

class Health:
    def __init__ (self):
        raise NotImplementedError ("Create subclass of Health")
    
    def __str__(self):
        return "{} (+{} HP)".format(self.name, self.healing_value)
        
class RottenBread(Health):
    def __init__ (self):
        self.name = "Rotten Bread"
        self.healing_value = 15 
        self.value= 15

class SmallBandage(Health):
    def __init__(self):
        self.name = " Cloth wraps"
        self.description= "Dirty rag to stop the bleeding"
        self.healing_value = 50
        self.value = 60 

class FirstAidKit(Health):
    def __init__(self):
        self.name = " First-aid Kit"
        self.description= "This might actually help"
        self.healing_value = 100
        self.value = 150    

 

