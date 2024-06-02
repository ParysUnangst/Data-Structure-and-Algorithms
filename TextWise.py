def reverse_string(s):
    # Base case: If the string is empty or has one character, return it as is
    if len(s) <= 1:
        return s
    # Recursive case: reverse the rest of the string and append the first character to the end
    return reverse_string(s[1:]) + s[0]

# Example usage:
input_string = "TextWise Solutions"
reversed_string = reverse_string(input_string)
print(f"Original String: {input_string}")
print(f"Reversed String: {reversed_string}")

    
