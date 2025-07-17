def swap(x, y):


    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
    return -1
        
    x = x + y
    y = x - y
    x = x - y
    
    return x, y
  
 
result1 = swap("Apple", 10)
print(result1)


result2 = swap(9, 17)
print(result2)