time = 100
count = 0
while count < time:
    print(time)
    time -= 1

    if time == count:
        print("Tick...tick...Boom!")
    else:
        print("...second(s) until impact")

