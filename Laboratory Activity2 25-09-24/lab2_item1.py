def palindrome(num):

    str_num = str(num)

    if str_num == str_num[::-1]:
        return "Palindrome"
    else:
        return "Not a Palindrome"
    
num = int(input("Enter an integer: "))

result = palindrome(num)
print(result)