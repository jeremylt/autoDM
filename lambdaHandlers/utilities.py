# coding=utf8
"""
	Utilities

	This code provides utility functions used throughout the module.
"""

# ------------------------------------------------------------------------------
# Utility functions
# ------------------------------------------------------------------------------

# Set IS_DEBUG = True for troubleshooting or False for production
IS_DEBUG = False


def debug_print(*args):
	""" Print if in debugging mode """
	if (IS_DEBUG):
		print(*args)


# ------------------------------------------------------------------------------


def is_error_string(return_value):
	""" Check if return value is error message

	>>> is_error_string(42)
	False
	>>> is_error_string("Some message")
	False
	>>> is_error_string("ERROR: some error message")
	True
    """

	return isinstance(return_value, str) and return_value.find("ERROR") != -1


# ------------------------------------------------------------------------------


def to_int(string):
	""" Convert string to int

    >>> to_int("42")
    42
    """

	try:
		number = int(float(string))
	except:
		number = 0

	return number


# ------------------------------------------------------------------------------


def to_float(string):
	""" Convert string to float

    >>> to_float("42.0")
    42.0
    """

	try:
		number = float(string)
	except:
		number = 0.0

	return number


# ------------------------------------------------------------------------------


def to_string(number):
	""" Convert float/int to string

    >>> to_string(13)
    '13'
    """

	return str(int(number))


# ------------------------------------------------------------------------------
