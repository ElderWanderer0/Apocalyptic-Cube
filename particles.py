import pygame
import sys
from random import choice, randint, uniform
from particles2 import Particle, ExlpodingParticle


screen_width = 1000
screen_height = 1000

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

particle_group = pygame.sprite.Group()
floating_particle_timer = pygame.event.custom_type()
pygame.time.set_timer(floating_particle_timer, 10)




def spawn_particle(n: int):
    for _ in range(n):
        pos = pygame.mouse.get_pos()
        color = choice(("red", "green", "blue"))
        direction = pygame.math.Vector2(uniform(-1, 1), uniform(-1, 1))
        direction = direction.normalize()
        speed = randint(50, 400)
        Particle(particle_group, pos, color, direction, speed)


def spawn_exploding_particle(n: int):
    for _ in range(n):
        pos = pygame.mouse.get_pos()
        color = choice(("red", "yellow", "orange"))
        direction = pygame.math.Vector2(uniform(-0.2, 0.2), uniform(0, -1))
        direction = direction.normalize()
        speed = randint(50, 400)
        ExlpodingParticle(particle_group, pos, color, direction, speed)


def spawn_floating_particle():
    init_pos = pygame.mouse.get_pos()
    pos = init_pos[0] + randint(-10, 10), init_pos[1] + randint(-10, 10)
    color = "white"
    direction = pygame.math.Vector2(0, -1)
    direction = direction.normalize()
    speed = randint(50, 100)
    Particle(particle_group, pos, color, direction, speed)

def main():
    particles = []
    run = True
    while run:
        screen.fill("black")
        posX = pygame.mouse.get_pos()[0]
        posY = pygame.mouse.get_pos()[1]
        particles.append([[posX, posY], [randint(0, 20) / 10 - 1, -2], randint(4, 6)])
        for particle in particles:
            particle[0][0] += particle[1][0]
            particle[0][1] += particle[1][1]
            particle[2] -= 0.1
            particle[1][1] += 0.03
            pygame.draw.circle(screen, (255, 255, 255), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
            if particle[2] <= 0:
                particles.remove(particle)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    spawn_particle(1000)
                if pygame.mouse.get_pressed()[2]:
                    spawn_exploding_particle(1000)
            if event.type == floating_particle_timer:
                spawn_floating_particle()


        # clock
        dt = clock.tick() / 1000
        """düşük ve yüksek seviye bilgisayarda güzel çalışabilmesi için dt var"""

        # display

        particle_group.draw(screen)

        # update
        particle_group.update(dt, screen_width, screen_height)
        print(len(particle_group.sprites())) #ne kadar partikül var görmek için
        pygame.display.update()


if __name__ == "__main__":
    pygame.init()
    main()
