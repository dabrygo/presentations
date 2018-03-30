import math

# table of squares
print("{:^3} | {:^5}".format('n', 'n**2'))
print("-" * 10)
for i in range(10):
    print("{:^3} | {:^5}".format(i, i**2))
    
# encryption
plaintext = 'defend the east wall of the castle'
no_spaces = plaintext.replace(' ', '')
first = no_spaces[::4]
second = no_spaces[1::2]
third = no_spaces[2::4]
answer = first + second + third
print(answer)

# decryption
encrypted = "dnetlhseedheswloteateftaafcl"
##encrypted = "IA_EZS_ELYLK_UZERLIPL"
height = 3
cycle = height * 2 - 2
length = len(encrypted)
base_width = math.floor(length / cycle)
extra = length % base_width
first_end = base_width+extra
first = '...'.join(list(encrypted[:first_end]))
second_end = first_end+2*base_width
second = '.' + '.'.join(list(encrypted[first_end:second_end])) + '.'
third = '..' + '...'.join(list(encrypted[second_end:])) + '..'
print(first)
print(second)
print(third)

# ord/chr
message = "A Møøse once bit my sister... No realli!"
print(' '.join([str(ord(c)) for c in message]))
print(''.join([chr(int(c)) for c in '''65 32 77 248 248 115 101 32 111 110 99 101 32 98 105 116 32 109 121 32 115 105 115 116 101 114 46 46 46 32 78 111 32 114 101 97 108 108 105 33'''.split()]))

# law of cosines
import math
def law_of_cosines(a, b, gamma):
    return math.sqrt(a**2 + b**2 - 2*a*b*math.cos(gamma))
print(law_of_cosines(3, 4, math.pi/2), math.hypot(3, 4))
print(law_of_cosines(3, 4, 0))
print(law_of_cosines(3, 4, 0.1))
print(law_of_cosines(3, 4, math.pi / 4))
print(law_of_cosines(3, 4, 3 * math.pi / 2))
