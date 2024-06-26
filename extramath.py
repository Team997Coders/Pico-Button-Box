def Map(x, in_min, in_max, out_min, out_max): #map one range to another
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def clamp(num, lower, upper): #limit number to range
    if num < lower:
        num = lower
    elif num > upper:
        num = upper
    return num