"""_________________________________________"""
import resources.floors as floor
import core.start as select_class
import core.actions as action
import core.getch as getch
import json, os
"""_________________________________________"""

def main():
	sym_now = '.'
	stat = json.loads(open('resources/character','r').read())
	if stat['name'] == '':
		stat = select_class.char.start_()
		action.game.save_char(stat)
	floor_now,x_pl,y_pl = floor.level.get_lvl(stat['floor'])[0], floor.level.get_lvl(stat['floor'])[1], floor.level.get_lvl(stat['floor'])[2]
	floor_now = action.game.set_marker('@',floor_now,x_pl,y_pl)
	while True:
		os.system('cls')
		action.game.show_table(floor_now,stat['overview'],x_pl,y_pl)
		floor_now,x_pl,y_pl, sym_now = action.game.key(getch.getch_().decode('utf-8').upper(),floor_now,x_pl,y_pl, sym_now)
if __name__ == "__main__":
	main()
