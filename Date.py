from datetime import*
from tkinter import*
root = Tk()
F = Frame(root)
F.pack(side = BOTTOM)
d = 1
def st():
 	global counter,x,y,d

 	if d==1:
 		l1['text'] = "Stopwatch Going to Start Press one More time"
 		d+=1
 	elif d==2:
 		y = datetime.fromtimestamp(counter)
 		x = y.strftime("%H:%M:%S")	    
 		l1['text']=x
 		l1.after(1000,st) 
 		counter += 1
def stop():
	global d
	d = 0
	return d
def reset():
	global counter,d
	if counter != 66600:
		counter = 66600
		d = 1
		y = datetime.fromtimestamp(counter)
		x = y.strftime("%H:%M:%S")
		l1['text'] = x
		return counter,d
counter = 66600
y = datetime.fromtimestamp(counter)
x = y.strftime("%H:%M:%S")
l1 = Label(root , text = x)
l1.pack()
Start = Button(F , text = "Start" , command = st)
Reset = Button(F , text = "Reset" , command = reset)
Stop = Button(F , text = "Stop ", command = stop)
Start.pack(side = LEFT)
Reset.pack(side = LEFT)
Stop.pack(side = RIGHT)
root.mainloop()