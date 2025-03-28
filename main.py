#Julian.Bourgeois
#march 24th 2025
import random
numbers = []
for i in range (100):
    num = random.randint (0,100)
    numbers.append(num)

avg = sum(numbers) /len (numbers)
print(numbers)
print(avg)

...