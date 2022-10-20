

#method that takes list of integers an returns difference between largest and smallest value RANGE
#ex. [2, 9, 4, 1, 8] --> 8
def bigDiff(l):
    maxNum = l[0]
    minNum = l[0]
    for elem in l:
        if elem > maxNum:
            maxNum = elem
        if elem < minNum:
            minNum = elem
    return maxNum - minNum
#method returning mean of all number save max, min
#ex. [2, 9, 4, 1, 8] --> 14/3 = 4.67
'''def centeredAvg(l):
    maxNum = l[0]
    minNum = l[0]
    count = True
    sum = 0
    for elem in l:
        if elem in l == 6:
            count = False
        if elem in l == 7:
            count = True
    l.remove(maxNum)
    l.remove(minNum)

    total = 0
    for elem in l:
        total = total + elem

    return total / len(l)'''
#Lists & Loops Practice Problem
'Question 1'
def find7s(l):
    count = 0
    for elem in l:
        if elem == 7:
             count = count + 1
        if elem == 7:
             count = count + 1   
        if count > 4:
            return True
        #else:
            #print("Fasle")
        #Q: Why printing None?
'Question 1 IN CLASS'
def find7s2(l):
    for i in range(len(l) - 1): 'i serves as itterater- can track list item position'
        if l[i] == 7:
            if l[i+1] == 7:
                return True
    return False
'Quesiton 2'
def Primes(l):
    count = 0
    for elem in l:
        if elem / maxNum:
            maxNum = elem
        if elem < minNum:
            minNum = elem
    l.remove(maxNum)
    l.remove(minNum)

    total = 0
    for elem in l:
        total = total + elem

    return total / len(l)
'Quesiton 2 IN CLASS'
def Primes2(l):
    count = 0
    for elem in l:
        if (elem == 2) or (elem == 3) or (elem == 5) or (elem == 7) or (elem == 11):
            break
        else:
            total = total + elem
    return total
'Question 3' #Q: difference between = and ==?
def exclusion(l):
    count = True
    total = 0
    for elem in l:
        if elem == 2:
            count = False
        elif count == False and elem == 3:
            count = True
        elif count == True:
            total = total + elem
'Quesiton 3 IN CLASS'
def exclusion2(l):
    count = 0
    found2 = False #this problem requires a variable to check
    for elem in l:
        if elem == 2:
            found2 = True
        
        if found2 == False:
            total = total + elem
            
        if found2 = True:
            if elem == 3:
                found2 = False
    return total

def main():

    print(bigDiff([2, 4, 9, 3, 1]))

    #centeredAveList = [1, 2, 3, 4, 5, 6]
    #print(centeredAvg(centeredAveList))

print("---------------Beginning of 17 Oct homework soluntions----------------")
"Question 1 sol'n"
print(find7s([1, 7, 1, 2, 3, 7, 7]))
print(find7s([1, 7, 1, 2, 3, 2, 7]))
print(find7s([1, 7, 1, 2, 3, 2, 7]))
print(find7s2([1, 7, 1, 2, 3, 7, 7]))


"Question 3 sol'n"
print(exclusion([1, 5, 6, 2, 8, 1, 3]))


if __name__ == "__main__":
    main()
