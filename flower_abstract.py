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
	if n != nmax:
		t.fd(r*2)
		heading = t.heading()
	for i in range(int(n)):
		if i % 2 == 0:
			t.fillcolor("blue")
		else:
			t.fillcolor("green")
		petal(t, r, n, angle)
		t.lt(360.0 / n)
		t.lt(180-angle)
	if n != nmax:
		t.setheading(heading)
		t.bk(r*2)




def petal(t, r, n, angle):
	if n == 6:
		t.fillcolor("purple")
	elif n == 5:
		t.fillcolor("indigo")
	elif n == 4:
		t.fillcolor("navy")
	elif n == 3:
		t.fillcolor("sea green")
	elif n == 2:
		t.fillcolor("goldenrod")
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
	if r >= 5:
		flower(t, r / 3, n - 1, angle)

	arc(t, r, angle)



root = Tk()
root.withdraw()
bob = turtle.Turtle()
canvas = turtle.getcanvas()
screen_width = 1200
screen_height = 1200
bob.screen.setup(screen_width, screen_height, 0, 0)
bob.screen.setworldcoordinates(0, -screen_height, screen_width, 0)
# bob.hideturtle()
bob.speed(0)
bob.up()
bob.goto(screen_width / 2, -7*screen_height / 8)
bob.down()
# n=11, rmin=50, r/2, n-1
nmax = 5
flower(bob, 200, nmax, 75)

turtle.mainloop()
