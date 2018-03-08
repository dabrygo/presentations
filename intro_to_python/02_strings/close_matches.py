from difflib import get_close_matches as close

with open('commonly_confused.txt') as f:
    text = f.read()
    dictionary = text.split()

print(close('breoch', dictionary, n=10))
