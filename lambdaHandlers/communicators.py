"""
	Auto DM

	Jeremy L Thompson

	This file provides communicator objects
"""
# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------

# Utilities
from abc import ABC, abstractmethod
from .utilities import *

# ------------------------------------------------------------------------------
# Base Class - Communicator
# ------------------------------------------------------------------------------


class Communicator:
	""" Communicator base class """

	@abstractmethod
	def build_reply(module):
		""" Build the Reply """
		pass


# ------------------------------------------------------------------------------
# AlexaCommunicator Class
# ------------------------------------------------------------------------------


class AlexaCommunicator(Communicator):
	""" AlexaCommunicator Class """

	def get_error_message(self, error):
		""" Standard error message """

		# Log
		print("Alexa Reply: " + error)
		# Return
		return ("I'm sorry, nothing matches what you want.\n\n"
		        "Would you like to try again?")

	def build_reply(self, module):
		""" Build the Reply

        >>> import random
        >>> random.seed(13)
        >>>
        >>> from lambdaHandlers.modules import Npc
        >>> module = Npc("", "grassland")
        >>>
        >>> comm = AlexaCommunicator()
        >>> comm.build_reply(module)
        'A centaur confronts you!\\n\\nWould you like another N P C?'
        """

		# Log
		debug_print("build_reply")
		debug_print("  AlexaCommunicator")

		# Input checking
		if type(module) == 'string' and "ERROR" in module:
			return self.get_error_message(module)

		# Module description
		reply = module.get_short_description()

		# Error checking
		if "ERROR" in reply:
			return self.get_error_message(reply)

		# Front matter
		if reply[0] in ['a', 'e', 'i', 'o', 'u']:
			reply = "An " + reply
		elif reply[:3] != "the":
			reply = "A " + reply
		else:
			reply = "T" + reply[1:]

		# End matter
		if module.type == "Monster":
			reply += " attacks!\n\nWould you like another monster?"
		elif module.type == "Npc":
			reply += " confronts you!\n\nWould you like another N P C?"
		elif module.type == "Encounter":
			reply += " attack!\n\nWould you like another encounter?"
		else:
			reply += ".\n\nWould you like another plot arc?"

		# Log
		debug_print("Alexa Reply: Success")

		# Return
		return reply


# ------------------------------------------------------------------------------
# WebCommunicator Class
# ------------------------------------------------------------------------------


class WebCommunicator(Communicator):
	""" WebCommunicator Class """

	def get_error_message(self, error):
		""" Standard error message """

		# Log
		print("Web Reply: " + error)
		# Return
		return ("I'm sorry, nothing matches what you want.\n"
		        "Would you like to try again?")

	def build_reply(self, module):
		""" Build the Reply

        >>> import random
        >>> random.seed(13)
        >>>
        >>> from lambdaHandlers.modules import Monster
        >>> module = Monster("", "swamp")
        >>>
        >>> comm = WebCommunicator()
        >>> comm.build_reply(module)
        '--- Random Monster ---\\ntroll - HP: 131-145'
        """

		# Log
		debug_print("build_reply")
		debug_print("  WebCommunicator")

		# Input checking
		if type(module) == 'string' and "ERROR" in module:
			return self.get_error_message(module)

		# Front matter
		reply = "--- Random "
		reply += module.type + " ---\n"

		# Module description
		reply += module.get_long_description()

		# Error checking
		if "ERROR" in reply:
			return self.get_error_message(reply)

		# Log
		debug_print("Web Reply: Success")

		# Return
		return reply


# ------------------------------------------------------------------------------
