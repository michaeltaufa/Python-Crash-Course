"""
Project Name: Yu-Gi-Oh Main 
Author: Michael Taufa
Date: 2025-03-28
Description: 
    This program will be the main file to execute files that are
    imported from 'yugioh_classModule.py' 
"""

print("\nThis is the start of the program: 'yugioh main'")

# from yugioh_classModules import Monster_Card, Fusion_monster, Ritual_monster

# SECTION - 'from file import class' method
    # NOTE: You can import specific classes from a class module

# print("\nThis instances is a fusion monster: Blue Eyes Ultimate Dragon")
# fusion_dragon = Fusion_monster('blue eyes ultimate dragon', 12, 4_500, 3_800)
# print(fusion_dragon.summon_fusionMonster())
# fusion_dragon.attack_position()


# print("\nThis instances is a ritual monster: Black Luster Soldier")
# ritual_monster = Ritual_monster('black luster soldier', 12, 3_000, 2_500)
# print(ritual_monster.summon_ritualMonster())
# ritual_monster.attack_position()


# SECTION - 'import file' method
    # NOTE: You can import the module and have access to ALL CLASSES
        # REMEMBER: You will need to use dot notation to call classes appropriately

import yugioh_classModules

fusion_dragon2 = yugioh_classModules.Fusion_monster('black skull dragon', 10, 3_300, 3_000)
print(fusion_dragon2.cardName.title())




