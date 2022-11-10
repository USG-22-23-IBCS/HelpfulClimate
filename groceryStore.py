
class GroceryStore:

    def __init__(self):
        self.manager = "Zedd"
        self.stock = {"-Drinks-" : 0,
                      "Cherry soda" : 1.25,
                      "Cherry kombucha" : 3.25,
                      "-Chips-" : 0,
                      "Sriracha Hippeas" : 4.50,
                      "Flamin Dorritos" : 2.50,
                      "-Salads-" : 0,
                      "Seaweed salad" : 4.75,
                      "Southwest salad" : 6.75,
                      "-Yogurt-" : 0,
                      "Greek yogurt" : 3.50,
                      "Sweet parfait" : 1.50,
                      "-Potato-" : 0,
                      "Baked potato" : 5.50,
                      "French fries" : 3.50}

def main():

    store = GroceryStore()
    #done = False
    #for i in range(4):
    cost = 0
    print("Hello! Welcome to your local Z!Mart grocery store!")
    print("Would you like a list of our current items or would you prefer to browse?")
    print("1 List or 2 Browse")
    user = input("")
    storeList = list(store.stock.keys())
    while True:
        if user == "1":
            for item in storeList:
                print(item)
            print("To browse aisles at any point, type 2, and to return to the list type 1 .")
            
            print("To check out at any point, type check out !")
        if user == "2":
            if user == "1a":
                print(store.stock.get("Cherry soda"))
                print(store.stock.get("Cherry kombucha"))
                print("Please indicate which beverage you'd like: 1 soda 2 kombucha")
                user = input("")
                if user == "1":
                    cost = cost + 1.25
                if user == "2":
                    cost = cost + 3.25
                print("Added to your cart! Current total is:")
                print(cost)
                print("~To browse or revisit an aisle, type 2")
                print("~To view store stock, type 1")
                print("~To make your purchase, type check out")
            if user == "2a":
                print(store.stock.get("Sriracha Hippeas"))
                print(store.stock.get("Flamin Dorritos"))
                print("Please indicate which chips you'd like: 1 Hippeas 2 Dorritos")
                user = input("")
                if user == "1":
                    cost = cost + 4.50
                if user == "2":
                    cost = cost + 2.50
                print("Added to your cart! Current total is:")
                print(cost)
                print("~To browse or revisit an aisle, type 2")
                print("~To view store stock, type 1")
                print("~To make your purchase, type check out")
            if user == "3a":
                print(store.stock.get("Seaweed salad"))
                print(store.stock.get("Southwest salad"))
                print("Please indicate which salad you'd like: 1 Seaweed 2 Southwest")
                user = input("")
                if user == "1":
                    cost = cost + 4.75
                if user == "2":
                    cost = cost + 6.75        
                print("Added to your cart! Current total is:")
                print(cost)
                print("~To browse or revisit an aisle, type 2")
                print("~To view store stock, type 1")
                print("~To make your purchase, type check out")
            if user == "4a":
                print(store.stock.get("Greek yogurt"))
                print(store.stock.get("Sweet parfait"))
                print("Please indicate which dairy product you'd like: 1 yougurt 2 parfait")
                user = input("")
                if user == "1":
                    cost = cost + 3.50
                if user == "2":
                    cost = cost + 1.50
                print("Added to your cart! Current total is:")
                print(cost)
                print("To browse or revisit an aisle, type 2")
            if user == "5a":
                print(store.stock.get("Baked potato"))
                print(store.stock.get("French fries"))
                print("Please indicate which item you'd like: 1 baked potato 2 french fries")
                user = input("")
                if user == "1":
                    cost = cost + 5.50
                if user == "2":
                    cost = cost + 3.50
                print("Added to your cart! Current total is:")
                print(cost)
                print("To browse or revisit an aisle, type 2")
            
        user = input("")
        if user == "check out":
            print(cost)
            break

        

        
      
if __name__ == "__main__":
    main()
