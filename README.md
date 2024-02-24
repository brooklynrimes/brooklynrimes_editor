Brooklyn Rimes 
CS 120 
Andy Harris
23 February 2024
Psuedocode
Import json

main()
While keepGoing = True
Runs the main loop
Run getMenuChoice

getMenuChoice()
	print(f”””
      0) exit
      1) load default game
      2) load a game file
      3) save the current game
      4) edit or add a node
      5) play the current game
“””)
Make variable validAnswer = false
Loop while validAnswer = false
Take input
Convert to string
If not a valid answer 
Print (Please input a valid response)
Else validAnswer = true
 check value of input.
			If 0 keepGoing = False
			If 1 run getDefaultGame
			If 2 run loadGame
			If 3 run saveGame
			If 4 run editNode
	If 5 run playGame


playGame()
game = activeGame
    inGame = True
    activeNode = "start"
    while(inGame == True):
        if activeNode == "quit":
            inGame = False
        else:
            activeNode = playNode(activeNode, game)

playNode()
def playNode(activeNode, game):
    (description, menu1, node1, menu2, node2) = game[activeNode]

    print(f"""
          {description}
          1. {menu1}
          2. {menu2}
          """)
    choice = input("please type the number that corresponds to your desired course of action: ")
    if choice == "1":
        activeNode = node1
    elif choice == "2":
        activeNode = node2
    else:
        print("Improper input. Please try again.")
    return(activeNode)

getDefaultGame()
		activeGame = {
			“Alone”: [“Do you win or lose?”, “win”, “start”, “Lose”, “quit”]
return(activeGame)

editNode()
for key in  activeGame.keys():
        print(f"  {key}")
selection = input(“input the node would you like to edit: ”)
If selection in nodes
	newNode = activeGame[selection}
else
newNode = [“”,””,””,””,]
(description, menu1, node1, menu2, node2) = newNode
newDescription = editField(description)
		newMenu1 = editField(“menu1” menu1)
		newNode1 = editField(“node1” node1)
		newMenu2 = editField(“menu2” menu2)
		newNode2 = editField(“node2”node2)
		activeGame[newNode] = [newMenu1, newNode1, newMenu2, newNode2,]
return(activeGame)

editField(prompt, curentValue)
print (prompt, curentValue)
edits = input(“please enter the new value”)
if edits = “”
	edits = curentValue
print(“Saved”)
return edits


saveGame(activeGame)
outFile = open("game.json", "w")
    json.dump(activeGame, outFile, indent=2)
    outFile.close()
print(“Game Saved”)


loadGame()
inFile = open("game.json", "r")
activeGame = json.load(inFile)
print(“Data loaded.”)
return (activeGame)
