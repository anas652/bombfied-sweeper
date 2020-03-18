import tkinter
import random

game_over = False
score = 0 
squarestoclear = 0

def play_bombdodger():
	createbombfield(bombfield)
	window=tkinter.Tk()
	layout_window(window)
	window.mainloop()


bombfield = []
def createbombfield(bombfield):
	global squarestoclear
	for row in range(0,10):
		rowlist = []
		for column in range(0,10):
			if random.randint(1,100) < 20:
				rowlist.append(1)
			else:
				rowlist.append(0)
				squarestoclear = squarestoclear + 1
		bombfield.append(rowlist)
	#printfield(bombfield)


def printfield(bombfield):
	for rowlist in bombfield:
		print(rowlist)



	

def layout_window(window):
	for rowNumber, rowlist in enumerate(bombfield):
		for columnNumber, columnEntry in enumerate(rowlist):
			if random.randint(1,90) < 30:
				square = tkinter.Label(window, text = "    ", bg = "darkgreen")
			elif random.randint(1,100) > 60:
				square = tkinter.Label(window, text = "    ", bg = "sea green")
			else:
				square = tkinter.Label(window, text = "    ", bg = "darkseagreen")
			square.grid(row = rowNumber, column = columnNumber)
			square.bind("<Button-1>", on_click) 


def on_click(event):
	global score
	global game_over
	global squarestoclear
	square = event.widget
	row = int(square.grid_info()["row"])
	column = int(square.grid_info()["column"])
	currentText = square.cget("text")
	if game_over == False:

		if bombfield[row][column] == 1:
			
			game_over = True
			square.config(bg = "red")
			print("Game over you hit a bomb!")
			print("your score was:", score)
		elif currentText == "    ":
			square.config(bg = "brown")
			totalBombs = 0





		#elif bombfield[row][column] == 0:
			#score = score+1
			#squarestoclear = squarestoclear-





play_bombdodger()













