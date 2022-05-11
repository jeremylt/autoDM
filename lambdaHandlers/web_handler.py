"""
	Web Auto DM

	Jeremy L Thompson

	This code provides a website Auto DM for tabletop RPG games that provides
	monsters within given specifications (Challenge Rating and Environment).
"""
# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------

# Supporting modules
from .communicators import WebCommunicator
from .modules import module_from_intent

# ------------------------------------------------------------------------------
# Response helper
# ------------------------------------------------------------------------------


def build_web_response(text_output):
	""" Build the web response """

	return {'body': text_output}


# ------------------------------------------------------------------------------
# Web intent
# ------------------------------------------------------------------------------


def on_web_intent(intent):
	""" Get a random module at the specified CR and/or environment for the web interface """

	# Log
	debug_print("on_web_intent")
	debug_print(" name: " + intent['name'])

	# Get response
	comm = WebCommunicator()
	module = module_from_intent(intent)
	text_output = comm.build_reply(module)

	# Return the web response JSON
	if is_error_string(text_output):
		return build_web_response(
		    "I'm sorry, nothing matches what you want.\n Would you like to try again?"
		)
	else:
		return build_web_response(text_output)


# ------------------------------------------------------------------------------
# Web handler
# ------------------------------------------------------------------------------


def web_lambda_handler(event, context):
	""" Route the incoming request based on type.
    The JSON body of the request is provided in the event parameter. """

	# Log
	debug_print("web_lambda_handler")
	debug_print("  source ip: " + event['ip'])

	# Handle web request
	return on_web_intent(event)


# ------------------------------------------------------------------------------
