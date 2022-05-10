"""
	Alexa Auto DM

	Jeremy L Thompson

	This code provides an Alexa Auto DM for tabletop RPG games that provides
	monsters within given specifications (Challenge Rating and Environment).
"""
# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------

# Supporting modules
from .communicators import AlexaCommunicator
from .modules import module_from_intent

# ------------------------------------------------------------------------------
# Response card helpers
# ------------------------------------------------------------------------------


def build_speechlet_response(title, output, reprompt_text, should_end_session):
	""" Build the Alexa speechlet response """

	# Log
	debug_print("build_speechlet_response")
	debug_print("  title: " + title)
	debug_print("  output: " + output)
	debug_print("  reprompt_text: " + reprompt_text)
	debug_print("  should_end_session: + should_end_session")

	return {
	    'outputSpeech': {
	        'type': 'PlainText',
	        'text': output
	    },
	    'card': {
	        'type': 'Simple',
	        'title': title,
	        'content': output
	    },
	    'reprompt': {
	        'outputSpeech': {
	            'type': 'PlainText',
	            'text': reprompt_text
	        }
	    },
	    'shouldEndSession': should_end_session
	}


# ------------------------------------------------------------------------------


def build_response(session_attributes, speechlet_response):
	""" Build the Alexa response """

	# Log
	debug_print("build_response")

	return {
	    'version': '1.0',
	    'sessionAttributes': session_attributes,
	    'response': speechlet_response
	}


# ------------------------------------------------------------------------------
# Skill responses
# ------------------------------------------------------------------------------


def get_welcome_response():
	""" Welcome response describes how to use the Alexa skill """

	# Log
	debug_print("get_welcome_response")

	# Build card title
	card_title = "Welcome"

	# Session details
	session_attributes = {}

	# Response
	speech_output = "Welcome to the Auto Game Master!\n\n" \
                          "How do you want to do this?"

	# If the user either does not reply to the welcome message or says something
	# that is not understood, they will be prompted again with this text.
	reprompt_text = "What type of module would you like?\n\n" \
                          "You can say 'Give me a C R 1 monster', " \
                          "'Give me a swamp N P C', or " \
                          "'I want a plot arc.'"

	should_end_session = False

	# Return the Alexa response JSON
	return build_response(
	    session_attributes,
	    build_speechlet_response(card_title, speech_output, reprompt_text,
	                             should_end_session))


# ------------------------------------------------------------------------------


def get_help_response():
	""" Help response """

	# Log
	debug_print("get_help_response")

	# Build card title
	card_title = "Help"

	# Session details
	session_attributes = {}

	# Response
	speech_output = "You can request a monster, N P C, encounter, or plot " \
                          " arc by challenge rating, environment, or both.\n\n" \
                          "For example, you can say 'Give me a C R 1 monster', " \
                          "'Give me a swamp N P C', or " \
                          "'I want a plot arc'.\n\n" \
                          "What type of module would you like?"

	# Reprompt text
	reprompt_text = "What type of module would you like? \n\n" \
                          "You can say 'Give me a C R 1 monster', " \
                          "'Give me a swamp N P C', or " \
                          "'I want a plot arc'."

	should_end_session = False

	# Return the Alexa response JSON
	return build_response(
	    session_attributes,
	    build_speechlet_response(card_title, speech_output, reprompt_text,
	                             should_end_session))


# ------------------------------------------------------------------------------


def handle_session_end_request():
	""" Session end response """

	# Log
	debug_print("handle_session_end_request")

	# Build card title
	card_title = "Session Ended"

	# Session details
	session_attributes = {}

	# Response
	speech_output = "Thank you for using the Auto Game Master!"

	# Flag session end
	should_end_session = True

	# Return the Alexa response JSON
	return build_response(
	    session_attributes,
	    build_speechlet_response(card_title, speech_output, None,
	                             should_end_session))


# ------------------------------------------------------------------------------


def module_in_alexa_session(intent, session):
	""" Get a random module at the specified CR or env from the specified
    environment for the Alexa inteface """

	# Log
	debug_print("module_in_alexa_session: " + intent['name'])

	# Get response
	comm = AlexaCommunicator()
	module = module_from_intent(intent)
	speech_output = comm.build_reply(module)

	# Build reply
	module_type_spoken = "response" if "ERROR" in module else module.type.lower(
	)
	if module_type_spoken == "npc":
		module_type_spoken = "N P C"

	# Build card title
	card_title = "Random " + module_type_spoken
	if "CR" in intent['name']:
		card_title += " By CR"
		if "Env" in intent['name']:
			card_title += " and Environment"
	elif "Env" in intent['name']:
		card_title += " By Environment"

	# Session details
	session_attributes = {}
	should_end_session = False

	if "ERROR" in speech_output:
		speech_output = "I'm not sure what type of " + module_type_spoken + \
                                                " you want.\n\nPlease try again."
		reprompt_text = "I'm not sure what type of " + module_type_spoken + \
                                                " you want.\n\n" \
                                                "You can say 'Give me a C R 1 monster', " \
                                                "'Give me a swamp N P C', or " \
                                                "'I want a plot arc'."
	else:
		reprompt_text = "Would you like another " + module_type_spoken + "?"

	# Return the Alexa response JSON
	return build_response(
	    session_attributes,
	    build_speechlet_response(card_title, speech_output, reprompt_text,
	                             should_end_session))


# ------------------------------------------------------------------------------
# Events
# ------------------------------------------------------------------------------


def on_session_started(session_started_request, session):
	""" Called when the session starts """

	# Log
	debug_print("on_session_started")
	debug_print("  requestId: " + session_started_request['requestId'])
	debug_print("  sessionId: " + session['sessionId'])

	# Startup logic would go here, but none needed currently


# ------------------------------------------------------------------------------


def on_launch(launch_request, session):
	""" User launched the skill without specifying intent """

	# Log
	debug_print("on_launch")
	debug_print("  requestId: " + launch_request['requestId'])
	debug_print("  sessionId: " + session['sessionId'])

	# Dispatch to the skill's launch
	return get_welcome_response()


# ------------------------------------------------------------------------------


def on_alexa_intent(intent_request, session):
	""" Called when the user specifies an intent for this skill """

	# Get intent
	intent = intent_request['intent']
	intent_name = intent_request['intent']['name']

	# Log
	debug_print("on_alexa_intent")
	debug_print("  requestId: " + intent_request['requestId'])
	debug_print("  sessionId: " + session['sessionId'])
	debug_print("  intent_name: " + intent_name)

	# Dispatch to the skill's intent handlers
	if "By" in intent_name:
		return module_in_alexa_session(intent, session)
	elif intent_name == "AMAZON.HelpIntent":
		return get_help_response()
	elif intent_name == "AMAZON.CancelIntent" or \
                              intent_name == "AMAZON.StopIntent":
		return handle_session_end_request()
	else:
		raise ValueError("Invalid intent")


# ------------------------------------------------------------------------------


def on_session_ended(session_ended_request, session):
	""" Called when user ends the session, except when skill returns
            should_end_session=true """

	# Log
	debug_print("on_session_ended")
	debug_print("  requestId: " + session_ended_request['requestId'])
	debug_print("  sessionId: " + session['sessionId'])

	# Cleanup logic would go here, but none needed currently


# ------------------------------------------------------------------------------
# Alexa handler
# ------------------------------------------------------------------------------


def alexa_lambda_handler(event, context):
	""" Route the incoming request based on type (LaunchRequest, IntentRequest, etc.)
     The JSON body of the request is provided in the event parameter. """

	# Log
	debug_print("alexa_lambda_handler")
	debug_print("  applicationId: " +
	            event['session']['application']['applicationId'])

	# Start session if new
	if event['session']['new']:
		on_session_started({'requestId': event['request']['requestId']},
		                   event['session'])

	# Handle event type
	if event['request']['type'] == "LaunchRequest":
		return on_launch(event['request'], event['session'])
	elif event['request']['type'] == "IntentRequest":
		return on_alexa_intent(event['request'], event['session'])
	elif event['request']['type'] == "SessionEndedRequest":
		return on_session_ended(event['request'], event['session'])


# ------------------------------------------------------------------------------
