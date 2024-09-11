input_str = input("Enter two space-separated charactes: ")
char1, char2 = input_str.split()

print("------------------------------------------") 
greater_char=max(char1,char2)
print("The Character with grater value is: ",greater_char )
print("------------------------------------------") 

print("This part is optional to include.")
print("Showing ASCII Values: ")
if len(char1) ==1 and len(char2) == 1:
    ascii_value1 = ord(char1)
    ascii_value2 = ord(char2)
    print(f"{char1}: {ascii_value1}")
    print(f"{char2}: {ascii_value2}")
else:
    print("Please enter exaclty two single characters. ")