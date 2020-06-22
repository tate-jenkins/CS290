import turtle
from tkinter import *
import time
from PIL import ImageGrab, Image
import random


def get_pixel(widget, x, y):
	ImageGrab.grab().crop((x, y, x + 1, y + 1)).save("C:\\Users\\Tate\\Desktop\\image.png")


def get_pixel_color(pixel):
	im = Image.open("C:\\Users\\Tate\\Desktop\\image.png")
	pix = im.load()
	rgb = pix[0, 0]
	print(rgb)
	if sum(list(rgb)) < 128:
		return "black"
	elif rgb == (255, 255, 255):
		return "white"
	elif rgb == (255, 0, 0):
		return "red"
	elif rgb == (0, 0, 255):
		return "blue"
	elif rgb == (0, 128, 0):
		return "white"


def square(t, length):
	for i in range(4):
		t.fd(length)
		t.lt(90)


def polyline(t, length, n, angle):
	for i in range(int(n)):
		t.fd(length)
		"""
		x = t.xcor() + 43
		y = -t.ycor() + 77
		color = get_pixel_color(get_pixel(canvas, x, y))
		if color == "red":
			t.rt(angle)
			t.fillcolor("green")
		elif color == "green":
			t.lt(angle)
			t.fillcolor("blue")
		elif color == "blue":
			t.rt(angle)
			t.fillcolor("red")
		elif color == "black":
			t.fd(10)
			flower(t, random.randint(100,200), 5, 30)
		"""
		t.lt(angle)


def polygon(t, length, n):
	angle = 360.0 / n
	polyline(t, length, n, angle)


def circle(t, r, n):
	c = 2 * 3.1415926 * r
	polygon(t, c / n, n)


def arc(t, r, angle):
	arc_length = 2 * 3.141526 * r * abs(angle) / 360
	n = int(arc_length / 4) + 3
	step_length = arc_length / n
	step_angle = float(angle) / n

	t.lt(step_angle / 2)
	polyline(t, step_length, n, step_angle)
	t.rt(step_angle / 2)


def flower(t, r, n, angle):
	choose_color(t,r, "green")
	color = list(t.fillcolor())
	new_color=[]
	for rgb in color:
		new_rgb = int(rgb)
		new_color.append(new_rgb)
	if r != r0:

		t.rt(angle/2)
	if r == r0:
		t.pensize(r / 20 + 2)
		t.pencolor("saddle brown")
		t.fd(r*random.uniform(1, 1.5))
		branch(t, r, angle)
		t.pensize(r / 20 + 2)
		t.pencolor("saddle brown")
		t.fd(r*random.uniform(1,1.5))

	branch(t,r/2,angle)

	t.pensize(r / 20 + 2)
	t.pencolor("saddle brown")






	for index in range(random.choice([0,1])):

		t.fd(r*random.uniform(1, 1.5))
		branch(t,r/2,angle)

	t.pensize(r / 20 + 2)
	t.pencolor("saddle brown")
	t.fd(r*random.uniform(1, 1.5))
	if r == r0:
		t.fd(r * random.uniform(1, 2))
	t.pensize(0)
	t.pencolor("black")

	f_heading = t.heading()

	for i in range(int(n)):
		t.fillcolor(new_color)
		petal(t, r, n, angle, True)
		t.lt(360.0 / n)
		t.lt(180-angle*random.uniform(0.5,1.5))
	if r != 120:
		t.setheading(f_heading)
		t.lt(angle/2)
	if r > 40 and random.choice([0,1,2,3,4]) > 0:
		flower2(t,r/2,n+3,angle)
	elif r != 120:
		temp_angle = random.uniform(-30,30)
		t.rt(temp_angle)
		branch(t,r/2,angle)
		t.lt(temp_angle)

def flower2(t, r, n, angle):
	choose_color(t,r, "pink")
	color = list(t.fillcolor())
	new_color=[]
	for rgb in color:
		new_rgb = int(rgb)
		new_color.append(new_rgb)
	f_heading = t.heading()

	for i in range(int(n)):
		t.fillcolor(new_color)
		petal(t, r, n, angle, False)
		t.lt(360.0 / n)
		t.lt(180-angle*random.uniform(0.75,1.25))
	if r != 120:
		t.setheading(f_heading)
		t.lt(angle/2)
	t.setheading(f_heading)
	choose_color(t,r, "yellow")
	color = list(t.fillcolor())
	new_color=[]
	for rgb in color:
		new_rgb = int(rgb)
		new_color.append(new_rgb)

	t.dot(r/3, new_color)


def choose_color(t, r, theme):
	turtle.colormode(255)
	if theme == "green":
		red = int(255*random.uniform(0.25,0.5))
		green = int(255*random.uniform(0.5,1))
		blue = int(255*random.uniform(0,0.25))
	elif theme == "pink":
		red = int(255*random.uniform(0.75,1))
		green = int(255*random.uniform(0,0.25))
		blue = int(255*random.uniform(0.5,0.75))
	elif theme == "yellow":
		red = int(255*random.uniform(0.75,1))
		green = int(255*random.uniform(0.75,1))
		blue = int(255*random.uniform(0,0.25))
	t.fillcolor((red,green,blue))
	"""
	if r == 120:
		t.fillcolor("forest green")
	elif r < 8:
		t.fillcolor("purple")
	elif r < 11:
		t.fillcolor("medium orchid")
	elif r < 16:
		t.fillcolor("pale violet red")
	elif r < 25:
		t.fillcolor("firebrick")
	elif r < 35:
		t.fillcolor("orange red")
	elif r < 50:
		t.fillcolor("dark orange")
	elif r < 80:
		t.fillcolor("gold")
	elif r < 120:
		t.fillcolor("yellow green")
	"""

def petal(t, r, n, angle, leaf):
	t.pensize(0)
	t.pencolor("black")
	if r > 20:
		t.begin_fill()
		arc(t, r, angle)
		heading = t.heading()
		x = t.xcor()
		y = t.ycor()
		t.lt(180 - angle)
		arc(t, r, angle)
		t.end_fill()
		t.up()
		t.goto(x,y)
		t.down()
		t.setheading(heading)
		if r >= 40 and leaf == True:
			branch(t, r*3/8*random.uniform(0.75,1.25), angle)
			flower(t, r*3/8*random.uniform(0.75,1.25), random.choice([1,2,3,4,5]), angle*random.uniform(0.75,1.25))
		t.up()
		t.goto(x,y)
		t.lt(180-angle)
		arc(t,r,angle)
		t.down()
	else:
		branch(t, r, angle)

def branch(t, length, a):

	t.pensize(length / 20 + 2)
	t.pencolor("saddle brown")
	if length > 40 and length != r0:
		position = t.position()
		heading = t.heading()
		if random.choice([0, 1]) == 1:
			t.rt(random.uniform(40,50))
		else:
			t.lt(random.uniform(40,50))

		t.fd(length)


		if random.choice([0, 1, 2, 3]) > 0:
			branch(t, length / 2, a)

		flower(t,length, random.choice([1,2,3,4,5]), a)

		t.up()
		t.setposition(position)
		t.setheading(heading)
		t.down()


	else:

		position = t.position()
		heading = t.heading()
		if random.choice([0, 1]) == 1:
			t.rt(random.uniform(30,60))
		else:
			t.lt(random.uniform(30,60))

		t.fd(length)


		if random.choice([0, 1, 2, 3]) > 0 and length > 10:
			branch(t, length / 2, a)

		t.up()
		t.setposition(position)
		t.setheading(heading)
		t.down()

	t.pensize(length / 20 + 2)
	t.pencolor("saddle brown")

root = Tk()
root.withdraw()
bob = turtle.Turtle()
canvas = turtle.getcanvas()
screen_width = 2500
screen_height = 2500
bob.screen.setup(screen_width, screen_height, 0, 0)
bob.screen.setworldcoordinates(0, -screen_height, screen_width, 0)
bob.hideturtle()
bob.speed(0)
bob.up()
bob.goto(screen_width / 2, -screen_height / 2)
bob.down()
# n=11, rmin=50, r/2, n-1
n0 = 5
r0 = 120
bob.lt(90)
flower(bob, r0, n0, 75)

turtle.mainloop()
