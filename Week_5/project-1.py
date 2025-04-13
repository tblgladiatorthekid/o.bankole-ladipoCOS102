
def calculate_area (r):
    pi = 3.14
    area = pi * r ** 2
    print(f"Area of your circle is {area} m^2.")
    return area

calculate_area(r = int(input("What is your radius?")))