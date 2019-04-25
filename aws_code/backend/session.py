"""
    Auto DM

    Jeremy L Thompson

    This file provides session objects
"""
# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------

# Objects
from communicators import *
from modules import *
import bisect

# ------------------------------------------------------------------------------
# Session Class
# ------------------------------------------------------------------------------
class Session:
    """ Session class """
    module = None    # Random module for the session
    comm = None      # Communicator for the session
    sessionType = "" # Type of session (type of module)

    def __init__(self, sessionType, commType, CR, envType):
        # Communicator
        if commType == "Alexa":
            self.comm = AlexaCommunicator()
        else:
            self.comm = WebCommunicator()

        # Session object
        self.sessionType = sessionType
        if sessionType == "Monster":
            self.module = Monster(CR, envType)
        elif sessionType == "Npc":
            self.module = Npc(CR, envType)
        elif sessionType == "Encounter":
            self.module = Encounter(CR, envType)
        elif sessionType == "PlotArc":
            self.module = PlotArc(CR, envType)
        else:
            pass

    def buildReply(self):
        """ Build the Reply """

        # Build reply if module is found
        if self.module:
            reply = self.comm.buildReply(self.module, self.sessionType)
        else:
            reply = "Invalid Module"

        # Log
        print("Session Reply:\n" + reply)

        # Return
        return(reply)

# ------------------------------------------------------------------------------
