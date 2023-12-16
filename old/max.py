x1 = int(input("ведите 1 число:")) 
x2 = int(input("ведите 2 число:")) 
x3 = int(input("ведите 3 число:")) 
if x1 > x2:
    
    if x1 > x3:
        print(f"макс число {x1}")
    else:
        print(f"макс число {x3}")
else: 
    if x2 > x3:
        print(f"макс число {x2}")
    else:
        print(f"макс число {x3}")