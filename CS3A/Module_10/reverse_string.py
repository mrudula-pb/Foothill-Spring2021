
def reverse_a_string(reverse_str):
    """ reverse a string recursively """
    if len(reverse_str) == 1:
        return reverse_str
    first_letter = reverse_str[-1]
    remainder_reversed = reverse_a_string(reverse_str[:-1])
    return first_letter + remainder_reversed

reverse_str = "python"
print(reverse_a_string(reverse_str))