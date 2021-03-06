import curses,curses.panel,curses.ascii
win=curses.initscr()
curses.curs_set(0)	
curses.start_color()
curses.init_pair(1,curses.COLOR_CYAN,curses.COLOR_WHITE)
curses.init_pair(2,curses.COLOR_RED,curses.COLOR_WHITE)
size=win.getmaxyx()
win.bkgd(curses.color_pair(1))
win.keypad(1)
win.nodelay(1)
win.border('|','|','*','*','(',')','(',')')
win.getch()
win.addstr(size[0]/2-5,25," .----------------.  .----------------.  .----------------.  .----------------. ",curses.color_pair(2))
win.addstr(size[0]/2-4,25,"| .--------------. || .--------------. || .--------------. || .--------------. |",curses.color_pair(2))
win.addstr(size[0]/2-3,25,"| |   ______     | || |     ____     | || | ____    ____ | || |   ______     | |",curses.color_pair(2))
win.addstr(size[0]/2-2,25,"| |  |_   _ \    | || |   .'    `.   | || ||_   \  /   _|| || |  |_   _ \    | |",curses.color_pair(2))
win.addstr(size[0]/2-1,25,"| |    | |_) |   | || |  /  .--.  \  | || |  |   \/   |  | || |    | |_) |   | |",curses.color_pair(2))
win.addstr(size[0]/2,25,"| |    |  __'.   | || |  | |    | |  | || |  | |\  /| |  | || |    |  __'.   | |",curses.color_pair(2))
win.addstr(size[0]/2+1,25,"| |   _| |__) |  | || |  \  `--'  /  | || | _| |_\/_| |_ | || |   _| |__) |  | |",curses.color_pair(2))
win.addstr(size[0]/2+2,25,"| |  |_______/   | || |   `.____.'   | || ||_____||_____|| || |  |_______/   | |",curses.color_pair(2))
win.addstr(size[0]/2+3,25,"| |              | || |              | || |              | || |              | |",curses.color_pair(2))
win.addstr(size[0]/2+4,25,"| '--------------' || '--------------' || '--------------' || '--------------' |",curses.color_pair(2))
win.addstr(size[0]/2+5,25," '----------------'  '----------------'  '----------------'  '----------------' ",curses.color_pair(2))
win.refresh()
win.clear()
win.border('|','|','*','*','(',')','(',')')
curses.delay_output(800)
curses.endwin()
