quarters = int(input(""))
g1 = int(input(""))
g2 = int(input(""))
g3 = int(input(""))
timesPlayed = 0


def check(amount):
    global g1
    global g2
    global g3
    if g1 >= 35:
        amount += 30
        g1 = 0
    if g2 >= 100:
        amount += 60
        g2 = 0
    if g3 >= 10:
        amount += 9
        g3 = 0
    return amount


while quarters > 0:
    g1 += 1
    quarters -= 1
    timesPlayed += 1
    quarters = check(quarters)
    if quarters == 0:
        break
    g2 += 1
    quarters -= 1
    timesPlayed += 1
    quarters = check(quarters)
    if quarters == 0:
        break
    g3 += 1
    quarters -= 1
    timesPlayed += 1
    quarters = check(quarters)
    if quarters == 0:
        break

if timesPlayed == 1:
    print(f"Martha plays {timesPlayed} time before going broke.")
else:
    print(f"Martha plays {timesPlayed} times before going broke.")

