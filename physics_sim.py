import pygame

bgcolor = (255,255,255)
screen = pygame.display.set_mode((1000, 1000))
screen.fill(bgcolor)

pygame.draw.circle(screen, (0,0,0), (500, 500), 15, 15)
pygame.display.flip()
pygame.display.set_caption('testing12')

location = (200,200)
my_ball = Ball(location,30)
my_ball.display()

class Ball:
	def __init__(sef, location, size):
		self.location = location
		self.size = size
		self.color = (0,0,0)
		self.thickness = self.size

	def display(self):
		pygame.draw.circle(screen,self.color,self.location,self.size, self.thickness)
		

running = True

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
 	   running = False
