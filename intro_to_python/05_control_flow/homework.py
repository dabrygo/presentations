# Problem 1
import random
choices = ('rock', 'paper', 'scissors')
bot = random.choice(choices)
player = random.choice(choices) #'rock'

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
