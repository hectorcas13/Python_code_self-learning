#this is a summation code
# it takes a range of two values to do a summation for example:
# [1,3] = 1+2+3 = 6

l = [3,8]
ini = l[0] 
fin = l[1]
ini2 = 0
cal2 = 0
if ini != 1:
    ini2= ini-1
    for i in range(len(l)):cal2 = (ini2 + 1) * ini2 / 2  
    for i in range(ini,fin): cal1 = (fin + 1) * fin / 2 
    print(int(cal1-cal2))
else:
    for i in range(ini,fin): cal1 = (fin + 1) * fin / 2
    print(int(cal1))
