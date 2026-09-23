import pygame
from random import randint


class Particle(pygame.sprite.Sprite):
    def __init__(self,
                 groups: pygame.sprite.Group,
                 pos: list[int],
                 color: str,
                 direction: pygame.math.Vector2,
                 speed: int):
        super().__init__(groups)
        self.pos = pos
        self.color = color
        self.direction = direction
        self.speed = speed
        self.alpha = 255
        self.fade_speed = 200
        self.size = 4

        self.create_surface()

    def create_surface(self):
        self.image = pygame.Surface((self.size, self.size)).convert_alpha()
        self.image.set_colorkey("black")
        pygame.draw.circle(surface=self.image, color=self.color, center=(self.size/2, self.size/2), radius=self.size/2)
        self.rect = self.image.get_rect(center=self.pos)

    def move(self, dt):
        self.pos += self.direction * self.speed * dt
        self.rect.center = self.pos

    def fade(self, dt):
        self.alpha -= self.fade_speed * dt
        self.image.set_alpha(self.alpha)

    def check_pose(self, screen_width, screen_height):
        if (self.pos[0] < -50 or
            self.pos[0] > screen_width + 50 or
            self.pos[1] < -50 or
            self.pos[1] > screen_height + 50
           ):
            self.kill()

    def check_alpha(self):
        if self.alpha <= 0:
            self.kill()

    def update(self, dt, screen_width, screen_height):
        self.move(dt)
        self.fade(dt)
        self.check_pose(screen_width, screen_height)
        self.check_alpha()



class ExlpodingParticle(Particle):
    def __init__(self,
                 groups: pygame.sprite.Group,
                 pos: list[int],
                 color: str,
                 direction: pygame.math.Vector2,
                 speed: int,
                 explode_range: int
                 ):
        super().__init__(groups, pos, color, direction, speed)
        self.t0 = pygame.time.get_ticks()
        self.explode_range = explode_range
        self.lifetime = randint(self.explode_range - 100, self.explode_range)
        self.exploding = False
        self.size = 4
        self.max_size = 50
        self.inflate_speed = 500
        self.fade_speed = 5000

    def explosion_timer(self):
        if not self.exploding:
            t = pygame.time.get_ticks()
            if t - self.t0 > self.lifetime:
                self.exploding = True

    def inflate(self, dt):
        self.size += self.inflate_speed * dt
        self.create_surface()

    def size_check(self):
        if self.size > self.max_size:
            self.kill()

    def update(self, dt, screen_width, screen_height):
        self.move(dt)
        self.explosion_timer()
        if self.exploding:
            self.inflate(dt)
            self.fade(dt)

        self.check_pose(screen_width, screen_height)
        self.size_check()
        self.check_alpha()


class FloatingParticle(Particle):
    def __init__(self,
                 groups: pygame.sprite.Group,
                 pos: list[int],
                 color: str,
                 direction: pygame.math.Vector2,
                 speed: int
                 ):
        super().__init__(groups, pos, color, direction, speed)


color_white = (255, 255, 255)
color_grey1 = (60, 60, 60)
color_grey2 = (128, 128, 128)
color_grey3 = (180, 180, 180)


class ParticleTriesSmoke:
    def __init__(self):
        self.particles = []
        self.size = 8
        self.speed = 10

    def add_particle(self, pos_x, pos_y, char_size):
        # pos_x = pygame.mouse.get_pos()[0]
        # pos_y = pygame.mouse.get_pos()[1]
        radius = 8 - char_size
        direction = -1
        duration = 5
        particles_circle = [[pos_x, pos_y], radius, self.size, direction, duration]
        self.particles.append(particles_circle)

    def draw_particle(self, surface):
        if self.particles:
            for particle in self.particles:
                particle[0][0] += particle[3]
                particle[1] -= 0.06
                pygame.draw.circle(surface, color_white, (particle[0]), int(particle[1]))
                pygame.draw.circle(surface, color_grey1, (particle[0][0] + 3, particle[0][1] + 1), int(particle[1]))
                pygame.draw.circle(surface, color_grey3, (particle[0][0] - 2, particle[0][1] - 2), int(particle[1]))

    def remove(self):
        particle_copier = [particle for particle in self.particles if particle[1] > 0]
        self.particles = particle_copier

    def instant_remove(self):
        self.particles = []



