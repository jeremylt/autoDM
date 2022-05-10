# coding=utf8
"""
	Auto DM

	Jeremy L Thompson

	These are utility functions for the Module class.
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
