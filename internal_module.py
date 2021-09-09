import OutsideModule

temperature = OutsideModule.get_temp()
target = 275
steps = 0
pressure = 100
status = ""

powered = True

def lowerTemp(degrees):
    newTemp = OutsideModule.lower_function(degrees)
    return newTemp

def raiseTemp(degrees):
    newTemp = OutsideModule.raise_function(degrees)
    return newTemp

def check(temperature):
    if temperature > target:
        status = "Too High!"
        newTemp = lowerTemp(temperature - target)
        temperature = newTemp
    elif temperature < target:
        status = "Too Low!"
        newTemp = raiseTemp(temperature + (target - temperature))
        temperature = newTemp
    else:
        status = "OK"
    return status

while powered == True:
    for y in range(0, 9):
        steps += 1
    if steps == 9:
        temperature = OutsideModule.get_temp()
        status = check(temperature)
        steps = 0
        print(status)
    else:
        pass
    


