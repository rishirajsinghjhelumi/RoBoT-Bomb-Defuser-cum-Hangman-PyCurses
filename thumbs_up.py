import curses,curses.panel,curses.ascii
win=curses.initscr()
curses.curs_set(0)	
curses.start_color()
curses.init_pair(1,curses.COLOR_CYAN,curses.COLOR_WHITE)
curses.init_pair(2,curses.COLOR_RED,curses.COLOR_WHITE)
size=win.getmaxyx()
b="Thumb's Up Man!!! Keep Going..."
x=[b[0:j] for j in range(1,len(b)+1)]
win.bkgd(curses.color_pair(1))
win.keypad(1)
win.nodelay(1)
win.border('|','|','*','*','(',')','(',')')
win.getch()
for i in x:
	win.addstr(size[0]/2-3,size[1]/2-10,"  ...../ )",curses.color_pair(2))
	win.addstr(size[0]/2-2,size[1]/2-10," .....' /",curses.color_pair(2))
	win.addstr(size[0]/2-1,size[1]/2-10,"  ---' (_____",curses.color_pair(2))
	win.addstr(size[0]/2,size[1]/2-10,"......... ((__)",curses.color_pair(2))
	win.addstr(size[0]/2+1,size[1]/2-10," ..... _ ((___)",curses.color_pair(2))
	win.addstr(size[0]/2+2,size[1]/2-10,"....... -'((__)",curses.color_pair(2))
	win.addstr(size[0]/2+3,size[1]/2-10,"   --.___((_)",curses.color_pair(2))
	curses.beep()
	win.addstr(5, size[1]/2-len(b)/2,i,curses.A_BLINK | curses.color_pair(2)|curses.A_UNDERLINE|curses.A_BOLD)
	curses.delay_output(80)
	win.refresh()
	win.clear()
	win.border('|','|','*','*','(',')','(',')')
curses.delay_output(1200)
curses.endwin()
