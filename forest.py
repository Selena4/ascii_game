
import random
import getch
import os


def join(x):
	def show_table():
		for x_ in table:
			y_ = ''
			for y__ in x_:
				y_ = y_ + y__
			print(y_)

	def move(char):
		if char.upper() == "A":
			if table[player_xy[1]][player_xy[0]-1] in obj:
				print('')
			elif table[player_xy[1]][player_xy[0]-1] == "E":
				start_battle()
			else:
				table[player_xy[1]][player_xy[0]] = "."
				table[player_xy[1]][player_xy[0]-1] = "@"
				player_xy[0] = player_xy[0] - 1
		if char.upper() == "D":
			if table[player_xy[1]][player_xy[0]+1] in obj:
				print('')
			elif table[player_xy[1]][player_xy[0]+1] == "E":
				start_battle()
			else:
				table[player_xy[1]][player_xy[0]] = "."
				table[player_xy[1]][player_xy[0]+1] = "@"
				player_xy[0] = player_xy[0] + 1
		if char.upper() == "S":
			if table[player_xy[1]+1][player_xy[0]] in obj:
				print('')
			elif table[player_xy[1]+1][player_xy[0]] == "E":
				start_battle()
			else:
				table[player_xy[1]][player_xy[0]] = "."
				table[player_xy[1]+1][player_xy[0]] = "@"
				player_xy[1] = player_xy[1] + 1
		if char.upper() == "W":
			if table[player_xy[1]-1][player_xy[0]] in obj:
				print('')
			elif table[player_xy[1]-1][player_xy[0]] == "E":
				start_battle()
			else:
				table[player_xy[1]][player_xy[0]] = "."
				table[player_xy[1]-1][player_xy[0]] = "@"
				player_xy[1] = player_xy[1] - 1
		if player_xy == []:
			start_battle_boss()

	obj = [chr(92), chr(47),"-","_","|"]
	enemies = {
	"1": {"hp":15,"att": 2,"def": 5}
	}



	if x == 1:
		player_xy = [3,3]
		table = [
		"_____________________________               ",
		"|...........................|               ",
		"|...........................|               ",
		"|...........................|               ",
		"|...........................|               ",
		"|...........................|               ",
		"-------------------|..|-----|               ",
		"                   |..|                     ",
		"                   |..|                     ",
		"-------------------|..|------               ",
		"|...........................|               ",
		"|...........................|               ",
		"|...........................|               ",
		"|...........................|    ___________",
		"|...........................|____|.........|",
		"|.....................................B....|",
		"|..........................................|",
		"-------------------------------------------|"
		]



	for i in range(len(table)):
		table[i] = list(table[i])
	table[player_xy[1]][player_xy[0]] = "@"
	for x_line in range(len(table)):
		for y_line in range(len(table[x_line])):
			if table[x_line][y_line] == ".":
				chaince = random.randint(1,100)
				if chaince <= 10:
					table[x_line][y_line] = "E"
	while True:
		os.system('clear')
		show_table()
		move(getch.getch())

join(1)
