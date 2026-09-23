import pygame
import sys
import random

clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 800))

color_white = (255, 255, 255)
color_grey1 = (60, 60, 60)
color_grey2 = (128, 128, 128)
color_grey3 = (180, 180, 180)


class ParticleTriesSmoke:
    def __init__(self):
        self.particles = []
        self.size = 8
        self.speed = 10

    def add_particle(self):
        pos_x = pygame.mouse.get_pos()[0]
        pos_y = pygame.mouse.get_pos()[1]
        radius = 8
        direction = -1
        duration = 5
        particles_circle = [[pos_x, pos_y], radius, self.size, direction, duration]
        self.particles.append(particles_circle)

    def draw_particle(self):
        if self.particles:
            for particle in self.particles:
                particle[0][0] += particle[3]
                particle[1] -= 0.06
                pygame.draw.circle(screen, color_white, (particle[0]), int(particle[1]))
                pygame.draw.circle(screen, color_grey1, (particle[0][0] + 3, particle[0][1] + 1), int(particle[1]))
                pygame.draw.circle(screen, color_grey3, (particle[0][0] - 2, particle[0][1] - 2), int(particle[1]))

    def remove(self):
        particle_copier = [particle for particle in self.particles if particle[1] > 0]
        self.particles = particle_copier


PARTICLE_EVENT = pygame.USEREVENT
pygame.time.set_timer(PARTICLE_EVENT, 20)

particle1 = ParticleTriesSmoke()

run = True
while run:
    screen.fill((30, 30, 30))
    clock.tick(144)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == PARTICLE_EVENT:
            particle1.add_particle()

    particle1.draw_particle()
    particle1.remove()
    pygame.display.update()


pygame.quit()
sys.exit()
