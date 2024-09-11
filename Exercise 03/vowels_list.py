def vowels_string(input_string):
    vowels = "aeiouAEIOU"

    vowel_list = []
    
    for char in input_string:
        if char in vowels:
            vowel_list.append(char)
    return vowel_list

input_string = input("Enter a string: ")
vowel_list = vowels_string(input_string)
print(vowel_list)

