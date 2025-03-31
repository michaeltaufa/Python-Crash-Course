"""
Project Name: Yu-Gi-Oh Card Classes 
Author: Michael Taufa
Date: 2025-03-28
Description: This program will list all Yu-Gi-Oh card classes
"""


class Monster_Card:
    def __init__(self, cardName, monsterLevel, attackLevel, defenseLevel):
        self.cardName = cardName
        self.monsterLevel = monsterLevel
        self.attackLevel = attackLevel
        self.defenseLevel = defenseLevel

    def attack_position(self):
        message_attackPosition = f"{self.cardName.title()} is in attack position."

        print(message_attackPosition)

        return message_attackPosition

    def defense_position(self):
        message_defensePosition = f"{self.cardName.title()} is in defense position."

        print(message_defensePosition)

        return message_defensePosition

    def display_monsterLevel(self):
        message_monsterLevel = f"{self.cardName.title()}'s monster level is {self.monsterLevel}."

        print(message_monsterLevel)

        return display_monsterLevel


class Fusion_monster(Monster_Card):
    def __init__(self, cardName, monsterLevel, attackLevel, defenseLevel):
        super().__init__(cardName, monsterLevel, attackLevel,defenseLevel)
        self.cardType = 'fusion monster'

    def summon_fusionMonster(self):
        message_fusionMonster = f"{self.cardName.title()} has been fusion summoned."

        return message_fusionMonster


class Ritual_monster(Monster_Card):
    def __init__(self, cardName, monsterLevel, attackLevel, defenseLevel):
            super().__init__(cardName, monsterLevel, attackLevel,defenseLevel)
            self.cardType = 'ritual monster'

    def summon_ritualMonster(self):
            message_ritualMonster = f"{self.cardName.title()} has been ritual summoned."

            return message_ritualMonster 
