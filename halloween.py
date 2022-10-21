import random

class House:

    def __init__(self):
        self.rating = random.randint(1,10)

    def getRating(self):
        return self.rating

##def calculatePath(num):
    #path = []


def main():

    m = [[], [], [], [], []]
    for l in m:
        for i in range(5):
            h = House()
            l.append(h.getRating())
            
#prints ratings in terms of indivisal ratings per print
    #for l in m:
        #for house in l:
            #print(house)
            
    for i in range(5):    
        print(m[0][i], m[1][i], m[2][i], m[3][i], m[4][i])

    num = int(input("how many houses"))

    for i in range()

    
    right = m[x+1][y]
    left = m[x-1][y]
    below = m[x][y+1]
    above = m[x][y-1]
    
    
    for i in range():
        if x > 4:
            break
        if x < 0:
            break
        if y > 4:
            break
        if y < 0:
            break

next = random.choice(neigh)    


    #calculatePath(num)
    
'neighbor variables'



if __name__ == "__main__":
    main()
