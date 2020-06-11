# returns every other char of a given string starting with first
def string_alternative(s_edit):
    print(s_edit[::2]) # using string slicing to print alternate characters in a string


if __name__ == '__main__':      # calling main function
    s_input = input("Enter the string to edit :")
    string_alternative(s_input)    # calling the function inside main
