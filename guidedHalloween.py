import random

class House:

    def __init__(self):
        self.rating = random.randint(1,10)

    def getRating(self):
        return self.rating

def greedyPath(m, num):
    bestHouses = []

    for i in range(len(bestHouses)):
        p = []

        #keeping track of value of path
        #picking next best house to start with

        start = bestHouses[i]
        x = start[0]
        y = start[1]
        
        for i in range(num - 1):

def randPath(m, num):
    #create an empty path
    p = []

    #try to add coordinates to the path
    #if the path were to get stuck or be 'unfinished' in anyway, try again
    #only finish once a fair path is generated
    while (len(p) < num):
        p = []

        x = random.randint(0, 4)
        y = random.randint(0, 4)
        pVal = m[x][y]
        p.append([x, y])
        #keep track of the value of the path
        #choose a random coordinate to start at

        #add neighbors to the path at a randomly chosen direction
        #keep track of whether we get stuck. If we get stuck, break

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

            nextHouse = random.choice(neighbors)
            p.append(nextHouse)
            x = nextHouse[0]
            y = nextHouse[1]
            pVal = pVal + m[x][y]
            
            #stuck = True
            #for n in neighbors:
                #if (n[0]<5) and (n[0]>-1):
                   #if (n[1]<5) and (n[1]>-1):
                       #if n not in p:
                           #stuck = False
            #if stuck:
                #break
            
            '''while True:
                #choose a random direction and attempt to add the neighbor
                neighbor = random.choice(neighbors)
                #do not add the neighbor to the path if it is outside of the 5x5
                #or if the neighbor is already in the path
                #break the while loop if it was a successful addition or if stuck
                if (neighbor [1]<5) and (neighbor[1]>-1):
                    if (neighbor[0]<5) and (neighbor[0]>-1):
                        if neighbor not in p:
                            p.append(neighbor)
                            x = neighbor[0]
                            y = neighbor[1]
                            pVal = pVal + m[x][y]
                            break'''

                
        return pVal, p

  
def main():
    m = [[], [], [], [], []]
    for l in m:
        for i in range(5):
            h = House()
            l.append(h.getRating())

    for i in range(5):
        print(m[0][i], m[1][i], m[2][i], m[3][i], m[4][i]) 

    num = int(input("How many houses?\n"))

    '''Random Path Call'''
    total = 0
    for i in range(5):
        for j in range(5):
            total = total + m[i][j]
    average = total/25
    
    pVal, p = randPath(m, num)
    while (average > pVal/num):
        pVal, p = randPath(m, num)
    
    print(p, pVal)
    print("Random path average value: " + str(pVal/num))
    print("Neighborhood is: " +str(average))
                       

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
