"""
	Auto DM

	Jeremy L Thompson

	This is the lambda handler for Alexa and web requests.
"""
# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------

# Alexa and web lambda handlers
from lambdaHandlers import alexa_lambda_handler, web_lambda_handler

# ------------------------------------------------------------------------------
# Initial handler
# ------------------------------------------------------------------------------


def lambda_handler(event, context):
	""" Determine if Alexa or Web request and pass to correct handler """

	# Check for web reqest
	is_web_event = 'web' in event.keys()
	if is_web_event:
		return web_lambda_handler(event, context)
	else:
		return alexa_lambda_handler(event, context)


# ------------------------------------------------------------------------------
