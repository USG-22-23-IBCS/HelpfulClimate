import random

class House:

    def __init__(self):
        self.rating = random.randint(1,10)

    def getRating(self):
        return self.rating

def greedyPath(m, num):
    bestHouses = []
    houses = []
    coords = []

    for i in range(5):
        for j in range(5):
            houses.append(m[i][j])
            coords.append([i,j])

    for i in range(25):
        maxHouse = houses[0]
        for h in houses:
            if h > maxHouse:
                maxHouse = h
        pos = houses.index(maxHouse)
        bestHouses.append(coords.pop(pos))
        houses.pop(pos)
    
    for i in range(25):
        p = []

        start = bestHouses[i]
        x = start[0]
        y = start[1]
        pVal = m[x][y]
        p.append(start)
           
            #keeping track of value of path
            #picking next best house to start with

        for i in range(num - 1):
            neighbors = [[x, y-1], [x, y+1], [x-1, y], [x+1, y]]
            bad = []

            for n in neighbors:
                if (n[0] > 4) or (n[0] < 0):
                    bad.append(n)
                elif (n[1] > 4) or (n[1]<0):
                    bad.append(n)
                elif n in p:
                    bad.append(n)
            for b in bad:
                neighbors.remove(b)
                'slay here'
            if len(neighbors) == 0:
                break
            bestN = neighbors[0]
            broken = False
            for b in  bestHouses:
                if broken:
                    break
                for n in neighbors:
                    if n == b:
                        bestN = n
                        broken = True
                        break

            p.append(bestN)
            x = bestN[0]
            y = bestN[1]

            pVal = pVal + m[x][y]

            if len(p) == num:
                return pVal, p
        return 0, [[0,0]]


def main():
    m = [[], [], [], [], []]
    for l in m:
        for i in range(5):
            h = House()
            l.append(h.getRating())

    for i in range(5):
        print(m[0][i], m[1][i], m[2][i], m[3][i], m[4][i]) 

    num = int(input("How many houses to visit?\n"))
    pVal, p = greedyPath(m, num)

    print(p)

    '''Random Path Call'''
    #total = 0
    #for i in range(5):
       # for j in range(5):
           # total = total + m[i][j]
    #average = total/25
    
    #pVal, p = randPath(m, num)
    #while (average > pVal/num):
        #pVal, p = randPath(m, num)
    
    #print(p, pVal)
    #print("Random path average value: " + str(pVal/num))
    #print("Neighborhood is: " +str(average))

    '''Greedy Path Call'''
    
                       

    #calculate the average rating of a house in the neighborhood

    
    #while the average of value of the house is greater than the
    #average of the path randomly chosen, try getting another random
    #path. stop, once it is better, and print it.

            

        

if __name__ == "__main__":
    main()
'''
--------------------
Greedy Path writeup
--------------------
1. Create list of highest-ranking houses in sorted order
#for loop as opposed to while loop
2. Keep track of pVal
#same as random path
3. Pick next house from bestHouse list
#different
4. Check to see bad neighbors and if we're stuck
#same as random path
5. Pick best neighbor from all tht good ones (items in neighbor list)
#different
6. Add neighbor to path and update x, y, pVal
#same as random path
7. if len(p) == num:
    return pVal, p

'''
