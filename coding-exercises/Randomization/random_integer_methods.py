# 1. randrange(start, stop, step)
# Returns a randomly selected integer from range(start, stop, step). This raises a ValueError if start > stop.

# 2. randint(a, b)
# Returns a random integer between a and b (both inclusive). This also raises a ValueError if a > b.

# Here is an example that illustrates both the above functions.

import random
 
i = 100
j = 20e7
 
# Generates a random number between i and j
a = random.randrange(i, j)
try:
    b = random.randrange(j, i)
except ValueError:
    print('ValueError on randrange() since start > stop')
 
c = random.randint(100, 200)
try:
    d = random.randint(200, 100)
except ValueError:
    print('ValueError on randint() since 200 > 100')
 
print('i =', i, ' and j =', j)
print('randrange() generated number:', a)
print('randint() generated number:', c)
