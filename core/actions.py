import json

class game:
	def save_char(stat):
		with open("resources/character", "w") as write_file:
			json.dump(stat, write_file)
	def restart_game():
		stat = json.loads(open('resources/restart_chr','r').read())
		with open("resources/character", "w") as write_file:
			json.dump(stat, write_file)
	def show_table(table,overview,x,y,name, icon, class_, level, exp, max_exp, hp, hp_max):
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
		print('')
		print(' ' +'-'*((overview//2)*2+5))
		print(' |' + ' '*((overview//2)*2 + 3) + '|      [' + icon + '] '+ name + ' ' + str(level) + ' lvl (' + str(hp) + '/' + str(hp_max) + ' hp)')
		t = 0
		for line in table[y-(overview//2):y+(overview//2)+1]:
			if t == 1:
				print(' | ' + line[x-(overview//2):x+(overview//2)+1] + ' |      class: ' + class_)
			elif t == 3:
				print(' | ' + line[x-(overview//2):x+(overview//2)+1] + ' |      exp: ' + str(exp) + ' / ' + str(max_exp))
			elif t == 5: 
				print(' | ' + line[x-(overview//2):x+(overview//2)+1] + ' |      x: ' + str(x_pl+1) + ', y:' + str(y_pl+1))
			else:
				print(' | ' + line[x-(overview//2):x+(overview//2)+1] + ' |')
			t += 1
		print(' |' + ' '*((overview//2)*2 + 3) + '|')
		print(' ' +'-'*((overview//2)*2+3)+'MAP')
	def set_marker(marker,table,x,y):
		table[y] = table[y][:x] + marker + table[y][x+1:]
		return table
	def key(key,floor,x,y,last_sym,icon):
		if key  == 'W':
			if y - 1  < 0: 
				print('none')
				return floor,x,y,last_sym
			sym = floor[y-1][x]  
			game.set_marker(icon,floor,x,y-1)
			game.set_marker(last_sym,floor,x,y)
			return floor, x,y-1,sym
		if key  == 'D':
			if x + 1  > len(floor[y])-1:
				print('none')
				return floor,x,y,last_sym
			sym = floor[y][x+1]  
			game.set_marker(icon,floor,x+1,y)
			game.set_marker(last_sym,floor,x,y)
			return floor, x+1,y,sym
		if key  == 'A':
			if x - 1  < 0: 
				print('none')
				return floor,x,y,last_sym
			sym = floor[y][x-1]  
			game.set_marker(icon,floor,x-1,y)
			game.set_marker(last_sym,floor,x,y)
			return floor, x-1,y,sym
		if key  == 'S':
			if y + 1  > len(floor)-1: 
				print('none')
				return floor,x,y,last_sym
			sym = floor[y+1][x]  
			game.set_marker(icon,floor,x,y+1)
			game.set_marker(last_sym,floor,x,y)
			return floor, x,y+1,sym