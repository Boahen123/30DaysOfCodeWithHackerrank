T = int(input("Enter the test cases: "))
# Number of test cases
stringList = []
for i in range(T):
    inputStr = input(f"Enter string[{i}]: ")
    stringList.append(inputStr)
    
print(stringList)

for index in range(len(stringList)):
    word = stringList[index]
    for k in range(0,len(word),2):
        print(word[k], end='')
    print(" ", end='')
    for j in range(1,len(word),2):
        print(word[j], end='')
        
    print()

    
    

    
