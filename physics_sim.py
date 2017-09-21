import turtle as tt

def main():
	obj1 = tt.clone()
	obj1.color('red')
	obj1.shape('circle')
	obj1.showturtle()
	obj1.goto(100,0)

	obj2 = tt.clone()
	obj2.color('blue')
	obj2.shape('circle')
	obj2.showturtle()
	obj2.goto(-100,0)

if __name__ == '__main__':
	tt.hideturtle()
	tt.penup()
	tt.setup(1920,1080)
	main()
	tt.done()