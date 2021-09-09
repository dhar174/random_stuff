import numpy.random as random


def get_temp():
    newTemp = random.randint(250, 300)
    return int(newTemp)

def lower_function(degrees):
##    newTemp = random.randrange(250, degrees)
    newTemp = random.randint(250, (degrees+250))
    return newTemp

def raise_function(degrees):
##    newTemp = random.randrange(degrees, 300)
    newTemp = random.randint(degrees, 300)
    return int(newTemp)

