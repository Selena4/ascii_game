import json

class char:
	def start_():
		stat = json.loads(open('resources/restart_chr','r').read())
		while stat['name'] == '':
			stat['name'] = input('say your name, hero: ')
			if stat['name'] == '':
				print('your nickname cannot be empty')
		while True:
			choice = input('choose your class: \na) mage\nb) knight\nc) rogue\nclass: ')
			if choice == 'a':
				stat['class'],stat['hp'], stat['hp_max'], stat['str'], stat['def'], stat['tal'], stat['dex'] = 'mage',60,60,2,2,8,3
				break
			elif choice == 'b':
				stat['class'],stat['hp'], stat['hp_max'], stat['str'], stat['def'], stat['tal'], stat['dex'] = 'knight',120,120,4,6,2,1
				break
			elif choice == 'c':
				stat['class'],stat['hp'], stat['hp_max'], stat['str'], stat['def'], stat['tal'], stat['dex'] = 'rogue',80,80,6,2,1,5
				break
			else:
				print('uncorrect class')
		input('congratulations! your class is ' + stat['class'] + ' now. start your way, ' + stat['name'])
		return stat 