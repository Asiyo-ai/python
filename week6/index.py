# import math
# print(math.sqrt(16))  # Output: 4.0
# print(math.pi)  # Output: 3.141592653589793

# import math

# print ("Power of 2 v 3 is", math.pow(2, 9.13))  # Output: 8.0

import random
print ("Random number between 1 and 10 is", random.randint(1,10))

# Output: Random number between 1 and 10
print ("random jasmine", random.choice(["jasmine", "rose", "lilly"]))

import requests
response = requests.get('https://api.github.com')

print(response)  # Output: 200 (if the request was successful)

import numpy as np
my_array = np.array([1, 2, 3, 4, 5])
print(my_array)  # Output: [1 2 3 4 5]
print("array *2", my_array * 2)  # Output: [ 2  4  6  8 10]
print("mean", np.mean(my_array))  # Output: 3.0



