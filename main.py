#USE python 2.7.2+ and above
execfile("welcome.py")
execfile("to.py")
execfile("robo.py")
execfile("bomb.py")
execfile("defuser.py")
execfile("good_guy.py")
execfile("devil_guy.py")
execfile("story.py")
execfile("rules.py")
import curses,curses.panel,curses.ascii,random,time,sys
f=open("words.txt")
d=f.read().split()
codes=[]
for j in range(5,15,1):
	codes.append((random.sample([i for i in d if len(i) == j if len(set(i))==j],1)[0]).upper())
win=curses.initscr()
curses.curs_set(0)
curses.start_color()
win.clear()
curses.init_pair(1,curses.COLOR_CYAN,curses.COLOR_WHITE)
curses.init_pair(2,curses.COLOR_RED,curses.COLOR_WHITE)
curses.init_pair(3,curses.COLOR_BLACK,curses.COLOR_WHITE)
curses.init_pair(4,curses.COLOR_MAGENTA,curses.COLOR_WHITE)
size=win.getmaxyx()
win.bkgd(curses.color_pair(1))
win.keypad(1)
win.nodelay(1)
win.border('|','|','*','*','(',')','(',')')
win.getch()
class A:
 def initialize(self,level,timer):
	global t,rush,codes,c,d,b1,b2,key,y,x,i,max1,shape,penalty,hitted,allowed,prev,y1,x1,r,t1,by,bx
	t="Time Left :"
	rush="Now Rush For The Bomb!!!!"
	c=random.sample(range(4,size[0]-1),len(codes[level]))
	d=random.sample(range(4,size[1]-1),len(codes[level]))
	b1=random.sample(range(5,size[0]-3),1)[0]
	b2=random.sample(range(5,size[1]-5),1)[0]
	for i in range(len(codes[level])):
		win.addch(c[i],d[i],codes[level][i],curses.color_pair(3))
	key=1
	y=[1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,3]
	x=[1,2,3,4,5,6,1,2,3,4,5,6,1,2,3,4,5,6]
	i=max1=shape=penalty=hitted=0
	allowed=prev=timer
	t1=time.time()
	by=[b1,b1,b1,b1,b1+1,b1+1,b1+1,b1+1]
	bx=[b2,b2+1,b2+2,b2+3,b2,b2+1,b2+2,b2+3]
	win.addstr(b1,b2," ,-*",curses.color_pair(4)|curses.A_BOLD)
	win.addstr(b1+1,b2,"(_) ",curses.color_pair(4)|curses.A_BOLD)
	win.addstr(y[0],x[0],  " [00]/",curses.color_pair(2)|curses.A_BOLD)
	win.addstr(y[1*6],x[0],"/|**|",curses.color_pair(2)|curses.A_BOLD)
	win.addstr(y[2*6],x[0]," /_ /_",curses.color_pair(2)|curses.A_BOLD)
	y1=[size[0]-2,1]
	x1=[20,20]
	r=range(len(x))
	r.reverse()
 def key_w(self,x,y,check,level):
	global codes,size,i,penalty
	win.addch(y,x," ")
	y=y-1
	if i==len(codes[level]):
		return (y,x)
	z=win.inch(y,x)&255
	if chr(z) == codes[level][i]:
		i=i+1
		check=1
		if i==len(codes[level]):
			return (y,x)
	if chr(z) in codes[level] and chr(z) != codes[level][i] and check==0 and i>=1:
		i=i-1
		penalty=penalty+2
	return (y,x)
 def key_a(self,x,y,check,level):
	global codes,size,i,penalty
	win.addch(y,x," ")
	x=x-1
	if i==len(codes[level]):
		return (y,x)
	z=win.inch(y,x)&255
	if chr(z) == codes[level][i]:
		i=i+1
		check=1
		if i==len(codes[level]):
			return (y,x)
	if chr(z) in codes[level] and chr(z) !=codes[level][i] and check==0 and i>=1:
		i=i-1
		penalty=penalty+2
	return (y,x)
 def key_d(self,x,y,check,level):
	global codes,size,i,penalty
	win.addch(y,x," ")
	x=x+1
	if i==len(codes[level]):
		return (y,x)
	z=win.inch(y,x)&255
	if chr(z) == codes[level][i]:
		i=i+1
		check=1
		if i==len(codes[level]):
			return (y,x)
	if chr(z) in codes[level] and chr(z) != codes[level][i] and check==0 and i>=1:
		i=i-1
		penalty=penalty+2
	return (y,x)
 def key_s(self,x,y,check,level):
	global codes,size,i,penalty
	win.addch(y,x," ")
	y=y+1
	if i==len(codes[level]):
		return (y,x)
	z=win.inch(y,x)&255
	if chr(z) == codes[level][i]:
		i=i+1
		check=1
		if i==len(codes[level]):
			return (y,x)
	if chr(z) in codes[level] and chr(z) != codes[level][i] and check==0 and i>=1:
		i=i-1
		penalty=penalty+2
	return (y,x)
 def key_ss(self,x,y,check,asc):
	global codes,size,i,penalty
	win.addch(y,x," ")
	y=y+1
	return (y,x)
 def print_shape(self):
	global x,y,shape
	if shape==0:
		win.addstr(y[0],x[0],  " [00]/",curses.color_pair(2)|curses.A_BOLD)
		win.addstr(y[1*6],x[0],"/|*.| ",curses.color_pair(2)|curses.A_BOLD)
		win.addstr(y[2*6],x[0]," /_ /_",curses.color_pair(2)|curses.A_BOLD)
		shape=1
	else:
		win.addstr(y[0],x[0],  "\[oo] ",curses.color_pair(2)|curses.A_BOLD)
		win.addstr(y[1*6],x[0]," |.*|\\",curses.color_pair(2)|curses.A_BOLD)
		win.addstr(y[2*6],x[0],"_\ _\ ",curses.color_pair(2)|curses.A_BOLD)
		shape=0
 def check_bullet(self):
	global x,y,y1,x1,size
	added=0
	for j in range(len(y1)):
		if y1[j] < size[0]-2:
			(y1[j],x1[j])=obj.key_ss(x1[j],y1[j],check,win.inch(y1[j],x1[j])&255)
		else:
			win.addch(y1[j],x1[j]," ")
			y1.remove(y1[j])
			x1.remove(x1[j])
			break
		if y1[j] > random.sample(range(15),1)[0] and added==0 and(len(y1))<15:
			added=1
			bullets=range(5,size[1]-2,8)
			random.shuffle(bullets)
			for j in range(len(bullets)):
				if bullets[j] not in x and bullets[j] not in x1:
					y1.append(1)
					x1.append(bullets[j])
					break
 def check_bullet_hit(self):
	global x,y,x1,y1,size,done
	hit=[]
	done=0
	for j in range(len(x)):
		hit.append((x[j],y[j]))
	for j in range(len(x1)):
		if (x1[j],y1[j]) in hit:
			done=1
	return done
 def hint(self,level):
	global codes
	win.addstr(0,4,"Hint :",curses.color_pair(2)| curses.A_BLINK|curses.A_BOLD)
	for j in range(len(codes[level])):
		if j%2==0:
			win.addstr(0,10+j,codes[level][j],curses.color_pair(2)| curses.A_BLINK|curses.A_BOLD)
		else:
			win.addstr(0,10+j,"_",curses.color_pair(2)| curses.A_BLINK|curses.A_BOLD)
obj=A()
for level in range(10):
	obj.initialize(level,180+10*level)
	while key!=27:
		hitted=obj.check_bullet_hit()
		curses.curs_set(0)	
		t2=time.time()
		if allowed+t1-t2-penalty < 0:
			break
		if allowed+t1-t2-penalty < 100:
			win.addch(0,size[1]-2," ",curses.color_pair(2)|curses.A_BOLD)
		win.addstr(0,size[1]-len(t)-4,t+str(int(allowed-t2+t1-penalty)),curses.color_pair(2)| curses.A_BLINK|curses.A_BOLD)	
		check=done=0
		prev_key=key
		a=win.getch()
		if a!=-1:
			key=a
		obj.hint(level)
		win.timeout(75)
		if key==ord("P") or key == ord("p"):
			allowed=int(allowed-t2+t1-penalty)
			key=win.getch()
			while 1:
				execfile("paused.py")
				key=win.getch()
				if key==ord("P") or key == ord("p"):
					t1=time.time()
					win.clear()
					win.border('|','|','*','*','(',')','(',')')
					obj.print_shape()
					key=prev_key
					break
		if float(prev - (allowed+t1-t2-penalty)) > 0.20:
			obj.check_bullet()
			prev=float(allowed+t1-t2-penalty)
		for j in range(len(y1)):
			if y1[j] < size[0]-2:
				win.addch(y1[j],x1[j],curses.ACS_CKBOARD|curses.A_BOLD|curses.color_pair(3))
		if key==curses.KEY_LEFT and x[0]>1:
			for l in range(len(x)):
				(y[l],x[l])=obj.key_a(x[l],y[l],check,level)
			obj.print_shape()
			hitted=obj.check_bullet_hit()
		elif key==curses.KEY_DOWN and y[len(x)-1]+1 < size[0]-1:
			for l in r:
				(y[l],x[l])=obj.key_s(x[l],y[l],check,level)
			obj.print_shape()
			hitted=obj.check_bullet_hit()
		elif key==curses.KEY_UP and y[0]>1:
			for l in range(len(x)):
				(y[l],x[l])=obj.key_w(x[l],y[l],check,level)
			obj.print_shape()
			hitted=obj.check_bullet_hit()
		elif key==curses.KEY_RIGHT and x[len(x)-1]+1 < size[1]-1:
			for l in r:
				(y[l],x[l])=obj.key_d(x[l],y[l],check,level)
			obj.print_shape()
			hitted=obj.check_bullet_hit()
		win.addstr(size[0]-1,size[1]/2-len(codes[level]),codes[level][0:i],curses.color_pair(2)| curses.A_BLINK|curses.A_BOLD)
		max1=max(max1,i)
		for j in range(i,max1):
			win.addch(size[0]-1,size[1]/2-len(codes[level])+j,"*",curses.color_pair(2)| curses.A_BLINK|curses.A_BOLD)
		for j in range(i,len(codes[level])):
			win.addch(c[j],d[j],codes[level][j],curses.color_pair(3)|curses.A_BOLD)
		for j in range(len(x)):
			if y[j] in by and x[j] in bx  and i == len(codes[level]):
				done=1
		if i==len(codes[level]):
			win.addstr(size[0]-1,size[1]-len(rush)-3,rush,curses.color_pair(2)|curses.A_BOLD|curses.A_UNDERLINE)
		win.addstr(b1,b2," ,-*",curses.color_pair(4)|curses.A_BOLD)
		win.addstr(b1+1,b2,"(_) ",curses.color_pair(4)|curses.A_BOLD)
		if done==1:
			break
		if hitted==1:
			break
	win.clear()
	win.refresh()
	win.border('|','|','*','*','(',')','(',')')
	if done==1 and hitted==0:
		execfile("thumbs_up.py")
	if done==1 and hitted==0 and level!=9:
		execfile("try_next_level.py")
	if hitted==1:
		execfile("game_over.py")
		curses.endwin()
		sys.exit()
		break
	if key==27:
		break
if hitted==0 and done==1:
	execfile("defeat.py")
curses.delay_output(800)
curses.endwin()
