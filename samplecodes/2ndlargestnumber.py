list = [1, 30, 49, 21, 4]
print (list) 
maxvalue = max(list)
print (maxvalue)
MaxValueIndex = list.index(maxvalue)
print (MaxValueIndex)

RemovedElement = list.pop(MaxValueIndex)
print (RemovedElement)

print (list)
SecondMaxElement = max(list)
print (SecondMaxElement )


