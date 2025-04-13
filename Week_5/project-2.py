def is_palindrome (x):
    print(x)
    #Reversed the string
    e = x[::-1]
    print(e)
    # Remove non-alphanumeric characters and convert to lowercase
    string = ''.join(e.lower() for e in x if e.isalnum())
    if string == string[::-1]:
        print("It is a palindrome.")
    else:
        print("It is not a palindrome")
    return string == string[::-1]

result = is_palindrome(input("Please input your word"))
print(result)