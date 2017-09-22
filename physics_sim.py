import pygame, math, random

my_particles = []
num_of_particles = 15
bgcolor = (255, 255, 255)
window_height = 700
window_width = 1000
screen = pygame.display.set_mode((window_width, window_height))

gravity = (math.pi,-0.001)
drag = 0.999
elasticity = 0.75

def main():
    screen.fill(bgcolor)
    pygame.display.set_caption('testing123')
    pygame.display.flip()

    for n in range(num_of_particles):
        size = random.randint(5,30)
        location = (random.randint(size,window_width - size),random.randint(size,window_height - size))
        my_particles.append(Particle(location,size,random.random(),random.uniform(0,math.pi/2)))

    running = True
    selected_particle = None 

    while running:
        screen.fill(bgcolor)
        for i in my_particles:
            if i != selected_particle:
                i.move()
                i.bounce()
            if selected_particle:
                (mouseX, mouseY) = pygame.mouse.get_pos()
                # selected_particle.x = mouseX
                # selected_particle.y = mouseY
                dx = mouseX - selected_particle.x
                dy = mouseY - selected_particle.y
                selected_particle.angle = math.atan2(dy,dx) + 0.5 * math.pi
                selected_particle.speed = math.hypot(dx,dy) * 0.1
            i.display()

        pygame.display.flip()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                (mouseX, mouseY) = pygame.mouse.get_pos()
                selected_particle = findParticle(my_particles, mouseX, mouseY)
            elif event.type == pygame.MOUSEBUTTONUP:
                selected_particle = None

class Particle:
    def __init__(self, location, size,speed,angle):
        self.x = location[0]
        self.y = location[1]
        self.size = size
        self.color = (255, 0, 255)
        self.thickness = 2

        self.speed = speed
        self.angle = angle

    def display(self):
        pygame.draw.circle(screen, self.color,(int(self.x),int(self.y)), self.size, self.thickness)



    def move(self):
        self.x += math.sin(self.angle) * self.speed
        self.y += math.cos(self.angle) * self.speed
        (self.angle, self.speed) = self.addVectors((self.angle, self.speed), gravity)
        self.speed *= drag

    def bounce(self):
        if self.x > window_width - self.size:
            self.x = 2*(window_width - self.size) - self.x
            self.angle = - self.angle
            self.speed *= elasticity
        elif self.x < self.size:
            self.x = 2*self.size - self.x
            self.angle = - self.angle
            self.speed *= elasticity
        if self.y > window_height - self.size:
            self.y = 2*(window_height - self.size) - self.y
            self.angle = math.pi - self.angle
            self.speed *= elasticity
        elif self.y < self.size:
            self.y = 2*self.size - self.y
            self.angle = math.pi - self.angle
            self.speed *= elasticity

    def addVectors(self, vector1, vector2):
        x  = math.sin(vector1[0]) * vector1[1] + math.sin(vector2[0]) * vector2[1]
        y  = math.cos(vector1[0]) * vector1[1] + math.cos(vector2[0]) * vector2[1]
        length = math.hypot(x, y)
        angle = 0.5 * math.pi - math.atan2(y,x)
        return (angle,length)

def findParticle(particles, x, y):
    for p in particles:
        if math.hypot(p.x - x, p.y - y) <= p.size:
            return p
    return None

# def collide():





if __name__ == '__main__':
    main()