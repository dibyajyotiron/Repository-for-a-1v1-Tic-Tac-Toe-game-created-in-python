#import random

board = ["0"," "," "," "," "," "," "," "," "," "]
board1 = ["0","1","2","3","4","5","6","7","8","9"]



def show_board():
	print(" " * 3 + "|" + " " * 3 + "|")
	print(" " + board[1] + " " + "|" + " " + board[2] + " " + "|" + " " + board[3] + " ")
	print(" " * 3 + "|" + " " * 3 + "|")
	print("-" * 3 + "|" + "-" * 3 + "|" + "-" * 3)
	print(" " * 3 + "|" + " " * 3 + "|")
	print(" " + board[4] + " " + "|" + " " + board[5] + " " + "|" + " " + board[6] + " ")
	print(" " * 3 + "|" + " " * 3 + "|")
	print("-" * 3 + "|" + "-" * 3 + "|" + "-" * 3)
	print(" " * 3 + "|" + " " * 3 + "|")
	print(" " + board[7] + " " + "|" + " " + board[8] + " " + "|" + " " + board[9] + " ")
	print(" " * 3 + "|" + " " * 3 + "|")


def show_board1():
	print(" " * 3 + "|" + " " * 3 + "|")
	print(" " + board1[1] + " " + "|" + " " + board1[2] + " " + "|" + " " + board1[3] + " ")
	print(" " * 3 + "|" + " " * 3 + "|")
	print("-" * 3 + "|" + "-" * 3 + "|" + "-" * 3)
	print(" " * 3 + "|" + " " * 3 + "|")
	print(" " + board1[4] + " " + "|" + " " + board1[5] + " " + "|" + " " + board1[6] + " ")
	print(" " * 3 + "|" + " " * 3 + "|")
	print("-" * 3 + "|" + "-" * 3 + "|" + "-" * 3)
	print(" " * 3 + "|" + " " * 3 + "|")
	print(" " + board1[7] + " " + "|" + " " + board1[8] + " " + "|" + " " + board1[9] + " ")
	print(" " * 3 + "|" + " " * 3 + "|")

# show_board()






# def player_input():
# 	inp = ""
# 	while not(inp == "X" or inp == "O"):
# 		inp = input("What do you want to use, X or O : ").upper()
# 	if inp == "X":
# 		return "X"
# 	else:
# 		return "O"


def position1():
	pos = int(input("{}, Enter the position for X : ".format(p1)))
	if board[pos] == " ":
		board[pos] = "X"
		show_board()
	else:
		print("This is already taken!!")
def position2():
	pos2 = int(input("{}, Enter the position for O: ".format(p2)))
	if board[pos2] == " ":
		board[pos2] = "O"
	else:
		print("This is already taken!!")


def win():
	while True:
		position1()
		position2()
		show_board()
		if board[1] == board[2] == board[3]=="X":
			print("Game Over!! {} wins!!" .format(p1))
			break
		elif board[1] == board[2] == board[3]=="O":
			print("Game Over!! {} wins!!".format(p2))
			break
		elif board[4] == board[5] == board[6]=="X":
			print("Game Over!! {} wins!!".format(p1))
			break
		elif board[4] == board[5] == board[6]=="O":
			print("Game Over!! {} wins!!".format(p2))
			break
		elif board[7] == board[8] == board[9]=="X":
			print("Game Over!! {} wins!!".format(p1))
			break
		elif board[7] == board[8] == board[9]=="O":
			print("Game Over!! {} wins!!".format(p2))
			break
		elif board[1] == board[4] == board[7]=="X":
			print("Game Over!! {} wins!!".format(p1))
			break
		elif board[1] == board[4] == board[7]=="O":
			print("Game Over!! {} wins!!".format(p2))
			break
		elif board[2] == board[5] == board[8]=="X":
			print("Game Over!! {} wins!!".format(p1))
			break
		elif board[2] == board[5] == board[8]=="O":
			print("Game Over!! {} wins!!".format(p2))
			break
		elif board[3] == board[6] == board[9]=="X":
			print("Game Over!! {} wins!!".format(p1))
			break
		elif board[3] == board[6] == board[9]=="O":
			print("Game Over!! {} wins!!".format(p2))
			break
		elif board[1] == board[5] == board[9]=="X":
			print("Game Over!! {} wins!!".format(p1))
			break
		elif board[1] == board[5] == board[9]=="O":
			print("Game Over!! {} wins!!".format(p2))
			break
		elif board[3] == board[5] == board[7]=="X":
			print("Game Over!! {} wins!!".format(p1))
			break
		elif board[3] == board[5] == board[7]=="O":
			print("Game Over!! {} wins!!".format(p2))
			break
		if tie():
			print("Ended up in a tie!!")
			break

def tie():
	fullBoard = True
	for i in range(1, 10):
		if board[i] == " ":
			fullBoard = False
			return False
	if fullBoard == True:
		return True


print("Welcome to this tic tac toe game!!\n This is how the demo board looks with all it's positions marked!!!")

show_board1()
print("So now that you've seen the demo board-\n\nLet's begin\n\n ")


print('ENTER YOUR NAMES:\n'
	  '(Remember if you select "X" you are player one, so name accordingly')
p1 = input("Player 1, enter your name: ")
p2 = input("Player 2, enter your name: ")


position1()
position2()
show_board()
win()



