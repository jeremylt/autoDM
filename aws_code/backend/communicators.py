"""
    Auto DM

    Jeremy L Thompson

    This file provides communicator objects
"""
# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------

# Utility
from abc import ABC, abstractmethod

# ------------------------------------------------------------------------------
# Base Class - Communicator
# ------------------------------------------------------------------------------
class Communicator:
    """ Communicator base class """

    @abstractmethod
    def buildReply(module, sessionType):
        """ Build the Reply """
        pass

# ------------------------------------------------------------------------------
# AlexaCommunicator Class
# ------------------------------------------------------------------------------
class AlexaCommunicator(Communicator):
    """ AlexaCommunicator Class """

    def buildReply(self, module, sessionType):
        """ Build the Reply """

        # Module description
        reply = module.getShortDesc()

        # Front matter
        if reply[0] in {'a', 'e', 'i', 'o', 'u'}:
            reply = "An " + reply
        elif reply[:3] != "the":
            reply = "A " + reply
        else:
            reply = "T" + reply[1:]

        # End matter
        if sessionType == "Monster":
            reply += " attacks!\n\nWould you like another monster?"
        elif sessionType == "Npc":
            reply += " confronts you!\n\nWould you like another N P C?"
        elif sessionType == "Encounter":
            reply += " attack!\n\nWould you like another encounter?"
        else:
            reply += ".\n\nWould you like another plot arc?"

        # Error checking
        if "ERROR" in reply:
            # Log
            print("Alexa Reply: ERROR")
            # Return
            return "I'm sorry, nothing matches what you want.\n\n" \
                   "Would you like to try again?"

        # Log
        print("Alexa Reply: Success")

        # Return
        return reply

# ------------------------------------------------------------------------------
# WebCommunicator Class
# ------------------------------------------------------------------------------
class WebCommunicator(Communicator):
    """ WebCommunicator Class """

    def buildReply(self, module, sessionType):
        """ Build the Reply """

        # Front matter
        reply = "--- Random "
        reply += sessionType + " ---\n"

        # Module description
        reply += module.getLongDesc()

        # Error checking
        if "ERROR" in reply:
            # Log
            print("Web Reply: ERROR")
            # Return
            return "I'm sorry, nothing matches what you want.\n" \
                   "Would you like to try again?"

        # Log
        print("Web Reply: Success")


        # Return
        return reply

# ------------------------------------------------------------------------------
