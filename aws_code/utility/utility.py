# coding=utf8
"""
    Auto DM

    Jeremy L Thompson

    This is a utility function for the web and Alexa lambda handlers.
"""

# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------

# AutoDM backend
import sys
sys.path.append('./backend')
from session import *

# ------------------------------------------------------------------------------
# Utility functions, written by Jeremy L Thompson
# ------------------------------------------------------------------------------
def get_intent_args(intent_name):
    """ Parses intent name """

    # Get argument flags
    # - CR
    crFlag = 0
    if "CR" in intent_name:
        crFlag = 1
    # Environment
    envFlag = 0
    if "Environment" in intent_name:
        envFlag = 1
    # Session Type
    sessionType = ""
    if "Monster" in intent_name:
        sessionType = "Monster"
    elif "Npc" in intent_name:
        sessionType = "Npc"
    elif "Encounter" in intent_name:
        sessionType = "Encounter"
    elif "PlotArc" in intent_name:
        sessionType = "PlotArc"

    return crFlag, envFlag, sessionType

# ------------------------------------------------------------------------------
def get_intent_reply(intent, communicatorType):
    """ Get a module response based on intent and communicator type """

    # Get crFlag, envFlag, and sessionType
    crFlag, envFlag, sessionType = get_intent_args(intent['name'])

    # Get CR and Env
    try:
        moduleCR      = intent['slots']['cr']['value']
        # Amazon rudely uses non-ASCII characters
        moduleCR      = moduleCR.replace('⁄', '/')
    except:
        if crFlag:
            return sessionType, "ERROR"
        else:
            moduleCR  = ""
    try:
        moduleEnv     = intent['slots']['env']['value']
    except:
        if envFlag:
            return sessionType, "ERROR"
        else:
            moduleEnv = ""

    # Log
    print("get_intent_reply: sessionType - " + sessionType +
          ", communicatorType - " + communicatorType + ", moduleCR - " +
          moduleCR + ", moduleEnv - " + moduleEnv)

    # Get reply
    currSession       = Session(sessionType, communicatorType, moduleCR,
                                moduleEnv)
    sessionReply      = currSession.buildReply()

    return sessionType, sessionReply

# ------------------------------------------------------------------------------
