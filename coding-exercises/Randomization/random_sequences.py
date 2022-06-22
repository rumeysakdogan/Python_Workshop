import random
# 1. random.shuffle(x)
# This is used to shuffle the sequence in place. A sequence can be any list/tuple containing elements.
 
sequence = [random.randint(0, i) for i in range(10)]
 
print('Before shuffling', sequence)
 
random.shuffle(sequence)
 
print('After shuffling', sequence)

# 2. random.choice(seq)
# This is a widely used function in practice, wherein you would want to randomly pick up an item from a List/sequence.
 
a = ['one', 'eleven', 'twelve', 'five', 'six', 'ten']
 
print(a)
 
for i in range(5):
    print(random.choice(a))

# 3. random.sample(population, k)
# Returns a random sample from a sequence of length k.

a = ['one', 'eleven', 'twelve', 'five', 'six', 'ten']
 
print(a)
 
for i in range(3):
    b = random.sample(a, 2)
    print('random sample:', b)

# Random Seed
# Since pseudorandom generation is based on the previous number, we usually use the system time to make sure that the program gives a new output every time we run it. We thus make use of seeds.

# Python provides us with random.seed() with which we can set a seed to get an initial value. This seed value determines the output of a random number generator, so if it remains the same, the output also remains the same.

random.seed(1)
 
print('Generating a random sequence of 4 numbers...')
print([random.randint(1, 100) for i in range(5)])
 
# Reset the seed to 1 again
random.seed(1)
 
# We now get the same sequence
print([random.randint(1, 100) for i in range(5)])