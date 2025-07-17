def find_and_replace(lst, find_val, replace_val):
    """
    - Searches for all occurrences of a value (find_val) in a given list (lst)
      and replaces them with another value (replace_val).
    - lst must be a list.
    - Returns the modified list.
    """
    if not isinstance(lst, list):
        raise ValueError("Input must be a list.")
    
    return [replace_val if item == find_val else item for item in lst]


original_list1 =  [1, 2, 3, 4, 2, 2]
Modified_list1 = find_and_replace(original_list1, 2, 5)
print (Modified_list1)

original_list2 =   ["apple", "banana", "apple"]
Modified_list2 = find_and_replace(original_list2, "apple", "orange")
print (Modified_list2) 
