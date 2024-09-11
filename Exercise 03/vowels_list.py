def Vowels_String(input_string):
    vowels = "aeiouAEIOU"

    vowel_list = []
    
    for char in input_string:
        if char in vowels:
            vowel_list.append(char)
    return vowel_list

input_string = input("Enter a string: ")
vowel_list = Vowels_String(input_string)
print(vowel_list)

