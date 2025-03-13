print(" FINANCIAL (INTEREST) CALCULATOR")

print ("Good day customer, please enter the following for this program to work.\n")
principal = int(input("Input your principal here.\n"))

rate = int(input("Input the rate on your principal here.\n"))

time = int(input("Input the time on your principal here.\n"))

choice = input("Next, please select which operation you would like to use: \nA. Simple Interest \nB. Compound Interest \nC. Annuity\n").upper()

if choice == "A":
    amount = principal * (1 + (rate/100)*time)
    simple_interest = amount - principal
    print("Your simple interest is: NGN",simple_interest)

elif choice == "B":
    amount = principal * ((1 + rate/100)**time)
    compound_interest = amount - principal
    print("Your compound interest is: NGN", compound_interest)

elif choice == "C":
    amount = principal * ((1 + rate/100) ** time) - 1/(rate/100)
    annuity = amount - principal
    print("Your annuity is: NGN", annuity)

