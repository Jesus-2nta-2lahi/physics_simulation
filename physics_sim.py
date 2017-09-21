import pygame, math, random

bgcolor = (255, 255, 255)
window_height = 1000
window_width = 1000

screen = pygame.display.set_mode((window_width, window_height))
screen.fill(bgcolor)
pygame.display.set_caption('testing123')
pygame.display.flip()

class Particle:
	def __init__(self, location, size,speed,angle):
		self.x = location[0]
		self.y = location[1]
		self.size = size
		self.color = (255, 100, 0)
		self.thickness = 2

		self.speed = speed
		self.angle = angle

	def display(self):
		pygame.draw.circle(screen, self.color,(int(self.x),int(self.y)), self.size, self.thickness)

	def move(self):
		self.x += math.sin(self.angle) * self.speed
		self.y += math.cos(self.angle) * self.speed

	def bounce(self):
		if self.x > window_width - self.size:
			self.x = 2*(window_width - self.size) - self.x
			self.angle = - self.angle
		elif self.x < self.size:
			self.x = 2*self.size - self.x
			self.angle = - self.angle
		if self.y > window_height - self.size:
			self.y = 2*(window_height - self.size) - self.y
			self.angle = math.pi - self.angle
		elif self.y < self.size:
			self.y = 2*self.size - self.y
			self.angle = math.pi - self.angle

my_particles = []
num_of_particles = 15

for n in range(num_of_particles):
	size = random.randint(5,30)
	location = (random.randint(size,window_width - size),random.randint(size,window_height - size))
	my_particles.append(Particle(location,size,random.random(),random.uniform(0,math.pi/2)))

running = True

while running:
	screen.fill(bgcolor)
	for i in my_particles:
		i.move()
		i.bounce()
		i.display()

	pygame.display.flip()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False