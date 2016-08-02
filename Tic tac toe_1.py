# coding: utf-8
import TicTacToeFunctions
PlayField = [[" "," "," "],
             [" "," "," "],
             [" "," "," "]]
x=0
Play = True
PlayFieldLen = len(PlayField)-1
while(x<=8 and Play):
	if(x%2==0):
		Player="x"
	else:
		Player="O"
	print("You're Player %s" % Player)
	X = input("What is the X coördinate?")
	Y = input("What is the Y coördinate?")
	X= int(X)
	Y = int(Y)
	if(X<=PlayFieldLen and Y<=PlayFieldLen and X>=0 and Y>=0):		
		PlayField=TicTacToeFunctions.InputHandler(Y,X,Player, PlayField)
		Play=TicTacToeFunctions.WinnerCheck(PlayField)
		x+=1
	else:
		print("invalid input please choose a coördnita between 0 and %s" % PlayFieldLen)
