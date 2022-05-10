"""
	Auto DM

	Jeremy L Thompson

	This file provides module objects
"""
# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------

# Dictionaries
from .dictionaries import *

# Utilities
import random
from abc import ABC, abstractmethod
from bisect import bisect
from .utilities import *

# ------------------------------------------------------------------------------
# Base Class - Module
# ------------------------------------------------------------------------------


class Module:
	""" Module base class """

	@abstractmethod
	def get_short_description(self):
		""" Build the short description """
		pass

	@abstractmethod
	def get_long_description(self):
		""" Build the long description """
		pass

	def __repr__(self):
		return self.get_short_description()


# ------------------------------------------------------------------------------
# Monster Class
# ------------------------------------------------------------------------------


class Monster(Module):
	""" Monster Class """

	# Get monster by CR and/or environment
	def get_random_monster(self, cr, environment):
		""" Get a random monster by CR and environment """

		# Log
		debug_print("get_random_monster_name")
		debug_print("  cr: " + cr)
		debug_print("  environment: " + environment)

		monsters = ALL_MONSTERS
		# CR
		if cr != "":
			monsters = [monster for monster in monsters if cr == monster['CR']]
		# Environment
		if environment != "":
			monsters = [
			    monster for monster in monsters
			    if environment in monster['Env']
			]

		# Get random monster
		if len(monsters) == 0:
			monster = "ERROR: No suitable monster found"
			print(monster)
		else:
			monster = random.choice(monsters)

		# Return
		return monster

	# Init
	def __init__(self, cr, environment):
		""" Create new random monster

        >>> import random
        >>> random.seed(13)
        >>>
        >>> Monster("2", "")
        gargoyle
        """

		# Log
		debug_print("__init__ for Monster")

		self.type = "Monster"

		# Get random monster
		self._monster = self.get_random_monster(cr, environment)

		# Get HP
		if "ERROR" not in self._monster:
			self._name = self._monster['Name']
			self._hp = ALL_HP[self._monster['CR']]
		else:
			self._name = "ERROR: No suitable monster found"
			self._hp = "ERROR"

	# Short description
	def get_short_description(self):
		""" Build the short description

        >>> import random
        >>> random.seed(13)
        >>>
        >>> monster = Monster("2", "")
        >>> monster.get_short_description()
        'gargoyle'
        """

		# Log
		debug_print("get_short_description")

		# Build description
		description = self._name

		# Log
		debug_print("  description: " + description)

		# Return
		return description

	# Long description
	def get_long_description(self):
		""" Build the long description

        >>> import random
        >>> random.seed(13)
        >>>
        >>> monster = Monster("2", "")
        >>> monster.get_long_description()
        'gargoyle - HP: 86-100'
        """

		# Log
		debug_print("get_long_description")

		# Build description
		description = (self._name + " - HP: " + str(self._hp[0]) + "-" +
		               str(self._hp[1]))

		# Log
		debug_print("  description: " + description)

		# Return
		return description


# ------------------------------------------------------------------------------
# Npc Class
# ------------------------------------------------------------------------------


class Npc(Module):
	""" Npc Class """

	# Get NPC by CR and/or environment
	def get_random_npc_type(self, cr, environment):
		""" Get a random NPC type by CR and environment """

		# Log
		debug_print("get_random_npc_type")
		debug_print("  cr: " + cr)
		debug_print("  environment: " + environment)

		npcs = ALL_NPCs
		# CR
		if cr != "":
			npcs = [npc for npc in npcs if cr == npc['CR']]
		# Environment
		if environment != "":
			npcs = [npc for npc in npcs if environment in npc['Env']]

		# Get random NPC
		if len(npcs) == 0:
			npc_type = "ERROR: No suitable NPC found"
			print(npc_type)
		else:
			npc_type = random.choice(npcs)

		# Return
		return npc_type

	# Init
	def __init__(self, cr, environment):
		""" Create new random NPC

        >>> import random
        >>> random.seed(13)
        >>>
        >>> Npc("9", "")
        abjurer
        """

		# Log
		debug_print("__init__ for Npc")

		self.type = "Npc"

		# Get NPC type
		self._type = self.get_random_npc_type(cr, environment)
		if "ERROR" not in self._type:
			self._class = self._type['Name']
		else:
			self._class = "ERROR"

		# Get NPC name
		self._name = random.choice(ALL_NAMES)

	# Short description
	def get_short_description(self):
		""" Build the short description

        >>> import random
        >>> random.seed(13)
        >>>
        >>> npc = Npc("9", "")
        >>> npc.get_short_description()
        'abjurer'
        """

		# Log
		debug_print("get_short_description")

		# Build description
		description = self._class

		# Log
		debug_print("  description: " + description)

		# Return
		return description

	# Long description
	def get_long_description(self):
		""" Build the long description

        >>> import random
        >>> random.seed(13)
        >>>
        >>> npc = Npc("9", "")
        >>> npc.get_long_description()
        'Uthemar - abjurer'
        """

		# Log
		debug_print("get_long_description")

		# Build description
		description = self._name + " - " + self._class

		# Log
		debug_print("  NPC Long Description: " + description)

		# Return
		return description


# ------------------------------------------------------------------------------
# Encounter Class
# ------------------------------------------------------------------------------


class Encounter(Module):
	""" Encounter Class """

	# Init
	def __init__(self, cr, environment):
		""" Create new random Encounter

        >>> import random
        >>> random.seed(13)
        >>>
        >>> Encounter("", "urban")
        conjurer and meenlock
        """
		# Log
		debug_print("__init__ for Encounter")
		debug_print("  cr: " + cr)
		debug_print("  environment: " + environment)

		self.type = "Encounter"
		self._npc = None
		self._monsters = []
		self._number_monsters = 0

		# Pick random CR if no CR
		if cr == "":
			cr = to_string(random.randint(1, 20))

		# Get tier
		tier = to_int(cr) // 5
		if tier > 4:
			tier = 4

		# Add NPC, if tier 1+
		if tier >= 1:
			npc_cr = to_string(2 * int(to_int(cr) / 3))
			npc = Npc(npc_cr, environment)
			if npc.get_short_description != "ERROR":
				self._npc = Npc(npc_cr, environment)
				self._number_monsters = 1

		# Check current CR and scaling
		if self._npc is not None:
			current_cr = to_float(self._npc._type['CR'])
			current_scale = ALL_CR_SCALES[bisect(
			    ALL_CR_SCALES, (self._number_monsters + 1, ))][1]
		else:
			current_cr = 0.0
			current_scale = 1.0

		# Add monsters
		max_ind = len(ALL_CRs)
		while (current_cr * current_scale <
		       to_int(cr)) or (self._number_monsters < 2):
			max_cr = int((to_int(cr) / current_scale - current_cr) / 2)
			new_cr = random.choice(ALL_CRs[1 if tier == 0 else 5:6 +
			                               min(max(max_cr, 0), max_ind - 6)])
			new_monster = Monster(new_cr, environment)
			if new_monster.get_short_description != "ERROR":
				self._monsters.append(new_monster)
				self._number_monsters += 1
				current_cr += to_float(new_cr)
				current_scale = ALL_CR_SCALES[bisect(
				    ALL_CR_SCALES, (self._number_monsters + 1, ))][1]
			else:
				break

	# Short description
	def get_short_description(self):
		""" Build the short description

        >>> import random
        >>> random.seed(13)
        >>>
        >>> encounter = Encounter("19", "")
        >>> encounter.get_short_description()
        'archdruid and ettercap'
        """

		# Log
		debug_print("get_short_description")

		description = ""

		# NPC
		if self._npc is not None:
			description += self._npc.get_short_description()
			if self._number_monsters > 2:
				description += ", "

		# Monsters
		for monster in self._monsters[:-1]:
			description += monster.get_short_description()
			if self._number_monsters > 2:
				description += ", "
		if self._number_monsters == 2:
			description += " "
		description += "and "
		description += self._monsters[-1].get_short_description()

		# Log
		debug_print("  Encounter Short Description: " + description)

		# Return
		return description

	# Long description
	def get_long_description(self):
		""" Build the long description

        >>> import random
        >>> random.seed(13)
        >>>
        >>> encounter = Encounter("19", "")
        >>> encounter.get_long_description()
        'NPC: \\n\\tForcas - archdruid\\nMonster 1:\\n\\tettercap - HP: 86-100\\n'
        """

		# Log
		debug_print("get_long_description")

		description = ""

		# Npc
		if self._npc is not None:
			description += ("NPC: \n\t" + self._npc.get_long_description() +
			                "\n")

		# Monsters
		i = 1
		for monster in self._monsters:
			description += ("Monster " + str(i) + ":\n\t" +
			                monster.get_long_description() + "\n")
			i += 1

		# Log
		debug_print("  Encounter Long Description: " + description)

		# Return
		return description


# ------------------------------------------------------------------------------
# PlotArc Class
# ------------------------------------------------------------------------------


class PlotArc(Module):
	""" PlotArc Class """

	# Init
	def __init__(self, cr, environment):
		""" Create new random Plot Arc

        >>> import random
        >>> random.seed(13)
        >>>
        >>> PlotArc("9", "")
        abjurer is trying to place a pawn in a position of power
        """

		# Log
		debug_print("__init__ for PlotArc")

		self.type = "Plot Arc"

		# Get random plot idea
		self._plot = random.choice(ALL_PLOTS)

		# Build random NPC
		self._npc = Npc(cr, environment)

		# Set environment type, if specified
		self._environment = environment

	# Short description
	def get_short_description(self):
		""" Build the short description

        >>> import random
        >>> random.seed(13)
        >>>
        >>> arc = PlotArc("9", "")
        >>> arc.get_short_description()
        'abjurer is trying to place a pawn in a position of power'
        """

		# Log
		debug_print("get_short_description")

		description = ""

		# NPC
		description += self._npc.get_short_description()

		# Plot
		description += " " + self._plot

		# Environment
		if self._environment:
			description += " in the " + self._environment

		# Log
		debug_print("  Plot Arc Short Desc: " + description)

		# Return
		return description

	# Long description
	def get_long_description(self):
		""" Build the long description

        >>> import random
        >>> random.seed(13)
        >>>
        >>> arc = PlotArc("9", "")
        >>> arc.get_long_description()
        'Arnbjorg - abjurer,  is trying to place a pawn in a position of power'
        """

		# Log
		debug_print("get_long_description")

		description = ""

		# NPC
		description += self._npc.get_long_description() + ", "

		# Plot
		description += " " + self._plot

		# Environment
		if self._environment:
			description += " in the " + self._environment

		# Log
		debug_print("  Plot Arc Long Desc: " + description)

		# Return
		return description


# ------------------------------------------------------------------------------
# Get Module from intent
# ------------------------------------------------------------------------------


def get_module_args_from_intent_name(intent_name):
	""" Parses intent name

    >>> get_module_args_from_intent_name("MonsterByCRandEnvironment")
    (True, True, 'Monster')

    >>> get_module_args_from_intent_name("NpcByCR")
    (True, False, 'Npc')

    >>> get_module_args_from_intent_name("EncounterByCRandEnvironment")
    (True, True, 'Encounter')

    >>> get_module_args_from_intent_name("PlotArcByEnvironment")
    (False, True, 'Plot Arc')
    """

	# Log
	debug_print("get_intent_args")
	debug_print("  intent_name: " + intent_name)

	# Get argument flags
	# - CR
	has_cr = "CR" in intent_name

	# - Environment
	has_environment = "Environment" in intent_name

	# - Module Type
	module_type = ""
	if "Monster" in intent_name:
		module_type = "Monster"
	elif "Npc" in intent_name:
		module_type = "Npc"
	elif "Encounter" in intent_name:
		module_type = "Encounter"
	elif "PlotArc" in intent_name:
		module_type = "Plot Arc"

	return has_cr, has_environment, module_type


# ------------------------------------------------------------------------------


def module_from_intent(intent):
	# Log
	debug_print("module_from_intent")

	# Break down name into type, CR, and environment
	has_cr, has_environment, module_type = get_module_args_from_intent_name(
	    intent['Name'])

	cr = ""
	if has_cr:
		try:
			cr = intent['slots']['cr']['value']
			# Amazon rudely uses non-ASCII characters
			cr = moduleCR.replace('⁄', '/')
		except BaseException:
			return "ERROR: No CR found"

	environment = ""
	if has_environment:
		try:
			environment = intent['slots']['env']['value']
		except BaseException:
			return "ERROR: No environment found"

	# Log
	debug_print("  module_type: " + module_type)
	debug_print("  cr: " + cr)
	debug_print("  environment: " + environment)

	# Module object
	if module_type == "Monster":
		return Monster(cr, environment)
	elif module_type == "Npc":
		return Npc(cr, environment)
	elif module_type == "Encounter":
		return Encounter(cr, environment)
	elif module_type == "Plot Arc":
		return PlotArc(cr, environment)
	else:
		return "ERROR: No suitable module found"


# ------------------------------------------------------------------------------
