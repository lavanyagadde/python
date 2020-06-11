# returns every other char of a given string starting with first
def string_alternative(s_edit):
    print(s_edit[::2])


if __name__ == '__main__':
    s_input = input("Enter the string to edit :")
    string_alternative(s_input)