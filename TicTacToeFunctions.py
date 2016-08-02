# coding: utf-8
def InputHandler(Y,X,Player, PlayField):
	PlayField[Y][X] = Player
	print(PlayField[0])
	print(PlayField[1])
	print(PlayField[2])
	return PlayField
def WinnerCheck(PlayField):
	x=0
	while(x<len(PlayField)):
		x1 = 1
		WinnerCheck = 0 
		while(x1<len(PlayField)):
			if(PlayField[x][x1]==PlayField[x][x1-1] and PlayField[x][x1]!=" "):
				WinnerCheck+=1
				if (WinnerCheck==2):
					print ("Someone won")
					return False
			x1+=1
		x2 = 1
		WinnerCheck2 = 0
		while(x2<len(PlayField)):
			if(PlayField[x2][x]==PlayField[x2-1][x] and PlayField[x2][x]!=" "):
				WinnerCheck2+=1
				if (WinnerCheck2==2):
					print ("Someone won")
					return False
			x2+=1
		if(PlayField[0][0] == PlayField[1][1] and PlayField[1][1] == PlayField[2][2] and PlayField[1][1]!=" "):
			print ("Someone won")
			return False
		if(PlayField[0][2] == PlayField[1][1] and PlayField[1][1] == PlayField[2][0] and PlayField[1][1] !=" "):
			print ("Someone won")
			return False
		x+=1
		return True
	
