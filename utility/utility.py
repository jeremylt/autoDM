"""
    Auto DM

    Jeremy L Thompson

    This is a utility function for the web and Alexa lambda handlers.
"""

# ------------------------------------------------------------------------------
# Utility function, written by Jeremy L Thompson
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
