import curses,curses.panel,curses.ascii,sys
win=curses.initscr()
curses.curs_set(0)
curses.start_color()
curses.init_pair(1,curses.COLOR_CYAN,curses.COLOR_WHITE)
curses.init_pair(2,curses.COLOR_RED,curses.COLOR_WHITE)
size=win.getmaxyx()
m1=b="The Devil has planted BOMBS all across the city......"
x=[b[0:j] for j in range(1,len(b)+1)]
win.bkgd(curses.color_pair(1))
win.keypad(1)
win.nodelay(1)
win.border('|','|','*','*','(',')','(',')')
win.getch()
key=1
for i in x:
	curses.beep()
	win.addstr(size[0]/2, size[1]/2-len(b)/2,i,curses.A_BLINK | curses.color_pair(2)|curses.A_UNDERLINE|curses.A_BOLD)
	curses.delay_output(40)
	win.refresh()
	win.clear()
	win.border('|','|','*','*','(',')','(',')')
curses.delay_output(800)
m2=b="Now it's up to you (The Good Guy) to save the city....."
x=[b[0:j] for j in range(1,len(b)+1)]
for i in x:
	curses.beep()
	win.addstr(size[0]/2-1, size[1]/2-len(m1)/2,m1,curses.A_BLINK | curses.color_pair(2)|curses.A_UNDERLINE|curses.A_BOLD)
	win.addstr(size[0]/2, size[1]/2-len(b)/2,i,curses.A_BLINK | curses.color_pair(2)|curses.A_UNDERLINE|curses.A_BOLD)
	curses.delay_output(40)
	win.refresh()
	win.clear()
	win.border('|','|','*','*','(',')','(',')')
curses.delay_output(800)
b="So Start Defusing BOMBS !!!!!"
x=[b[0:j] for j in range(1,len(b)+1)]
for i in x:
	curses.beep()
	win.addstr(size[0]/2-2, size[1]/2-len(m1)/2,m1,curses.A_BLINK | curses.color_pair(2)|curses.A_UNDERLINE|curses.A_BOLD)
	win.addstr(size[0]/2-1, size[1]/2-len(m2)/2,m2,curses.A_BLINK | curses.color_pair(2)|curses.A_UNDERLINE|curses.A_BOLD)
	win.addstr(size[0]/2, size[1]/2-len(b)/2,i,curses.A_BLINK | curses.color_pair(2)|curses.A_UNDERLINE|curses.A_BOLD)
	curses.delay_output(40)
	win.refresh()
	win.clear()
	win.border('|','|','*','*','(',')','(',')')
curses.delay_output(1200)
curses.endwin()
