OPENERS = ('(', '[')
CLOSERS = (')', ']')
OPPOSITES = dict(zip(OPENERS, CLOSERS))

def is_balanced(string):
    opened = []
    for c in string:
        if c in OPENERS: # we're in a new expression
            opened.append(c)
        elif c in CLOSERS:
            if len(opened) == 0:
                return False # no corresponding openers at all!
            last_opener = opened.pop()
            if c != OPPOSITES[last_opener]: 
                return False # last opener doesn't match this closer
    return len(opened) == 0 # any unclosed openers?

print(is_balanced("A string without brackets is balanced"))
print(is_balanced('(parenthesized)'))
print(is_balanced('[bracketed]'))
print(is_balanced('[parentheses (within) brackets]'))
print(is_balanced('only parens: (a + (b + c))'))
print(is_balanced('outer brackets: [a + (b + c)]'))
print(is_balanced('inner brackets: (a + [b + c])'))
print(is_balanced('(-b \pm sqrt(b**2 - 4*a*c))/(2*a)'))

print()

print(is_balanced('(unclosed'))
print(is_balanced('unopened)'))
print(is_balanced('(a + (b + c) missing last parens'))
print(is_balanced('(a + (b + c))))))) too many closers!'))
print(is_balanced('(close a parenthesis with a bracket]'))
print(is_balanced('[close a bracket with a parenthesis)'))
        
            
