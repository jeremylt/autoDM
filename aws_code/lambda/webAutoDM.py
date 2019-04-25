"""
    Web Auto DM

    Jeremy L Thompson

    This code provides a website Auto DM for tabletop RPG games that provides
    monsters within given specifications (Challenge Rating and Environment).
"""
# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------

# Utility
import sys
sys.path.append('./utility')
from utility import *

# ------------------------------------------------------------------------------
# Response helper, written/rewritten by Jeremy L Thompson
# ------------------------------------------------------------------------------
def build_web_response(text_output):
    """ Build the web response """

    return { 'body' : text_output }

# ------------------------------------------------------------------------------
# Web intent, written/rewritten by Jeremy L Thompson
# ------------------------------------------------------------------------------
def on_web_intent(intent):
    """ Get a random omdule at the specified CR or env from the specified
    environment for the web interace """

    # Log
    print("module_in_web_session: " + intent['name'])

    # Get response
    sessionType, text_output = get_intent_reply(intent, "Web")

    # Return the web response JSON
    if text_output != "ERROR":
        return build_web_response(text_output)
    else:
        return build_web_response("I'm sorry, nothing matches what you want.\n"\
                                  "Would you like to try again?")

# ------------------------------------------------------------------------------
# Web Handler, written/rewritten by Jeremy L Thompson
# ------------------------------------------------------------------------------
def web_lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter. """

    # Log
    print("web_lambda_handler source ip= " + event['ip'])

    # Handle web request
    return on_web_intent(event)

# ------------------------------------------------------------------------------
