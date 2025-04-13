def swap_first_last (lst):
    if len(lst) > 1:
        lst[0],lst[-1] = lst[-1],lst[0]
    return lst
list = []
n = int(input("Enter your number of values"))

for i in range(n):
    e = int(input("Enter your values here"))
    list.append(e)
print(list)
if len(list) > 1:
    swap = swap_first_last(list)
    print(f"After swap;{swap}")
