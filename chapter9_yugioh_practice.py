# For this program, we will be focused on Inheritance, where creating 
# 'Parent Classes' and 'Child Classes'
    # This program has been created by Michael Taufa


# Parent Class
    # When creating Parent Class, it is important to focus on main attributes
    # a class that can transfer to subclass

class Monster_Cards():
    def __init__(self, monsterName, monsterLevel, attackLevel, defenseLevel):
        self.monsterName = monsterName
        self. monsterLevel = monsterLevel
        self.attackLevel = attackLevel
        self.defenseLevel = defenseLevel

    def display_monsterLevel(self):
        message_monsterLevel = f"{self.monsterName.title()}'s level is {self.monsterLevel}."

        return message_monsterLevel

    def attack_position(self):
        message_attackPosition = f"{self.monsterName.title()} is in attack position."

        return message_attackPosition

    def defense_position(self):
        message_defensePostion = f"{self.monsterName.title()} is in defence position."

        return message_defensePostion

    # 'Parent Class' methods can be override by redeclaring method in 'Child Class'
    def normal_summon(self):
        message_normalSummon = f"{self.monsterName.title()} is normal summoned."

        return message_normalSummon


# Create a class/ instance of an Attribute:
    # We will call this attribute to other subclasses

class Special_Summon():
    
    def __init__(self, special_summon = 'successful'):
        self.special_summon = special_summon

    def specialSummon_Monster(self):
        message_specialSummon = f"This monster has been special summoned."

        return message_specialSummon

class Fusion_summonAttribute():
    def __init__(self, fusion_summon = 'successful'):
        self.fusion_summon = fusion_summon

    def fusion_summon_monster(self):
        message_fusionSummon = f"This monster has been fusion summoned."

        return message_fusionSummon 

# Child Class
    # When creating Child Class, it is IMPORTANT to declare child class 'AFTER'
    # the 'Parent Class'
        # NOTE: The super() main purpose is to intialize all functions from Parent Class

class normal_monsterCard(Monster_Cards):

    def __init__(self, monsterName, monsterLevel, attackLevel, defenseLevel):
        super().__init__(monsterName, monsterLevel, attackLevel, defenseLevel)
        self.cardType = 'normal'
        self.cardColor = 'yellow'
        self.special_summon = Special_Summon()

    def normal_summon(self):
        message_normalSummon = f"{self.monsterName.title()} is normal summoned."

        return message_normalSummon



class effect_monsterCard(Monster_Cards):

    def __init__(self, monsterName, monsterLevel, attackLevel, defenseLevel):
        super().__init__(monsterName, monsterLevel, attackLevel, defenseLevel)
        self.cardType = 'effect'
        self.cardColor = 'orange'

    def display_effect(self):
        message_monsterEffect = f"{self.monsterName.title()}'s effect is activated."

        return message_monsterEffect

    def normal_summon(self):
        message_normalSummon = f"{self.monsterName.title()} is normal summoned."

        return message_normalSummon


class fusion_monsterCard(Monster_Cards):

    def __init__(self, monsterName, monsterLevel, attackLevel, defenseLevel):
        super().__init__(monsterName, monsterLevel, attackLevel, defenseLevel)
        self.cardType = 'fusion'
        self.cardColor = 'purple'
        self.fusion_summon = Fusion_summonAttribute()

    def normal_summon(self):
        message_normalSummon = f"{self.monsterName.title()} cannot be normal summoned."

        return message_normalSummon


class ritual_monsterCard(Monster_Cards):

    def __init__(self, monsterName, monsterLevel, attackLevel, defenseLevel):
        super().__init__(monsterName, monsterLevel, attackLevel, defenseLevel)
        self.cardType = 'ritual'
        self.cardColor = 'blue'

    def normal_summon(self):
        message_normalSummon = f"{self.monsterName.title()} cannot be normal summoned."

        return message_normalSummon


print("\nThis card is created from the 'Child Class' for 'dragon1'.")
dragon1 = normal_monsterCard('blue eyes white dragon', 7, 3_000, 2_500)
print(dragon1.monsterName.title())
print(dragon1.display_monsterLevel())
print(dragon1.attack_position())
print(dragon1.defense_position())
print(dragon1.normal_summon())

print(dragon1.special_summon.specialSummon_Monster())

print("\nThis card is created from the 'Child Class' for 'dragon2'.")
dragon2 = normal_monsterCard('red eyes black dragon', 7, 2_400, 2_000)
print(dragon2.monsterName.title())
print(dragon2.display_monsterLevel())
print(dragon2.attack_position())
print(dragon2.defense_position())
print(dragon2.normal_summon())


print("\nThis card is created from the 'Child Class' for 'dragon3'.")
dragon3 = fusion_monsterCard('blue eyes ultimate dragon', 12, 4_500, 3_800)
print(dragon3.fusion_summon.fusion_summon_monster())


warrior1 = ritual_monsterCard('black luster soldier', 8, 3_000, 2_500)
spellcaster2 = effect_monsterCard('dark magician girl', 6, 2_000, 1_700)











