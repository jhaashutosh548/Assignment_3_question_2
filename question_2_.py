def reverse_string(input_string):
    reversed_string = ''
    for char in input_string:
        reversed_string = char + reversed_string
    return reversed_string

# Sample string
input_string = "1234abcd"

# Call the function to reverse the string
reversed_string = reverse_string(input_string)

# Print the reversed string
print("Reversed String:", reversed_string)