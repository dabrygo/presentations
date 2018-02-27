import string

def caesar_cipher(message, a_is='N'):
  upper = string.ascii_uppercase
  upper_a_is = a_is.upper()
  shift = upper.index(upper_a_is)
  upper_key = upper[shift:] + upper[:shift]
  key = upper_key.lower() + upper_key
  table = str.maketrans(string.ascii_letters, key)
  return message.translate(table)
