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
	try:
		# Web request
		is_web_event = event['web']
		return web_lambda_handler(event, context)
	except:
		# Alexa request
		return alexa_lambda_handler(event, context)


# ------------------------------------------------------------------------------
