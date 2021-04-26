from random import randint

class Die():
    """A model of a 6-sided die."""

    def __init__(self, sides=6):
        """Initialize the sides of the die."""
        self.sides = sides

    def roll_die(self):
        """Return a number between 1 and 6."""
        return randint(1, self.sides)



d12 = Die(sides=12)
results = []

for roll_num in range(10):
    result = d12.roll_die()
    results.append(result)
print("10 rolls of a twelve-sided die:")
print(results)


