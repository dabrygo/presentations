# Problem 1
import random
choices = ('rock', 'paper', 'scissors')
bot = random.choice(choices)
player = 'rock' #random.choice(choices) #input().lower(); assert player in choices

print(f"player chose {player} and bot chose {bot}")
if player == bot:
    print("tie")
elif player == 'rock' and bot == 'paper':
    print("bot wins")
elif player == 'scissors' and bot == 'rock':
    print("bot wins")
elif player == 'paper' and bot == 'scissors':
    print("bot wins")
else:
    print("you win!")


# Problem 2
def fibonacci(n):
    fibonacci = [1, 1]
    for i in range(3, n+1):
        b = fibonacci.pop()
        a = fibonacci.pop()
        c = a + b
        fibonacci = [b, c]
    return fibonacci.pop()

start = [fibonacci(i) for i in range(1,11)]
print(*start, sep=', ', end='...\n')

# Problem 3
##max_guesses = 10
##low = 1
##high = 100
##number = random.randint(low, high)
##for i in range(1, max_guesses+1):
##    guess = int(input(f"Guess a number between {low} and {high}: "))
##    if guess > number:
##        print("Too high")
##    elif guess < number:
##        print("Too low")
##    else:
##        print(f"You guessed my number {number} in {i} tries!")
##        break
##else:
##    print(f'None of those. My number was {number}.')



# Problem 4
inventory = {'bread': 5, 'sword': 1, 'gold': 42}

def take(quantity, item):
    if not any(inventory.values()):
        raise Exception("I'm not carrying anything")
    amount = inventory[item]
    if quantity > amount:
        raise ValueError(f"Can't take {quantity} {item}; I only have {amount}")
    inventory[item] = amount - quantity

try:
    take(1, 'kangaroo')
except KeyError:
    pass
take(5, 'bread')
try:
    take(2, 'sword')
except ValueError:
    pass
take(1, 'sword')
take(41, 'gold')
try:
    take(2, 'gold')
except Exception:
    pass
take(1, 'gold')
try:
    take(1, 'gold')
except:
    pass
print(inventory)
