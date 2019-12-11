"""_________________________________________"""
import resources.floors as floor
import core.start as select_class
import core.actions as action
import core.getch as getch
import json, os,time, sys
"""_________________________________________"""

#I recommend you run this file with cmd or terminal otherwise you can get errors

def main():
	water = False
	oxy = 30
	sym_now = '.'
	text = ''
	stat = json.loads(open('resources/save/character','r').read())
	if stat['name'] == '':
		stat = select_class.char.start_()
		action.game.save_char(stat)
	floor_now,x_pl,y_pl = floor.level.get_lvl(stat['floor'])[0], floor.level.get_lvl(stat['floor'])[1], floor.level.get_lvl(stat['floor'])[2]
	floor_now = action.game.set_marker(stat['icon'],floor_now,x_pl,y_pl)
	while True:
		os.system('cls')
		action.game.show_table(floor_now,stat['overview'],x_pl,y_pl,stat['name'],stat['icon'],stat['class'],stat['level'],stat['exp'],stat['max_exp'],stat['hp'],stat['hp_max'], stat['gold'], water,oxy, text) #name, icon, class_, level, exp, max_exp, hp, hp_max
		time.sleep(1/(stat['dex']*3))
		key = getch.getch_().decode('utf-8').upper()
		if key in ['W','A','S','D']:
			floor_now,x_pl,y_pl, sym_now, text = action.game.move(key,floor_now,x_pl,y_pl, sym_now,stat['icon'])
		else:
			action.game.use(key,stat)
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

if __name__ == "__main__":
	main()
