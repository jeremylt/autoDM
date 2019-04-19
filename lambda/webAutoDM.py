"""
    Web Auto DM

    Jeremy L Thompson

    This code provides a website Auto DM for tabletop RPG games that provides
    monsters within given specifications (Challenge Rating and Environment).
"""
# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------

# AutoDM backend
import sys
sys.path.append('./backend')
sys.path.append('./utility')
from session import *
# Utility
from utility import *

# ------------------------------------------------------------------------------
# Response helper, written/rewritten by Jeremy L Thompson
# ------------------------------------------------------------------------------
def build_web_response(text_output):
    """ Build the web response """

    return { 'module_text' : text_output }

# ------------------------------------------------------------------------------
# Web Responses, written/rewritten by Jeremy L Thompson
# ------------------------------------------------------------------------------
def web_session(intent, sessionType, crFlag, envFlag):
    """ Get a random monster at the specified CR from the specified
    environment """

    # Get CR and Env
    try:
        moduleCR          = intent['cr']
    except:
        if crFlag:
            moduleCR      = "ERROR"
        else:
            moduleCR      = ""
    try:
        moduleEnv         = intent['env']
    except:
        if envFlag:
            moduleEnv     = "ERROR"
        else:
            moduleEnv     = ""

    # Log
    print("module_in_web_session: sessionType - " + sessionType +
          ", moduleCR - " + moduleCR + ", moduleEnv - " + moduleEnv)

    # Build reply
    if moduleCR != "ERROR" and moduleEnv != "ERROR":
        webSession        = Session(sessionType, "Web", moduleCR, moduleEnv)
        text_output       = webSession.buildReply()

    # Return the web response JSON
    return build_web_response(text_output)

# ------------------------------------------------------------------------------
# Web intent, written/rewritten by Jeremy L Thompson
# ------------------------------------------------------------------------------
def on_web_intent(intent_request):
    """ Called when the user specifies an intent for the web """

    # Get intent name
    intent_name = intent_request['name']

    # Log
    print("on_web_intent")
    print(intent_name)

    # Get argument flags
    crFlag, envFlag, sessionType = get_intent_args(intent_name)

    # Dispatch to the backend
    return web_session(intent_request, sessionType, crFlag, envFlag)

# ------------------------------------------------------------------------------
# Web Handler, written/rewritten by Jeremy L Thompson
# ------------------------------------------------------------------------------
def web_lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter. """

    # Log
    print("web_lambda_handler source ip=" + event['context']['source-ip'])

    # Handle web request
    return on_web_intent(event['params']['querystring'])

# ------------------------------------------------------------------------------
