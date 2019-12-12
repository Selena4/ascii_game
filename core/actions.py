import json,os, sys,time
import core.getch as getch

class game:
	def show_table(table,overview,x,y,name, icon, class_, level, exp, max_exp, hp, hp_max, gold, water, oxy,text, sym):
		count_enemy = 0	
		for line in table:
			count_enemy = count_enemy + line.count('E')
		x_pl = x
		y_pl = y
		if y - (overview//2) < 0:
			y = overview//2 
		if x - (overview//2) < 0:
			x = overview//2 
		if x + (overview//2) > len(table[y])-1:
			x = len(table[y]) - overview//2 -1
		if y + (overview//2) > len(table) -1: 
			y = len(table) - overview//2 -1
		output = '\r\n ' +'-'*((overview//2)*2+5) + '\n'
		output = output +' |' + ' '*((overview//2)*2 + 3) + '|      [' + icon + '] '+ name + ' ' + str(level) + ' lvl (' + str(hp) + '/' + str(hp_max) + ' hp) | gold: ' + str(gold)  + '\n'
		t = 0
		for line in table[y-(overview//2):y+(overview//2)+1]:
			if t == 1:
				output = output +' | ' + line[x-(overview//2):x+(overview//2)+1] + ' |      class: ' + class_ + ' | symbol: ' + sym + '\n'
			elif t == 3:
				output = output + ' | ' + line[x-(overview//2):x+(overview//2)+1] + ' |      exp: ' + str(exp) + ' / ' + str(max_exp) + '\n'
			elif t == 5: 
				output = output +' | ' + line[x-(overview//2):x+(overview//2)+1] + ' |      x: ' + str(x_pl+1) + ', y:' + str(y_pl+1) + ' | count emenies: '+ str(count_enemy) +'\n'
			elif t == 7:
				output = output + ' | ' + line[x-(overview//2):x+(overview//2)+1] + ' |      key \'H\' - show helping table \n'
			elif t == 9 and water:
				output = output + ' | ' + line[x-(overview//2):x+(overview//2)+1] + ' |      oxygen: ' + str(oxy) + '\n'
			else:
				output = output +' | ' + line[x-(overview//2):x+(overview//2)+1] + ' | \n'
			t += 1
		output = output + ' |' + ' '*((overview//2)*2 + 3) + '|\n'
		output = output + ' ' +'-'*((overview//2)*2+3)+'MAP\n'
		output = output + '\n' +text
		print(output)
	def set_marker(marker,table,x,y):
		table[y] = table[y][:x] + marker + table[y][x+1:]
		return table
	def move(key,floor,x,y,last_sym,icon):
		objects_sym = ['/','\\','-','_', '|']
		fly_sym = ["*","#"]
		if key  == 'W':
			if y - 1  < 0 or floor[y-1][x] in objects_sym: 
				sym = last_sym
				text = 'none'

			else:
				sym = floor[y-1][x]  
				game.set_marker(icon,floor,x,y-1)
				game.set_marker(last_sym,floor,x,y)
				y = y - 1
				text = ''
		if key  == 'D':
			if x + 1  > len(floor[y])-1 or floor[y][x+1] in objects_sym:
				sym = last_sym
				text = 'none'
			else:
				sym = floor[y][x+1]  
				game.set_marker(icon,floor,x+1,y)
				game.set_marker(last_sym,floor,x,y)
				x = x + 1
				text = ''
		if key  == 'A':
			if x - 1  < 0 or floor[y][x-1] in objects_sym: 
				sym = last_sym
				text = 'none'
			else:
				sym = floor[y][x-1]  
				game.set_marker(icon,floor,x-1,y)
				game.set_marker(last_sym,floor,x,y)
				x = x - 1
				text = ''
		if key  == 'S':
			if y + 1  > len(floor)-1 or floor[y+1][x] in objects_sym: 
				sym = last_sym
				text = 'none'
			else:
				sym = floor[y+1][x]  
				game.set_marker(icon,floor,x,y+1)
				game.set_marker(last_sym,floor,x,y)
				y = y + 1
				text = ''
		if sym in fly_sym:
			game.set_marker(sym,floor,x,y)
		return floor,x,y,sym, text
	def use(key, stat, log):
		if key == "H":
			os.system('cls')
			print('* L - legend of map')
			print('* I - show inventory')
			print('* Z - exit with save')
			print('* [ - use potion of health')
			print('* press any key')
			getch.getch()
		if key == "Z":
			os.system('cls')
			if input('are you sure?[y/n]').lower() == 'y':
				data.save_char(stat)
				exit()
			else:
				return
		if key == 'I':
			print('inventory:\n')
			for item in stat['inventory']:
				print(item)
			getch.getch()
		if key == 'G':
			os.system('cls')
			print(log)
			input()
class data:
	def save_char(stat):
		with open("resources/save/character", "w") as write_file:
			json.dump(stat, write_file)
	def restart_game():
		stat = json.loads(open('resources/restart_chr','r').read())
		with open("resources/save/character", "w") as write_file:
			json.dump(stat, write_file)
	def last_save():
		stat = json.loads(open('resources/save/chracter','r').read())
		return stat
