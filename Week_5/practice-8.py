total = 50
def sum (arg1, arg2):
    total = arg1 + arg2
    print(f"Inside the local function: {total}")
    return total
sum(10, 20)
print(f"Outside the function global: {total}")