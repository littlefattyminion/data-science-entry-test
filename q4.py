def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    if not isinstance(s, str):
        raise ValueError("Input must be a string.")
    
    return s[::-1]


result1 = string_reverse("Hello World")
print (result1)

result2 =  string_reverse("Python")
print(result2)