
class Octopus:
    #constructor method has all of the instance variables (values/data)
    def __init__(self, order, x, col, phenotypicTrait):
        self.order = order
        self.numTentacles = 8
        self.color = col
        self.adaptation = phenotypicTrait


    def getOrder(self):
        return self.order

    def setColor(self, c):
        self.color = c
        #why no return in set?
    def getColor(self):
        return self.color

    def setAdapt(self, a):
        self.adapatation = a
        #why some have another variable/dimension and others just 'self'?
    def getAdapt(self):
        return self.adaptation

    def setTent(self, x):
        self.numTentacles = x
    def getTent(self):
        return self.numTentacles

def main():

    haliphronAt = Octopus("Octopada", 7, "white", "hidden eighth limb")
    northPacificGiant = Octopus("Octopada", 8, "auburn", "size")

    haliphronAt.setColor("White")
    northPacificGiant.setColor("Auburn")
    print(haliphronAt.getColor())
    print(northPacificGiant.getColor())

    print(haliphronAt.getOrder())
    print(northPacificGiant.getOrder())

    haliphronAt.setTent(7)
    print(haliphronAt.getTent())
    print(northPacificGiant.getTent())

    

if __name__ == "__main__":
    main()
