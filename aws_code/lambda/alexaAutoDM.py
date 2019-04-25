"""
    Alexa Auto DM

    Jeremy L Thompson

    This code provides an Alexa Auto DM for tabletop RPG games that provides
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
# Response Card Helpers, code From Alexa Tutorial, modified by Jeremy L Thompson
# ------------------------------------------------------------------------------
def build_speechlet_response(title, output, reprompt_text, should_end_session):
    """ Build the Alexa speechlet response """

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

    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }

# ------------------------------------------------------------------------------
# Skill Responses, written/rewritten by Jeremy L Thompson
# ------------------------------------------------------------------------------
def get_welcome_response():
    """ Welcome response describes how to use the Alexa skill """

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
    return build_response(session_attributes,
                          build_speechlet_response(card_title,
                                                   speech_output,
                                                   reprompt_text,
                                                   should_end_session))

# ------------------------------------------------------------------------------
def get_help_response():
    """ Help response """

    # Build cart title
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
    return build_response(session_attributes,
                          build_speechlet_response(card_title,
                                                   speech_output,
                                                   reprompt_text,
                                                   should_end_session))

# ------------------------------------------------------------------------------
def handle_session_end_request():
    """ Session end response """

    # Build card title
    card_title = "Session Ended"

    # Session details
    session_attributes = {}

    # Response
    speech_output = "Thank you for using the Auto Game Master! "

    # Flag session end
    should_end_session = True

    # Return the Alexa response JSON
    return build_response(session_attributes,
                          build_speechlet_response(card_title,
                                                   speech_output,
                                                   None,
                                                   should_end_session))

# ------------------------------------------------------------------------------
def module_in_alexa_session(intent, session):
    """ Get a random module at the specified CR or env from the specified
    environment for the Alexa inteface """

    # Log
    print("module_in_alexa_session: " + intent['name'])

    # Get response
    sessionType, speech_output = get_intent_reply(intent, "Alexa")

    # Build card title
    card_title = "Random " + sessionType
    if "CR" in intent['name']:
        card_title       += " By CR"
        if "Env" in intent['name']:
            card_title   += " and Environment"
    elif "Env" in intent['name']:
        card_title       += " By Environment"

    # Session details
    session_attributes    = {}
    should_end_session    = False

    # Build reply
    if sessionType == "Npc":
        sessionLow        = "N P C"
    elif sessionType == "PlotArc":
        sessionLow        = "plot arc"
    else:
        sessionLow        = sessionType.lower()
    if speech_output != "ERROR":
        reprompt_text     = "Would you like another " + sessionLow + "?"
    else:
        speech_output     = "I'm not sure what type of " + sessionLow + \
                            " you want.\n\nPlease try again."
        reprompt_text     = "I'm not sure what type of " + sessionLow + \
                            " you want.\n\n" \
                            "You can say 'Give me a C R 1 monster', " \
                            "'Give me a swamp N P C', or " \
                            "'I want a plot arc'."

    # Return the Alexa response JSON
    return build_response(session_attributes,
                          build_speechlet_response(card_title,
                                                   speech_output,
                                                   reprompt_text,
                                                   should_end_session))

# ------------------------------------------------------------------------------
# Events, code from Alexa tutorial, modified by Jeremy L Thompson
# ------------------------------------------------------------------------------
def on_session_started(session_started_request, session):
    """ Called when the session starts """

    # Log
    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])

# ------------------------------------------------------------------------------
def on_launch(launch_request, session):
    """ User launched the skill without specifying intent """

    # Log
    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    # Dispatch to the skill's launch
    return get_welcome_response()

# ------------------------------------------------------------------------------
def on_alexa_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    # Get intent
    intent      = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Log
    print("on_alexa_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    print(intent_name)

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
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    # Cleanup logic would go here

# ------------------------------------------------------------------------------
# Alexa Handler, code from Alexa tutorial, modified by Jeremy L Thompson
# ------------------------------------------------------------------------------
def alexa_lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter. """

    # Log
    print("event.session.application.applicationId=" +
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
