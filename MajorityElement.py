def MajorityElement(a):
    count = 0
    element = a[0]
    for i in range(len(a)):
        if count == 0:
            element = a[i]

        if a[i] == element:
            count += 1

        else: 
            count -= 1
    count2 = 0
    for i in range(len(a)):
        if a[i] == element:
            count2 += 1
    
    if count2 > len(a)//2:
        return element
    return None

    
print(MajorityElement([2,2,1,1,1,2,2]))
       