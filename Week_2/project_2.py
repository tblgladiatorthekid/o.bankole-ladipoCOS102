import math
print("FORMULA CALCULATOR")

choice = input ("Please select what type of formula you are using: A. Quadratic, B. Cubic, C. Quartic")

if choice == "A":
    a = int(input("Enter your value with the hightest power: "))
    b = int(input("Enter your next value here: "))
    c = int(input("Enter your last value here: "))

    d = b - 4*a*c

    if d >= 0:
        root1 = (-b + math.sqrt(d))/(2*a)
        root2 = (-b - math.sqrt(d))/(2*a)

        root1 = complex(real_numbers,imaginary_numbers)
        root2 = complex(real_numbers,imaginary_numbers)

    print(f"You chose a quadratic equation {a}, {b} and {c}. The roots are {root1} and {root2}.")

elif choice == "B":
    a = int(input("Enter your value with the hightest power: "))
    b = int(input("Enter your next value here: "))
    c = int(input("Enter your next value here: "))
    d = int(input("Enter your last value here: "))

    p = (3*a*c - b**2)/(3 * a**2)
    q = (2*b**3-9*a*b*c+27*a**2*d)/(27*a**3)

    if -q >= 0:
        m

    
        
    
