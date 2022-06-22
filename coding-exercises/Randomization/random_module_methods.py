# 1. seed()
# This initializes a random number generator. To generate a new random sequence, a seed must be set depending on the current system time. random.seed() sets the seed for random number generation.

# 2. getstate()
# This returns an object containing the current state of the generator. To restore the state, pass the object to setstate().

# 3. setstate(state_obj)
# This restores the state of the generator at the point when getstate() was called, by passing the state object.

# 4. getrandbits(k)
# This returns a Python integer with k random bits. This is useful for methods like randrange() to handle arbitrary large ranges for random number generation.

import random

random.getrandbits(100)

random.seed(1)

# Get the state of the generator
state = random.getstate()
 
print('Generating a random sequence of 3 integers...')
for i in range(3):
    print(random.randint(1, 1000))
 
# Restore the state to a point before the sequence was generated
random.setstate(state)
print('Generating the same identical sequence of 3 integers...')
for i in range(3):
    print(random.randint(1, 1000))