print("STAFF CHECKER\n")

total_staff = 2500

#SEQUENCE LIMITED TO TOTAL NUMBER OF STAFF
while total_staff > 0:
    name = input("Good day; please enter your name here:\n")
    experience = int(input("Please enter your total years of experience:\n"))
    age = int(input("Next, please enter your age: \n"))

    if experience > 25 and age >= 55:
        print(f"{name},you will receive an Annual Tax Revenue of NGN 5,600,000.")

    elif experience > 20 and age >= 45:
        print(f"{name},you will receive an Annual Tax Revenue of NGN 4,480,000.")

    elif experience > 10 and age >= 35:
        print(f"{name},you will receive an Annual Tax Revenue of NGN 1,500,000.")

    else:
        print(f"{name}, you are to receive an Annual Tax Revenue of NGN 550,000.")
#EXIT LOOP ONCE ALL STAFF HAS BEEN PROCESSED
    total_staff -= 1
    print(f"Staff left to check: {total_staff}\n")

    if total_staff == 0:
        print("All staff has been processed.")
        break




