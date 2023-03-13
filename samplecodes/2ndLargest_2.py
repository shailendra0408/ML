numberlist = [10000000, 30, 49, 21, 4, -1, 49]
print (numberlist)
NewNumberList = []

for i in range (0, len(numberlist)):
    for j in range (i+1,len(numberlist)):
        if (numberlist[i]< numberlist[j]):
            temp = numberlist[i];
            numberlist[i] = numberlist[j];
            numberlist[j] = temp;

print (numberlist)
print (numberlist[1])



            
    