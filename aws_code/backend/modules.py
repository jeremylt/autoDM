"""
    Auto DM

    Jeremy L Thompson

    This file provides module objects
"""
# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------

# Dictionaries
from dictionaries import *
# Utilities
import random
from bisect import bisect
from abc import ABC, abstractmethod

# ------------------------------------------------------------------------------
# Utilities
# ------------------------------------------------------------------------------
def replyCheck(reply):
    """ Check reply for error """

    if "ERROR" in reply:
        return "ERROR"
    else:
        return reply

# ------------------------------------------------------------------------------
def toInt(string):
    """ Convert string to int """

    try:
        number = int(float(string))
    except:
        number = 0
    return number

# ------------------------------------------------------------------------------
def toFlt(string):
    """ Convert string to float """

    try:
        number = float(string)
    except:
        number = 0.0
    return number

# ------------------------------------------------------------------------------
def toStr(number):
    """ Convert float/int to string """

    return str(int(number))

# ------------------------------------------------------------------------------
# Base Class - Module
# ------------------------------------------------------------------------------
class Module:
    """ Module base class """

    @abstractmethod
    def getShortDesc(self):
        """ Build the short description """
        pass

    @abstractmethod
    def getLongDesc(self):
        """ Build the long description """
        pass

# ------------------------------------------------------------------------------
# Monster Class
# ------------------------------------------------------------------------------
class Monster(Module):
    """ Monster Class """
    name = ""   # Name of the monster
    hp = [0, 0] # HP range of the monster

    # Get monster by CR and/or Env
    def getMonster(self, CR, envType):
        """ Get a random monster by CR and environment """

        # No CR
        if CR == "":
            monsters = [monster["Name"] for monster
                        in allMonsters
                        if envType in monster['Env']]
        # No Env
        elif envType == "":
            monsters = [monster["Name"] for monster
                        in allMonsters
                        if monster['CR'] == CR]
        # Both CR and Env
        else:
            monsters = [monster["Name"] for monster
                        in allMonsters
                        if envType in monster['Env']
                        and monster['CR'] == CR]

        # Get random monster
        if len(monsters):
            name = random.choice(monsters)
        else:
            name = "ERROR"

        # Return
        return name

    # Init
    def __init__(self, CR, envType):
        # Get random monster
        self.name = self.getMonster(CR, envType)

        # Get HP
        if self.name != "ERROR":
            self.hp = allHP[[monster["CR"] for monster
                            in allMonsters
                            if monster["Name"] == self.name][0]]

    # Short description
    def getShortDesc(self):
        """ Build the short description """

        # Build description
        desc = self.name

        # Check
        desc = replyCheck(desc)

        # Log
        print("Monster Short Desc: " + desc)

        # Return
        return desc

    # Long description
    def getLongDesc(self):
        """ Build the long description """

        # Build description
        desc = self.name + " - HP: " + str(self.hp[0]) + "-" + str(self.hp[1])

        # Check
        desc = replyCheck(desc)

        # Log
        if desc == "ERROR":
            print("Monster Long Desc: " + desc)
        else:
            print("Monster Long Desc: " + self.name)

        # Return
        return desc

# ------------------------------------------------------------------------------
# Npc Class
# ------------------------------------------------------------------------------
class Npc(Module):
    """ Npc Class """
    name = ""     # Name of the NPC
    npcClass = "" # Class of the NPC

    # Get NPC by CR and/or Env
    def getNPCClass(self, CR, envType):
        """ Get a random NPC class by CR and environment """

        # Check for valid CR
        if CR != "" and  toInt(CR) < 2:
            return "ERROR"

        # No CR or Env
        elif CR == "" and envType == "":
            npcs = [npc["Name"] for npc
                    in allNPCs]
        # No CR
        elif CR == "":
            npcs = [npc["Name"] for npc
                    in allNPCs
                    if envType in npc['Env']]
        # No Env
        elif envType == "":
            npcs = [npc["Name"] for npc
                    in allNPCs
                    if abs(toInt(npc['CR']) - toInt(CR)) <= 2]
        # Both CR and Env
        else:
            npcs = [npc["Name"] for npc
                    in allNPCs
                    if envType in npc['Env']
                    and abs(toInt(npc['CR']) - toInt(CR)) <= 2]

        # Get random NPC
        if len(npcs):
            npcClass = random.choice(npcs)
        else:
            npcClass= "ERROR"

        # Return
        return npcClass

    # Init
    def __init__(self, CR, envType):
        # Get NPC class
        self.npcClass = self.getNPCClass(CR, envType)

        # Get NPC name
        self.name = random.choice(allNames)

    # Short description
    def getShortDesc(self):
        """ Build the short description """

        # Build description
        desc = self.npcClass

        # Check
        desc = replyCheck(desc)

        # Log
        print("NPC Short Desc: " + desc)

        # Return
        return desc

    # Long description
    def getLongDesc(self):
        """ Build the long description """

        # Build description
        desc = self.name + " - " + self.npcClass

        # Check
        desc = replyCheck(desc)

        # Log
        if desc == "ERROR":
            print("NPC Long Desc: " + desc)
        else:
            print("NPC Long Desc: " + self.npcClass)

        # Return
        return desc

# ------------------------------------------------------------------------------
# Encounter Class
# ------------------------------------------------------------------------------
class Encounter(Module):
    """ Encounter Class """
    npc = None      # NPC in the encounter
    monsters = None # List of monsters in the encounter
    numMob = 0      # Number of monsters/NPCs in the encounter

    # Init
    def __init__(self, CR, envType):
        # Check for valid CR
        if CR != "" and  toInt(CR) < 1:
            return None

        # Pick random CR if no CR
        if CR == "":
          CR = toStr(random.randint(1, 20))

        # Get tier
        tier = toInt(CR) // 5
        if tier > 4:
            tier = 4

        # Add NPC, if tier 1+
        if tier >= 1:
            npcCR = toStr(2 * int(toInt(CR) / 3))
            newNpc = Npc(npcCR, envType)
            if newNpc.getShortDesc != "ERROR":
                self.npc = Npc(npcCR, envType)
                self.numMob = 1

        # Check current CR and scaling
        if self.npc != None:
            npcClass = self.npc.getShortDesc()
            currCR = toFlt([monster["CR"] for monster
                            in allMonsters
                            if monster["Name"] == npcClass][0])
            currScale = allCRScales[bisect(allCRScales, (self.numMob+1,))][1]
        else:
            currCR = 0.0
            currScale = 1.0

        # Add first monster
        maxInd = len(allCRs)
        while self.monsters == None:
            maxCR = int((toInt(CR)/currScale - currCR) / 2)
            newCR = random.choice(allCRs[1 if tier == 0 else 5 :
                                         6 + min(max(maxCR, 0), maxInd - 6)])
            self.monsters = [Monster(newCR, envType)]
            self.numMob += 1

        # Add monsters
        while (currCR*currScale < toInt(CR)) or (self.numMob < 2):
            maxCR = int((toInt(CR)/currScale - currCR) / 2)
            newCR = random.choice(allCRs[1 if tier == 0 else 5 :
                                         6 + min(max(maxCR, 0), maxInd - 6)])
            newMonster = Monster(newCR, envType)
            if newMonster.getShortDesc != "ERROR":
                self.monsters.append(newMonster)
                self.numMob += 1
                currCR += toFlt(newCR)
                currScale = allCRScales[bisect(allCRScales, (self.numMob+1,))][1]

    # Short description
    def getShortDesc(self):
        """ Build the short description """

        desc = ""
        # Npc
        if self.npc != None:
            desc += self.npc.getShortDesc()
            if self.numMob > 2:
                desc += ", "

        # Monsters
        for monster in self.monsters[:-1]:
            desc += monster.getShortDesc()
            if self.numMob > 2:
                desc += ", "
        if self.numMob == 2:
            desc += " "
        desc += "and "
        desc += self.monsters[-1].getShortDesc()

        # Check
        desc = replyCheck(desc)

        # Log
        if desc == "ERROR":
            print("Encounter Short Desc: ERROR")
        else:
            print("Encounter Short Desc: Success")

        # Return
        return desc

    # Long description
    def getLongDesc(self):
        """ Build the long description """

        desc = ""
        # Npc
        if self.npc != None:
            desc += "NPC: \n\t" + self.npc.getLongDesc() + "\n"
        # Monsters
        i = 1
        for monster in self.monsters:
            desc += "Monster " + str(i) + ":\n\t" + monster.getLongDesc() + "\n"
            i += 1

        # Check
        desc = replyCheck(desc)

        # Log
        if desc == "ERROR":
            print("Encounter Long Desc: ERROR")
        else:
            print("Encounter Long Desc: Success")

        # Return
        return desc

# ------------------------------------------------------------------------------
# PlotArc Class
# ------------------------------------------------------------------------------
class PlotArc(Module):
    """ PlotArc Class """
    npc = None   # NPC in the plot arc
    plot = ""    # Plot suggestion for the plot arc
    envType = "" # Environment type, if specified

    # Init
    def __init__(self, CR, envType):
        # Get random plot idea
        self.plot = random.choice(allPlots)

        # Build random NPC
        self.npc = Npc(CR, envType)

        # Set environment type, if specified
        self.envType = envType

    # Short description
    def getShortDesc(self):
        """ Build the short description """

        desc = ""
        # Npc
        desc += self.npc.getShortDesc()
        # Plot
        desc += " " + self.plot
        # Environment
        if self.envType:
            desc += " in the " + self.envType

        # Check
        desc = replyCheck(desc)

        # Log
        if desc == "ERROR":
            print("PlotArc Short Desc: ERROR")
        else:
            print("PlotArc Short Desc: Success")

        # Return
        return desc

    # Long description
    def getLongDesc(self):
        """ Build the long description """

        desc = ""
        # Npc
        desc += self.npc.getLongDesc() + ", "
        # Plot
        desc += " " + self.plot
        # Environment
        if self.envType:
            desc += " in the " + self.envType

        # Check
        desc = replyCheck(desc)

        # Log
        if desc == "ERROR":
            print("PlotArc Long Desc: ERROR")
        else:
            print("PlotArc Long Desc: Success")

        # Return
        return desc

# ------------------------------------------------------------------------------
