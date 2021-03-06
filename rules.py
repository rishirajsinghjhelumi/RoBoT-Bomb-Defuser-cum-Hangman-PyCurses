import curses,curses.panel,curses.ascii,sys
win=curses.initscr()
curses.curs_set(0)
curses.start_color()
curses.init_pair(1,curses.COLOR_CYAN,curses.COLOR_WHITE)
curses.init_pair(2,curses.COLOR_RED,curses.COLOR_WHITE)
curses.init_pair(3,curses.COLOR_BLACK,curses.COLOR_WHITE)
size=win.getmaxyx()
m=[]
m.append("Rule No.1 -> You have to guess the meaning DIFFUSE CODE that can be created by the alphabets given.")
m.append("Rule No.2 -> You have to take the alphabets in the GIVEN ORDER ONLY.")
m.append("Rule No.3 -> If You take a wrong alphabet then the previous alphabet will appear again.")
m.append("Rule No.4 -> If two or more alphabets are same you have to take it in orderly manner according to the DIFFUSE CODE.")
m.append("Rule No.5 -> You have to complete the level within the time specified.")
m.append("Rule No.6 -> There will be a 2 second penalty for walking over a wrong alphabet.")
m.append("Rule No.7 -> You have to dodge the enemy bombs falling.If you hit your GAME IS OVER.")
m.append("Rule No.8 -> After getting the DIFFUSE CODE you have to go to the bomb to complete level.")
win.bkgd(curses.color_pair(1))
win.keypad(1)
win.nodelay(1)
win.border('|','|','*','*','(',')','(',')')
win.getch()
for k in range(len(m)):
	b=m[k]
	x=[b[0:j] for j in range(1,len(b)+1)]
	for i in x:
		for l in range(k):
			win.addstr(3+2*l,4,m[l],curses.A_BLINK | curses.color_pair(2)|curses.A_UNDERLINE|curses.A_BOLD)
		win.addstr(3+2*k,4,i,curses.A_BLINK | curses.color_pair(2)|curses.A_UNDERLINE|curses.A_BOLD)
		curses.beep()
		curses.delay_output(20)
		win.refresh()
		win.clear()
		win.border('|','|','*','*','(',')','(',')')
		win.addstr(size[0]-4,4,"Use Arrow Keys To move.",curses.color_pair(3)|curses.A_BOLD)
		win.addstr(size[0]-3,4,"Use \"P\" or \"p\" to Pause the Game.",curses.color_pair(3)|curses.A_BOLD) 
		win.addstr(size[0]-2,4,"Use Esc to Exit the Game any time.",curses.color_pair(3)|curses.A_BOLD)
	curses.delay_output(100)
curses.delay_output(5000)
curses.endwin()
