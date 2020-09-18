#Author: Jasper Gordon
#Created 17 September 2020
#Image source: https://www.pinterest.com/pin/499618152405878049/

from PIL import Image
import numpy as np
import random as rand
import random

#Width of final image
WIDTH = 1200

#height of final image
HEIGHT = 1200

#List of possible ingredients
ingredients = ["hamburger", "bottomBun", "cheese", "topBun"]

#List of lists containing ingredient transition combinations
toppingTransitions = [["hh", "hBb", "hc", "hTb"], ["Bbh", "BbBb", "Bbc", "BbTb"], ["ch", "cBb", "cc", "cTb"],
                    ["Tbh", "TbBb", "Tbc", "TbTb"]]

#List of lists containing probabilities corresponding to possible ingredient combinations
toppingMatrix = [[.3, .1, .35, .25], [.6, .05, .15, .2], [.3, .05, .2, .45], [.25, .25, .25, .25]]

# A method to randomly choose one of the possible toppings
# Returns a topping name as a string                
def topping_generator():   
        randomInt = random.randint(0,3)
        return ingredients[randomInt]

# A method that implements a Markov chain to construct a "burger" image of various ingridients
# Args:  int toppings = The number of ingredients in the burger
# Returns a list of strings
def build_burger (toppings):
        #Starting base topping
        curTopping = topping_generator()
        #List to hold the selected toppings
        toppingList = [curTopping]
        i = 0
        #starting probability
        prob = 1
        while i != toppings:
                if curTopping == "hamburger":
                        change =  np.random.choice(toppingTransitions[0],replace=True,p=toppingMatrix[0])
                        if change == "hh":
                                prob *= toppingMatrix[0][0]
                                toppingList.append("hamburger")
                        elif change == "hBb":
                                prob *= toppingMatrix[0][1]
                                curTopping = "bottomBun"
                                toppingList.append("bottomBun")
                        elif change == "hc":
                                prob *= toppingMatrix[0][2]
                                curTopping = "cheese"
                                toppingList.append("cheese")
                        else:
                                prob *= toppingMatrix[0][3]
                                curTopping = "topBun"
                                toppingList.append("topBun")
                elif curTopping == "bottomBun":
                        change =  np.random.choice(toppingTransitions[1],replace=True,p=toppingMatrix[1])
                        if change == "Bbh":
                                prob *= toppingMatrix[1][0]
                                curTopping = "hamburger"
                                toppingList.append("hamburger")
                        elif change == "BbBb":
                                prob *= toppingMatrix[1][1]
                                toppingList.append("bottomBun")
                        elif change == "Bbc":
                                prob *= toppingMatrix[1][2]
                                curTopping = "cheese"
                                toppingList.append("cheese")
                        else:
                                prob *= toppingMatrix[1][3]
                                curTopping = "topBun"
                                toppingList.append("topBun")
                elif curTopping == "cheese":
                        change =  np.random.choice(toppingTransitions[2],replace=True,p=toppingMatrix[2])
                        if change == "ch":
                                prob *= toppingMatrix[2][0]
                                curTopping = "hamburger"
                                toppingList.append("hamburger")
                        elif change == "cBb":
                                prob *= toppingMatrix[2][1]
                                curTopping = "bottomBun"
                                toppingList.append("bottomBun")
                        elif change == "cc":
                                prob *= toppingMatrix[2][2]
                                toppingList.append("cheese")
                        else:
                                prob *= toppingMatrix[2][3]
                                curTopping = "topBun"
                                toppingList.append("topBun")
                elif curTopping == "topBun":
                        change =  np.random.choice(toppingTransitions[3],replace=True,p=toppingMatrix[3])
                        if change == "Tbh":
                                prob *= toppingMatrix[3][0]
                                curTopping = "hamburger"
                                toppingList.append("hamburger")
                        elif change == "TbBb":
                                prob *= toppingMatrix[3][1]
                                curTopping = "bottomBun"
                                toppingList.append("bottomBun")
                        elif change == "Tbc":
                                prob *= toppingMatrix[3][2]
                                curTopping = "cheese"
                                toppingList.append("cheese")
                        else:
                                prob *= toppingMatrix[3][3]
                                toppingList.append("topBun")
                i += 1
        return toppingList

# A method to transform an "order" into a visual image of a burger using a list of strings
# Stacks ingridinets in burger from the bottom up
# Args: List order = a list of strings
def burger_drawer(order):
        img = Image.new("RGB", (WIDTH, HEIGHT),(255,255,255))
        #Variable to determine where to place the next topping
        imgBound = HEIGHT
        i = 0
        while i < len(order):
                #Case where burger doesn't fit on screen
                if imgBound <= 0:
                        print ("You have reached toppings limit.")
                        img.show()
                        exit()
                else:        
                        newTopping = Image.open(order[i] + ".png")
                        toppingHeight = newTopping.height
                        img.paste(newTopping, (int((WIDTH/2)-int(newTopping.width/2)), imgBound - toppingHeight))
                        #Adjust placement of each new topping by moving upwards the height of the previous
                        imgBound -= toppingHeight
                        i += 1
        img.show()

burger_order = build_burger(7)
burger_drawer(burger_order)
