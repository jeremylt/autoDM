"""
    Auto DM

    Jeremy L Thompson

    This is the lambda handler for Alexa and web requests.
"""
# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------

# Alexa and web lambda handlers
import sys
sys.path.append('./lambda')
from alexaAutoDM import *
from webAutoDM import *

# ------------------------------------------------------------------------------
# Main Handler, written/rewritten by Jeremy L Thompson
# ------------------------------------------------------------------------------
def lambda_handler(event, context):
    """ Determine if Alexa or Web request """

    # Check for web reqest
    try:
      web = event['params']['querystring']['web']
      # Web request
      return web_lambda_handler(event, context)
    except:
      # Alexa request
      return alexa_lambda_handler(event, context)

# ------------------------------------------------------------------------------
