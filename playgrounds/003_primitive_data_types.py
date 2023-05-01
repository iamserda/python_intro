print("PROGRAM 2")
print("(START)")

# formatting strings using fstrings
client = "Toussaint Louverture"
username = "ht_leader_one"
loc = "Port-au-Prince, Haiti"
time = "Jan 1, 1804 at 10:10 AM"
browser = "Google Chrome"
message =f"""Hello {client}({username}),

Your account was accessed in {loc} at {time} using {browser}.

Please reach out to Help and Support if that was not you.

Best,
Team HealthFit
"""

print("\nEXAMPLE 2: Using f'str' to create and format new strings:")
print("message:", message)  # notice formats remain as written.
# string manipulations, string  methods
print("message-length", len(message))
print("message[:10]", message[:10])
print("message[10:20]", message[10:20])
print()
new_message = "Python is a programming language like no other!!"
first_half_message = new_message[:int((len(new_message)/2))]
last_half_message = new_message[(int(len(new_message)/2)):]
print("new message:", new_message,"length:", len(new_message))
print("first-half:", first_half_message, "length:", len(first_half_message))
print("scnd-half:", last_half_message, "length:", len(last_half_message))

course = "python programming 101"
print("<class 'str'>.capitalize():",course.capitalize())
print(course)


# # string.methods()
##
a_string = " The latest version of Python is version 3.   "
#  capitalize() - Converts the first character to upper case
print(".capitalize():", a_string.capitalize())
#  casefold() - Converts string into lower case
print(".casefold():", a_string.casefold())
#  center() - Returns a centered string
#  count() -  Returns the number of times a specified value occurs in a string
print("'s' count:", a_string.count("s"))
#  encode() - Returns an encoded version of the string
#  endswith() - Returns true if the string ends with the specified value
#  expandtabs() - Sets the tab size of the string
#  find() - Searches the string for a specified value and returns the position of where it was found
#  format() - Formats specified values in a string
#  format_map() - Formats specified values in a string
#  index() -  Searches the string for a specified value and returns the position of where it was found
#  isalnum() -  Returns True if all characters in the string are alphanumeric
#  isalpha() -  Returns True if all characters in the string are in the alphabet
#  isdecimal() -  Returns True if all characters in the string are decimals
#  isdigit() -  Returns True if all characters in the string are digits
#  isidentifier() - Returns True if the string is an identifier
#  islower() -  Returns True if all characters in the string are lower case
#  isnumeric() -  Returns True if all characters in the string are numeric
#  isprintable() -  Returns True if all characters in the string are printable
#  isspace() -  Returns True if all characters in the string are whitespaces
#  istitle() -  Returns True if the string follows the rules of a title
#  isupper() -  Returns True if all characters in the string are upper case
#  join() - Joins the elements of an iterable to the end of the string
#  ljust() -  Returns a left justified version of the string
#  lower() -  Converts a string into lower case
#  lstrip() - Returns a left trim version of the string
#  maketrans() -  Returns a translation table to be used in translations
#  partition() -  Returns a tuple where the string is parted into three parts
#  replace() -  Returns a string where a specified value is replaced with a specified value
#  rfind() -  Searches the string for a specified value and returns the last position of where it was found
#  rindex() - Searches the string for a specified value and returns the last position of where it was found
#  rjust() -  Returns a right justified version of the string
#  rpartition() - Returns a tuple where the string is parted into three parts
#  rsplit() - Splits the string at the specified separator, and returns a list
#  rstrip() - Returns a right trim version of the string
#  split() -  Splits the string at the specified separator, and returns a list
#  splitlines() - Splits the string at line breaks and returns a list
#  startswith() - Returns true if the string starts with the specified value
#  strip() -  Returns a trimmed version of the string
#  swapcase() - Swaps cases, lower case becomes upper case and vice versa
#  title() -  Converts the first character of each word to upper case
#  translate() -  Returns a translated string
#  upper() -  Converts a string into upper case
#  zfill() -  Fills the string with a specified number of 0 values at the beginning

# https://www.w3schools.com/python/python_ref_string.asp


"""
    Mutli-line comments:
    Here we cover: variables, primitive data types, collections, iterations, conditions, comparisons, functions, classes

    Example of a multi-line comment.
    We use 3 quotes to start a multi line string or comment.
    This is an example of a multi-line comments.
    Since this string is not saved or used within the program,
    Python Interpreter reads it as a comment, a multi-line comment to be exact.
    Python does not TRUELY support multi-line comments. This is more like a workaround.
    These are also called Docstring(Documentation Strings).
"""
# Multi-line comments using """... """ are also known as docstrings.
""" Docstrings are used to document source code.
    We used doctrings to leave notes or insights to self and other people who may maintain the code in the future.
"""