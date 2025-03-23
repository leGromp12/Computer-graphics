import turtle

ws = turtle.Screen()
geekyTurtle = turtle.Turtle()

def miniStar():
	
	for i in range(5):
		geekyTurtle.right(144)
		geekyTurtle.forward(100)


for i in range(5):
		geekyTurtle.forward(300)
		geekyTurtle.right(-144)
		
		miniStar()
		
turtle.done()