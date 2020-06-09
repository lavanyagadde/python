# Reversing the string
s_string = list(input("Enter the string: "))
if len(s_string) > 2:
    s = s_string[2:]
    s_reverse = s[::-1]
    print(''.join(s_reverse))
else:
    print("Please Enter string with more than 2 characters: ")