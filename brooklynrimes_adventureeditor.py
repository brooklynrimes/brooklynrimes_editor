""" adventureEditor.py
    complete a text adventor editor
    node editor included 
    save and load --> JSON
"""
import json 

def main(): 
    game = getDefaultGame()
    keepGoing = True
    while keepGoing:  
        userChoice = getMenuChoice() 
        if userChoice == "0": 
            keepGoing = False 
        elif userChoice == "1": 
             print("load default game")
             game = getDefaultGame() 
        elif userChoice == "2": 
             print(" load a game file") 
             game = loadGame()
        elif userChoice == "3": 
            print("save current game")
            saveGame(game)
        elif userChoice == "4":
             print("edit or add a name")
             game = editNode(game)
        elif userChoice == "5":
             playGame(game) 
        else: 
             print("Oh no you made a mistake")

def getMenuChoice(): 
    """ prints a menu guarantees a result string 0-5 """

    print(""" 
        0) exit
        1) load default game
        2) load a game file
        3) save the current game
        4) edit or add a node
        5) play the current game """)
    userChoice = input("Your choice \n")

    return userChoice

def getDefaultGame(): 
    game = { 
        "Start" : ["You can start over or quit forever","Start over","Start", "Quit", "quit"]
    }
    return game 

def playNode(game,currentGame):
    (desc, menuA, nodeA, menuB, nodeB,) = game[currentGame]
    userChoice = input (desc + "\n1)" + menuA + "\n2)" + menuB + "\n")
    if userChoice ==("1"):
        newNode = nodeA
    elif userChoice == ("2"):
        newNode = nodeB
    else: 
        newNode = currentGame 
    return newNode

def playGame(game):
    game = getDefaultGame()
    currentGame = "Start"
    keepGoing = True 
    while keepGoing:
        currentGame= playNode( game, currentGame) 
        if currentGame =="quit":
            keepGoing = False

def saveGame(game):
    saveFile = open("game.json", "w") 
    json.dump(game, saveFile, indent= 2)
    saveFile.close()

def loadGame():
    loadFile = open("game.json", "r")
    game = json.load(loadFile)
    loadFile.close()
    return game 

def editNode(game):
    print("These node names are currently in use")
    print(json.dumps(game, indent=2))
    for nodeName in game.keys(): 
        print(f"{nodeName}")
    newNodeName = input("Input new node. If node name exists, no new node will be added")
    if newNodeName in game.keys():
        newNode = game[newNodeName]
    else: 
        newNode = ["","","","",""]
        #copy that node to other node 
        #or else... create newNode w/ empty data
    (desc, menuA, nodeA, menuB, nodeB) = newNode
    #use editField() --> user to edit each node 
    newDesc = getField("description", desc)
    newMenuA= getField("Menu A", menuA)
    newNodeA = getField("Node A", nodeA)
    newMenuB = getField("Menu B", menuB)
    newNodeB = getField("Node B", nodeB)

    game[newNodeName] = [newDesc, newMenuA, newNodeA, newMenuB, newNodeB]
    return game 

def getField(prompt, currentValue):
    #get field name
    newVal = input(f"{prompt} ({currentValue}): ")
    if newVal == "": 
        newVal = currentValue
    return newVal
        # print field's currrent value
        #user press enter quickly
        #retain current val
        #or else...
        #use new val

main() 


