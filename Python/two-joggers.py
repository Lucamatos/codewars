import math

def nbr_of_laps(x, y):
    mdc = math.gcd(x,y)

    mmc = (x*y)//mdc

    return (mmc//x, mmc//y)

#ou

def nbr_of_laps(x, y):
    if x > y:
        maior = x
    else:
        maior = y
    while True:
        if maior % x == 0 and maior % y == 0:
            z = maior
            break
        else:
            maior += 1
    return (z // x, z // y)
