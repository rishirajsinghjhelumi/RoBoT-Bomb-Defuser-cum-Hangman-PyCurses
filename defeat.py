import curses,curses.panel,curses.ascii
win=curses.initscr()
curses.curs_set(0)	
curses.start_color()
curses.init_pair(1,curses.COLOR_CYAN,curses.COLOR_WHITE)
curses.init_pair(2,curses.COLOR_RED,curses.COLOR_WHITE)
size=win.getmaxyx()
m="Game By :-> Rishi Raj"
m1=b="CONGRATULATIONS !!"
x=[b[0:j] for j in range(1,len(b)+1)]
win.bkgd(curses.color_pair(1))
win.keypad(1)
win.nodelay(1)
win.border('|','|','*','*','(',')','(',')')
win.getch()
for i in x:
	win.addstr(size[0]/2-10,size[1]/2-15,"                              .-\"\"\"-.",curses.color_pair(2))
	win.addstr(size[0]/2-9,size[1]/2-15,"                            /`       `\ ",curses.color_pair(2))
	win.addstr(size[0]/2-8,size[1]/2-15,"     ,-==-.                ;           ;",curses.color_pair(2))
	win.addstr(size[0]/2-7,size[1]/2-15,"    /(    \`.              |           |",curses.color_pair(2))
	win.addstr(size[0]/2-6,size[1]/2-15,"   | \ ,-. \ (             :           ;",curses.color_pair(2))
	win.addstr(size[0]/2-5,size[1]/2-15,"    \ \`-.> ) 1             \         /",curses.color_pair(2))
	win.addstr(size[0]/2-4,size[1]/2-15,"     \_`.   | |              `._   _.`",curses.color_pair(2))
	win.addstr(size[0]/2-3,size[1]/2-15,"      \o_`-_|/                _|`\"'|-.",curses.color_pair(2))
	win.addstr(size[0]/2-2,size[1]/2-15,"     /`  `>.  __          .-'`-|___|_ )",curses.color_pair(2))
	win.addstr(size[0]/2-1,size[1]/2-15,"    |\  (^  >'  `>-----._/             )",curses.color_pair(2))
	win.addstr(size[0]/2,size[1]/2-15,"    | `._\ /    /      / |      ---   -;",curses.color_pair(2))
	win.addstr(size[0]/2+1,size[1]/2-15,"    :     `|   (      (  |      ___  _/",curses.color_pair(2))
	win.addstr(size[0]/2+2,size[1]/2-15,"     \     `.  `\      \_\      ___ _/",curses.color_pair(2))
	win.addstr(size[0]/2+3,size[1]/2-15,"      `.     `-='`t----'  `--.______/",curses.color_pair(2))
	win.addstr(size[0]/2+4,size[1]/2-15,"        `.   ,-''-.)           |---|",curses.color_pair(2))
	win.addstr(size[0]/2+5,size[1]/2-15,"          `.(,-=-./             \_/",curses.color_pair(2))
	win.addstr(size[0]/2+6,size[1]/2-15,"             |   |               V",curses.color_pair(2))
	win.addstr(size[0]/2+7,size[1]/2-15,"             |-''`-.             `.",curses.color_pair(2))
	win.addstr(size[0]/2+8,size[1]/2-15,"            /  ,-'-.\              `-.",curses.color_pair(2))
	win.addstr(size[0]/2+9,size[1]/2-15,"           |  (      \                `.",curses.color_pair(2))
	win.addstr(size[0]/2+10,size[1]/2-15,"            \  \     |               ,.'",curses.color_pair(2))
	curses.beep()
	win.addstr(size[0]-2, size[1]-len(m)-4,m,curses.A_BLINK | curses.color_pair(2)|curses.A_UNDERLINE|curses.A_BOLD)
	win.addstr(5, size[1]/2-len(b)/2,i,curses.A_BLINK | curses.color_pair(2)|curses.A_UNDERLINE|curses.A_BOLD)
	curses.delay_output(80)
	win.refresh()
	win.clear()
	win.border('|','|','*','*','(',')','(',')')
curses.delay_output(1200)
b="The VICTORY is YOURS....!!!!"
x=[b[0:j] for j in range(1,len(b)+1)]
for i in x:
	win.addstr(size[0]/2-10,size[1]/2-15,"                              .-\"\"\"-.",curses.color_pair(2))
	win.addstr(size[0]/2-9,size[1]/2-15,"                            /`       `\ ",curses.color_pair(2))
	win.addstr(size[0]/2-8,size[1]/2-15,"     ,-==-.                ;           ;",curses.color_pair(2))
	win.addstr(size[0]/2-7,size[1]/2-15,"    /(    \`.              |           |",curses.color_pair(2))
	win.addstr(size[0]/2-6,size[1]/2-15,"   | \ ,-. \ (             :           ;",curses.color_pair(2))
	win.addstr(size[0]/2-5,size[1]/2-15,"    \ \`-.> ) 1             \         /",curses.color_pair(2))
	win.addstr(size[0]/2-4,size[1]/2-15,"     \_`.   | |              `._   _.`",curses.color_pair(2))
	win.addstr(size[0]/2-3,size[1]/2-15,"      \o_`-_|/                _|`\"'|-.",curses.color_pair(2))
	win.addstr(size[0]/2-2,size[1]/2-15,"     /`  `>.  __          .-'`-|___|_ )",curses.color_pair(2))
	win.addstr(size[0]/2-1,size[1]/2-15,"    |\  (^  >'  `>-----._/             )",curses.color_pair(2))
	win.addstr(size[0]/2,size[1]/2-15,"    | `._\ /    /      / |      ---   -;",curses.color_pair(2))
	win.addstr(size[0]/2+1,size[1]/2-15,"    :     `|   (      (  |      ___  _/",curses.color_pair(2))
	win.addstr(size[0]/2+2,size[1]/2-15,"     \     `.  `\      \_\      ___ _/",curses.color_pair(2))
	win.addstr(size[0]/2+3,size[1]/2-15,"      `.     `-='`t----'  `--.______/",curses.color_pair(2))
	win.addstr(size[0]/2+4,size[1]/2-15,"        `.   ,-''-.)           |---|",curses.color_pair(2))
	win.addstr(size[0]/2+5,size[1]/2-15,"          `.(,-=-./             \_/",curses.color_pair(2))
	win.addstr(size[0]/2+6,size[1]/2-15,"             |   |               V",curses.color_pair(2))
	win.addstr(size[0]/2+7,size[1]/2-15,"             |-''`-.             `.",curses.color_pair(2))
	win.addstr(size[0]/2+8,size[1]/2-15,"            /  ,-'-.\              `-.",curses.color_pair(2))
	win.addstr(size[0]/2+9,size[1]/2-15,"           |  (      \                `.",curses.color_pair(2))
	win.addstr(size[0]/2+10,size[1]/2-15,"            \  \     |               ,.'",curses.color_pair(2))
	curses.beep()
	win.addstr(size[0]-2, size[1]-len(m)-4,m,curses.A_BLINK | curses.color_pair(2)|curses.A_UNDERLINE|curses.A_BOLD)
	win.addstr(4, size[1]/2-len(m1)/2,m1,curses.A_BLINK | curses.color_pair(2)|curses.A_UNDERLINE|curses.A_BOLD)
	win.addstr(5, size[1]/2-len(b)/2,i,curses.A_BLINK | curses.color_pair(2)|curses.A_UNDERLINE|curses.A_BOLD)
	curses.delay_output(80)
	win.refresh()
	win.clear()
	win.border('|','|','*','*','(',')','(',')')
curses.delay_output(1200)
curses.endwin()