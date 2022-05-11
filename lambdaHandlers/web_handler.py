"""
	Web lambda handler

	This code provides the lambda handler for requests from  websites.
"""
# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------

# Supporting modules
from lambdaHandlers.communicators import WebCommunicator
from lambdaHandlers.modules import module_from_intent
from lambdaHandlers.utilities import *

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
	""" Get a random module at the specified CR and/or environment for the web interface

	>>> import random
	>>> random.seed(13)
	>>> # valid monster intent
	>>> monster_intent = {
	...		'web': True,
	...		'ip': "2001:0db8:85a3:0000:0000:8a2e:0370:7334",
	...		'name': "MonsterByCRandEnvironment",
	...		'slots': {
	...			'cr': {'value': "2"},
	...			'env': {'value': "swamp"}
	...		}
	...	}
	>>> on_web_intent(monster_intent)
	{'body': '--- Random Monster ---\\nswarm of poisonous snakes - HP: 86-100'}
	"""

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
    The JSON body of the request is provided in the event parameter.

	>>> import random
	>>> random.seed(13)
	>>> # valid monster intent
	>>> monster_intent = {
	...		'web': True,
	...		'ip': "2001:0db8:85a3:0000:0000:8a2e:0370:7334",
	...		'name': "MonsterByCRandEnvironment",
	...		'slots': {
	...			'cr': {'value': "2"},
	...			'env': {'value': "swamp"}
	...		}
	...	}
	>>> web_lambda_handler(monster_intent, "")
	{'body': '--- Random Monster ---\\nswarm of poisonous snakes - HP: 86-100'}
	"""

	# Log
	debug_print("web_lambda_handler")
	debug_print("  source ip: " + event['ip'])

	# Handle web request
	return on_web_intent(event)


# ------------------------------------------------------------------------------
