from random import randint, choice
# Create a random string of 10 numbers betwen 1 and 100 and 5 letters:
numbers = []
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
lottery_letters = []
winning_results = [] 

for letter in range(5):
    result = choice(letters)
    lottery_letters.append(result)

for number in range(10):
    result = randint(1, 10)
    numbers.append(result)

lottery = lottery_letters + numbers


for number in range(4):
    your_ticket = choice(lottery)
    if your_ticket == type(int):
        winning_results.append(str(your_ticket))
    else:
        winning_results.append(your_ticket)
        
print(lottery)
print(f"If your ticket matches {tuple(winning_results)} you've won!")




