import curses,curses.panel,curses.ascii
win=curses.initscr()
curses.curs_set(0)	
curses.start_color()
curses.init_pair(1,curses.COLOR_CYAN,curses.COLOR_WHITE)
curses.init_pair(2,curses.COLOR_RED,curses.COLOR_WHITE)
size=win.getmaxyx()
b="And The Devil !!!!!"
x=[b[0:j] for j in range(1,len(b)+1)]
win.bkgd(curses.color_pair(1))
win.keypad(1)
win.nodelay(1)
win.border('|','|','*','*','(',')','(',')')
win.getch()
for i in x:
	win.addstr(size[0]-24,size[1]/2+5,"              .-----.",curses.color_pair(2))
	win.addstr(size[0]-23,size[1]/2+5,"            ,' -   - `.",curses.color_pair(2))
	win.addstr(size[0]-22,size[1]/2+5,"    _ _____/  <q> <p>  \_____ _",curses.color_pair(2))
	win.addstr(size[0]-21,size[1]/2+5,"   /_||   ||`-._____.-`||   ||-\ ",curses.color_pair(2))
	win.addstr(size[0]-20,size[1]/2+5,"  / _||===||           ||===|| _\ ",curses.color_pair(2))
	win.addstr(size[0]-19,size[1]/2+5," |- _||===||===========||===||- _|",curses.color_pair(2))
	win.addstr(size[0]-18,size[1]/2+5," \___||___||___________||___||___/",curses.color_pair(2))
	win.addstr(size[0]-17,size[1]/2+5,"  \\\|///   \_:_:_:_:_:_/   \\\\\\|//",curses.color_pair(2))
	win.addstr(size[0]-16,size[1]/2+5,"  |   _|    |_________|    |   _|",curses.color_pair(2))
	win.addstr(size[0]-15,size[1]/2+5,"  |   _|   /( ======= )\   |   _|",curses.color_pair(2))
	win.addstr(size[0]-14,size[1]/2+5,"  \\\||//  /\ `-.___.-' /\  \\\||//",curses.color_pair(2))
	win.addstr(size[0]-13,size[1]/2+5,"   (o )  /_ '._______.' _\  ( o)",curses.color_pair(2))
	win.addstr(size[0]-12,size[1]/2+5,"  /__/ \ |    _|   |_   _| / \__\ ",curses.color_pair(2))
	win.addstr(size[0]-11,size[1]/2+5,"  ///\_/ |_   _|   |    _| \_/\\\\\\ ",curses.color_pair(2))
	win.addstr(size[0]-10,size[1]/2+5," ///\\\_\ \    _/   \    _/ /_//\\\\\\ ",curses.color_pair(2))
	win.addstr(size[0]-9,size[1]/2+5," \\\|//_/ ///|\\\\\\   ///|\\\\\\ \_\\\|//",curses.color_pair(2))
	win.addstr(size[0]-8,size[1]/2+5,"         \\\\\\|///   \\\\\\|///",curses.color_pair(2))
	win.addstr(size[0]-7,size[1]/2+5,"         /-  _\\\   //   _\ ",curses.color_pair(2))
	win.addstr(size[0]-6,size[1]/2+5,"         |   _||   ||-  _|",curses.color_pair(2))
	win.addstr(size[0]-5,size[1]/2+5,"       ,/\____||   || ___/\,",curses.color_pair(2))
	win.addstr(size[0]-4,size[1]/2+5,"      /|\___`\,|   |,/'___/|\ ",curses.color_pair(2))
	win.addstr(size[0]-3,size[1]/2+5,"      |||`.\\\ \\\   // //,'|||",curses.color_pair(2))
	win.addstr(size[0]-2,size[1]/2+5,"      \\\\\\\\_//_//   \\\_\\\_////",curses.color_pair(2))
	curses.beep()
	win.addstr(5, size[1]/2-len(b)/2,i,curses.A_BLINK | curses.color_pair(2)|curses.A_UNDERLINE|curses.A_BOLD)
	curses.delay_output(80)
	win.refresh()
	win.clear()
	win.border('|','|','*','*','(',')','(',')')
curses.delay_output(800)
curses.endwin()