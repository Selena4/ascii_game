"""_________________________________________"""
import resources.floors as floor
import core.start as select_class
import core.actions as action
import core.getch as getch
import json, os,time, sys, threading, random
"""_________________________________________"""

#I recommend you run this file with cmd or terminal otherwise you can get errors
def main():
	global floor_now, stat, x_pl, y_pl, water, oxy, text, sym_now, log
	water = False
	log = 'log:\n\n'
	oxy = 30
	text = ''
	stat = json.loads(open('resources/save/character','r').read())
	if stat['name'] == '':
		stat = select_class.char.start_()
		action.game.save_char(stat)
	floor_now,x_pl,y_pl = floor.level.get_lvl(stat['floor'])[0], floor.level.get_lvl(stat['floor'])[1], floor.level.get_lvl(stat['floor'])[2]
	sym_now = floor_now[y_pl][x_pl]
	floor_now = action.game.set_marker(stat['icon'],floor_now,x_pl,y_pl)
	threads()
	while True:
		os.system('cls')
		action.game.show_table(floor_now,stat['overview'],x_pl,y_pl,stat['name'],stat['icon'],stat['class'],stat['level'],stat['exp'],stat['max_exp'],stat['hp'],stat['hp_max'], stat['gold'], water,oxy, text, sym_now) #name, icon, class_, level, exp, max_exp, hp, hp_max
		key = getch.getch_().decode('utf-8').upper()
		if key in ['W','A','S','D']:
			floor_now,x_pl,y_pl, sym_now, text = action.game.move(key,floor_now,x_pl,y_pl, sym_now,stat['icon'])
		else:
			action.game.use(key,stat,log)
		if sym_now == "~":
			water = True
			if oxy > 0:
				oxy -= 1
			if oxy == 0:
				stat['hp'] = stat['hp'] - 5
		else:
			water = False
			if oxy < 30:
				oxy += 1
		if stat['hp'] <= 0:
			action.game.relive()
			sym_now = ' '
			stat['hp'] = stat['hp_max']
			floor_now,x_pl,y_pl = floor.level.get_lvl(stat['floor'])[0], floor.level.get_lvl(stat['floor'])[1], floor.level.get_lvl(stat['floor'])[2]
			floor_now = action.game.set_marker(stat['icon'],floor_now,x_pl,y_pl)

def threads():
	thread = threading.Thread(target=spawning_enemies)
	thread.daemon = True
	thread.start()
def spawning_enemies():
	global floor_now, stat, x_pl, y_pl, water, oxy, text, sym_now, log
	while True:
		count_enemy = 0
		for line in floor_now:
			count_enemy = count_enemy + line.count('E')
		if count_enemy < 100:
			while True:
				x_en = random.randint(0,len(floor_now[0])-1)
				y_en = random.randint(0,len(floor_now)-1)
				if floor_now[y_en][x_en] == '.':

					floor_now = action.game.set_marker('E',floor_now,x_en,y_en)
					log = log + 'enemy spawned: ' + str(x_en+1) + ' ' + str(y_en+1) + '\n'
					break

if __name__ == "__main__":
	main()
