x1 = int(input("ведите 1 число:"))
x2 = int(input("ведите 2 число:"))

s = 0
if x1 > x2:
    i = x2
    while i <= x1:
        s = s+i
        i += 1                
else:
    i = x1
    while i <= x2:
        s = s+i
        i += 1 
print(f"сумма = {s}")