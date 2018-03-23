# Problem 1
city, state, country = ('ABQ', 'NM', 'USA')

# Problem 2
x = [1, 2, 8]
x.remove(8)     # arg is value; no return
first = x.pop(0) # arg is index; return value

# Problem 3
x = [2, 1, 8]
y = sorted(x) # does not modify list
z = [2, 1, 8]
z.sort()      # modifies list

# Problem 4
firsts = ['William', 'Warren', 'John', 'Franklin', 'John']
middles = ['Henry', 'Gamaliel', 'Calvin', 'Delano', 'Fitzgerald']
lasts = ['Harrison', 'Harding', 'Coolidge', 'Roosevelt', 'Kennedy']

# with zip
for first, middle, last in zip(firsts, middles, lasts):
    m, *_ = middle
    print(f'{last}, {first} {m}.')

# without zip
size = len(firsts)
for i in range(size):
    first = firsts[i]
    m, *_ = middles[i]
    last = lasts[i]
    print(f'{last}, {first} {m}.')

# Problem 5
sassafras = set('sassafras')
succotash = set('succotash')

print(len(sassafras), len(succotash)) # a
print(sassafras & succotash, len(sassafras & succotash)) # b
print(sassafras ^ succotash, len(sassafras ^ succotash)) # c
print(sassafras - succotash, len(sassafras - succotash)) # d
print(succotash - sassafras, len(succotash - sassafras)) # e

# Problem 6
from collections import Counter
dna = 'GATTACA'
counter = Counter(dna)
g_count = counter['G']
c_count = counter['C']
gc_content = (g_count + c_count) / len(dna) * 100
print(f"GC Content of {dna} = {gc_content:.2f}%")
