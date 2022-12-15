def main():
    L = [34, 20, 46, 67, 37, 27, 87, 983, 567, 32]

    print(L)
    print("bubbling being below")
    steps = 0
    for i in range(len(L)-1):
        for j in range(len(L)-1):

            if L[j] > L[j+1]:
            #swap
                temp = L[j]
                L[j] = L[j+1]
                L[j+1] = temp
            steps = steps + 1

        print("done!")
        print(L)
        
        print(len(L))
        print(steps)


        #Selection
        print("commence selecting")
        L = [4, 8, 2, 6, 10, 15]
        for i in range(len(L)-1):
            curMin = L[i]
            curInd = i
            for j in range(i, len(L)):
                if L[j] < curMin:
                    curMin = L[j]
                    curInd = j
            #Swap value to correct position
            temp = curMin
            L[j] = L[j+1]
            L[curInd] = L[i]
            L[i] = temp

            

              

if __name__ == "__main__":
    main()
