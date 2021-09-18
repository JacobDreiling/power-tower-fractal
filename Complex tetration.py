from math import hypot,exp,log,atan,sin,cos,pi,log1p
import canvas

width= 300
#canvas.begin_updates()
canvas.set_size(width,width)

x1,x2= -5,5
y1,y2= -5,5
maxiterations= 200

def color(n):
	c=lambda x:max(0,min(1,2-6*abs(x-1/2)))
	return c((x+1/3)%1),c(x%1),c((x-1/3)%1)
def angle(x,y):
	#return the principal angle of the number x+yi
	if y==0: return pi*(x<0)
	if x==0: return pi/2+pi*(y<0)
	correction= 2-abs(x*y)/(x*y)-abs(y)/y
	return atan(y/x)+correction*pi/2
def f(x,y,c_x,c_y):
	#the real part of the complex exponential (c_x+c_yi)^(x+yi)
	return exp(x*log(hypot(c_x,c_y))-y*angle(c_x,c_y))*cos(y*log(hypot(c_x,c_y))+x*angle(c_x,c_y))
def g(x,y,c_x,c_y):
	#the imaginary part of the complex exponential (c_x+c_yi)^(x+yi)
	return exp(x*log(hypot(c_x,c_y))-y*angle(c_x,c_y))*sin(y*log(hypot(c_x,c_y))+x*angle(c_x,c_y))

for x in range(width):
	for y in range(width):
		#convert canvas coordinates to complex plane coords
		x0,y0= x*(x2-x1)/width+x1, y*(y2-y1)/width+y1
		a,b= x0,y0
		n=0
		while n<maxiterations:
			try:a,b= f(a,b,x0,y0),g(a,b,x0,y0)
			#if the input to exp() is too large
			except: break
			n+=1
		
		if n==maxiterations:
			canvas.set_fill_color(0,0,0)
		else:
			lv= (n/maxiterations)**1
			canvas.set_fill_color(lv,0,1)
		canvas.fill_pixel(x,y)

canvas.end_updates()
#canvas.save_png('Fractal.png')
