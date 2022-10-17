

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
def centeredAvg(l):
    maxNum = l[0]
    minNum = l[0]
    for elem in l:
        if elem > maxNum:
            maxNum = elem
        if elem < minNum:
            minNum = elem
    l.remove(maxNum)
    l.remove(minNum)

    total = 0
    for elem in l:
        total = total + elem

    return total / len(l)

def main():

    print(bigDiff([2, 4, 9, 3, 1]))

    centeredAveList = [1, 2, 3, 4, 5, 6]
    print(centeredAvg(centeredAveList))
    
    
if __name__ == "__main__":
    main()
