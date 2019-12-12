import os,time

def start():         #XDDDDD                                                         
	line1_ = ''
	line2_ = ''
	line3_ = ''
	line4_ = ''
	line5_ = ''
	line6_ = ''
	line7_ = ''
	line1 = '\n\n`7MMF\'     A     `7MF\' .g8""8q. `7MM"""Mq. `7MMF\'      `7MM\"\"\"Yb.    '
	line2 = '  `MA     ,MA     ,V .dP\'    `YM. MM   `MM.  MM          MM    `Yb.'
	line3 = '   VM:   ,VVM:   ,V  dM\'      `MM MM   ,M9   MM          MM     `Mb'
	line4 = '    MM.  M\' MM.  M\'  MM        MM MMmmdM9    MM          MM      MM'
	line5 = '    `MM A\'  `MM A\'   MM.      ,MP MM  YM.    MM      ,   MM     ,MP'
	line6 = '     :MM;    :MM;    `Mb.    ,dP\' MM   `Mb.  MM     ,M   MM    ,dP\''
	line7 = '      VF      VF       `"bmmd\"\' .JMML. .JMM.JMMmmmmMMM .JMMmmmdP\'  '
	print('\n\n')
	for i in range(len(line2)):
		os.system('cls')
		line1_ = line1_ + line1[i]
		line2_ = line2_ + line2[i]
		line3_ = line3_ + line3[i]
		line4_ = line4_ + line4[i]
		line5_ = line5_ + line5[i]
		line6_ = line6_ + line6[i]
		line7_ = line7_ + line7[i]
		print(line1_)
		print(line2_)
		print(line3_)
		print(line4_)
		print(line5_)
		print(line6_)
		print(line7_)
		time.sleep(0.02)
                                                                    
	input('\n\nwelcome to gorgeous ascii game world! good to see you again, move on. [Enter]')


