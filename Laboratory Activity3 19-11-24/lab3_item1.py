def roman_to_integer(roman):
    
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    
    roman = roman.upper()
    
    sum = 0 
    beforevalue = 0  

    for char in reversed(roman):
        if char not in roman_values:
            return "Invalid Roman numeral." 
        
        newvalue = roman_values[char]
        
    
        if newvalue < beforevalue:
            sum -= newvalue
        else:
            sum += newvalue
        
        beforevalue = newvalue 

    return sum

if __name__ == "__main__":
    roman_numeral = input("Enter a Roman numeral: ")
    normalized_roman = roman_numeral.upper()  
    result = roman_to_integer(roman_numeral)
    if isinstance(result, int):
        print(f"The integer value of '{normalized_roman}' is: {result}")
    else:
        print(result)
