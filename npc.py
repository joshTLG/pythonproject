import items


class NonPlayableCharacter():
    def __init__(self):
        raise NotImplementedError("Create subclass of NPC.")

    def __str__(self):
        return self.name


class Trader(NonPlayableCharacter):
    def __init__(self):
        self.name = "Merchant"
        self.gold = 1000
        self.inventory = [items.SmallBandage(),
                      items.SmallBandage(),
                      items.SmallBandage(),
                      items.FirstAidKit(),
                      items.Axe(),
                      items.Spear(),
                      items.Sword(),
                      items.DawnHammer()]