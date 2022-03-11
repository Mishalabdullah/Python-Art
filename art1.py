from tkinter import *
import colorsys
import turtle
import time
# turtle uses tk as its dependancy

s = turtle.Screen()
s.bgcolor('black')
turtle.speed(0)
n=200
h=0
for i in range (250):
	c = colorsys.hsv_to_rgb(h,1,0.9)
	h = h+1/n 
	turtle.pencolor(c)
	turtle.pensize(2)
	turtle.rt(165)
	turtle.fd(i*5)
	turtle.rt(265)
	turtle.fd(i*5)
	turtle.rt(165)
	turtle.fd(i*5)
	if i == 249:
	 time.sleep(10)
	
