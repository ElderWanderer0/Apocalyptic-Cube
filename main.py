import pygame
from pygame.locals import *
import sys
import random
from GameParticles import Particle, ExlpodingParticle, ParticleTriesSmoke

pygame.init()

particle_group = pygame.sprite.Group()
floating_particle_timer = pygame.event.custom_type()
pygame.time.set_timer(floating_particle_timer, 10)

# Colors--------------------------------------------------------------------------------------------------------------//
color_ice = (225, 240, 235)
color_white = (255, 255, 255)
color_black = (0, 0, 0)
color_grey1 = (60, 60, 60)
color_grey2 = (128, 128, 128)
color_grey3 = (180, 180, 180)
color_yellow = (200, 200, 0)
color_mud = (112, 84, 62)
color_meteor = (212, 103, 18)
color_brown = (150, 75, 0)
# Screen settings-----------------------------------------------------------------------------------------------------//
screen_width = 1800
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))
# Caption-------------------------------------------------------------------------------------------------------------//
pygame.display.set_caption("Apocalyptic Cube")


# text drawing--------------------------------------------------------------------------------------------------------//
def draw_text(text, font, size, x, y, color):
    text_font = pygame.font.SysFont(font, size)
    deftext = text_font.render(text, 1, color)
    screen.blit(deftext, (x, y))


# Character function--------------------------------------------------------------------------------------------------//
def draw_rect(color, x, y, width, height):
    itself = pygame.draw.rect(screen, color, pygame.Rect(x, y, width, height))
    return itself


def draw_column1(color, x, y, width, height, color2, x2, y2, width2, height2):
    itself = pygame.draw.rect(screen, color, pygame.Rect(x, y, width, height))
    itself2 = pygame.draw.rect(screen, color2, pygame.Rect(x2, y2, width2, height2))
    return itself, itself2


# Meteor function-----------------------------------------------------------------------------------------------------//
def draw_circle(color, x, y, radius):
    itself = pygame.draw.circle(screen, color, [x, y], radius)
    return itself


def spawn_meteor(color, x, y, radius, x_lenght):
    itself = pygame.draw.circle(screen, color, [x, y], radius)
    pygame.draw.circle(screen, color_brown, [x, y], radius, 4)
    init_pos = [x, y]
    pos = [init_pos[0] + random.randint(-10, x_lenght), init_pos[1] + random.randint(-10, 10)]
    color = random.choice(("yellow", "orange", "grey"))
    direction = pygame.math.Vector2(0, -1)
    direction = direction.normalize()
    speed = random.randint(50, 100)
    Particle(particle_group, pos, color, direction, speed)
    return itself


"""color, x, y, radius"""

# effects-------------------------------------------------------------------------------------------------------------//
particles = []


def floating_cloud_effect(color_effect, x, y):
    """posX = pygame.mouse.get_pos()[0]
    posY = pygame.mouse.get_pos()[1]"""
    particles.append([[x, y], [random.randint(0, 20) / 10 - 1, -2], random.randint(4, 6)])
    for particle in particles:
        particle[0][0] += particle[1][0]
        particle[0][1] += particle[1][1]
        particle[2] -= 0.1
        particle[1][1] += 0.03
        pygame.draw.circle(screen, color_effect, [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
        if particle[2] <= 0:
            particles.remove(particle)


def spawn_floating_particle(x, y):
    init_pos = [x, y]
    pos = [init_pos[0] + random.randint(-10, 10), init_pos[1] + random.randint(-10, 10)]
    color = "white"
    direction = pygame.math.Vector2(0, -1)
    direction = direction.normalize()
    speed = random.randint(50, 100)
    Particle(particle_group, pos, color, direction, speed)


def spawn_particle(n: int, x, y, color_tuple, particle_range):
    for _ in range(n):
        pos = [x, y]
        color = random.choice(color_tuple)
        direction = pygame.math.Vector2(random.uniform(-1, 1), random.uniform(-1, 1))
        direction = direction.normalize()
        speed = random.randint(50, particle_range)
        Particle(particle_group, pos, color, direction, speed)


def spawn_exploding_particle(x, y, explode_range):
    for _ in range(100):
        pos = [x, y]
        color = random.choice(("yellow", "orange", "grey", color_brown))
        direction = pygame.math.Vector2(random.uniform(-0.2, 0.2), random.uniform(0, -1))
        direction = direction.normalize()
        speed = random.randint(50, 400)
        ExlpodingParticle(particle_group, pos, color, direction, speed, explode_range)


PARTICLE_EVENT = pygame.USEREVENT
pygame.time.set_timer(PARTICLE_EVENT, 20)
particle_smoke = ParticleTriesSmoke()
# Character characteristic--------------------------------------------------------------------------------------------//
char_x = 200
char_y = 700
char_width = 100
char_height = 100
char_Jspeed = 30
char_speed = 5

# Column characteristic-----------------------------------------------------------------------------------------------//
col_xF = 2000
col_x = col_xF
col_y = random.randint(600, 750)
col_speed = 10
col_width = random.randint(200, 800)
col_widthF = 0
col_height = 50
col_x2 = 2000
col_y2 = random.randint(300, 450)
col_width2 = random.randint(200, 800)
col_width2F = 0

vertical_column_height = 200
vertical_column_width = 50
vertical_column_x = col_xF + col_width
vertical_column_x2 = col_xF + col_width2

col_x5 = col_xF
col_y5 = random.randint(600, 750)
col_width5 = random.randint(200, 800)
col_x6 = col_xF
col_y6 = random.randint(300, 450)
col_width6 = random.randint(200, 800)
col_x7 = col_xF
col_y7 = random.randint(600, 750)
col_width7 = random.randint(200, 800)
col_x8 = col_xF
col_y8 = random.randint(300, 450)
col_width8 = random.randint(200, 800)

col_x3 = col_x5 + col_width5
col_x4 = col_x8 + col_width8


# Columns-------------------------------------------------------------------------------------------------------------//
column = draw_rect(color_yellow, col_x, col_y, col_width, col_height)
column2 = draw_rect(color_yellow, col_x2, col_y2, col_width2, col_height)
column3 = draw_rect(color_yellow, col_x3, col_y5 - vertical_column_height + 50, vertical_column_width,
                    vertical_column_height)
column4 = draw_rect(color_yellow, col_x4, col_y8, vertical_column_width, vertical_column_height)
column5 = draw_rect(color_yellow, col_x5, col_y5, col_width5, col_height)
column6 = draw_rect(color_yellow, col_x6, col_y6, col_width6, col_height)
column7 = draw_rect(color_yellow, col_x7, col_y7, col_width7, col_height)
column8 = draw_rect(color_yellow, col_x8, col_y8, col_width8, col_height)

# Spikes_Characteristics----------------------------------------------------------------------------------------------//
sp1_x = -600
sp1_y1 = 400
sp1_y2 = 500
sp1_x2 = 0
sp1_y3 = (sp1_y2 + sp1_y1) / 2
sp1_width = sp1_x2 - sp1_x
sp1_height = sp1_y2 - sp1_y1

sp2_x = -600
sp2_y1 = 50
sp2_y2 = 150
sp2_x2 = 0
sp2_y3 = (sp2_y2 + sp2_y1) / 2
sp2_width = sp2_x2 - sp2_x
sp2_height = sp2_y2 - sp2_y1

sp1_y2_n = 0
sp1_y1_n = 0
sp1_y3_n = 0

sp2_y2_n = 0
sp2_y1_n = 0
sp2_y3_n = 0

sp_y_speed = 0.5
spike_sting = False
spike_rollback = False

spike_sting2 = False
spike_rollback2 = False

sting_timer = random.randint(3, 6)


# Spikes--------------------------------------------------------------------------------------------------------------//
spike1 = pygame.draw.polygon(screen, color_grey2, [[sp1_x, sp1_y1], [sp1_x, sp1_y2], [sp1_x2, sp1_y3]])
spike2 = pygame.draw.polygon(screen, color_grey2, [[sp2_x, sp2_y1], [sp2_x, sp2_y2], [sp2_x2, sp2_y3]])

# Spike creation------------------------------------------------------------------------------------------------------//
spike_chance = 2

# Character-----------------------------------------------------------------------------------------------------------//
character = draw_rect(color_ice, char_x, char_y, char_width, char_height)

floor = draw_rect(color_mud, -500, 800, 2500, 500)

Vertical_column1 = False
Vertical_column2 = False

# Meteors-------------------------------------------------------------------------------------------------------------//
meteor_speedList = [2, 2.2, 2.3, 2.5]
meteor_velocityList = [2, 2.8, 3.4, 4]

m1_x = random.randint(300, 1700)
m2_x = random.randint(300, 1700)
m3_x = random.randint(300, 1700)
m1_y = random.randint(-100, 0)
m2_y = random.randint(-100, 0)
m3_y = random.randint(-100, 0)
m1_r = random.randint(15, 25)
m2_r = random.randint(15, 25)
m3_r = random.randint(15, 25)
m1_s = random.choice(meteor_speedList)
m2_s = random.choice(meteor_speedList)
m3_s = random.choice(meteor_speedList)
m1_v = random.choice(meteor_velocityList)
m2_v = random.choice(meteor_velocityList)
m3_v = random.choice(meteor_velocityList)
const_value = 10
m1_expRan = m1_r * const_value
m2_expRan = m2_r * const_value
m3_expRan = m3_r * const_value

m1 = spawn_meteor(color_meteor, m1_x, m1_y, m1_r, m1_r)
m2 = spawn_meteor(color_meteor, m2_x, m2_y, m2_r, m2_r)
m3 = spawn_meteor(color_meteor, m3_x, m3_y, m3_r, m3_r)

# score---------------------------------------------------------------------------------------------------------------//
time_listScore = []
time = pygame.time.get_ticks()//1000
time_listScore.append(time)
score = 0
per_seconds = 2

time_listSpk = [time]
time_listSpk2 = [time]
# column_creation-----------------------------------------------------------------------------------------------------//
column_creator = True
probability = [0, 1, 2]
chance = random.choice(probability)

finished1_c = False
finished2_c = False
finished1_c1 = False
finished2_c1 = False
finished3_c1 = False
finished1_c2 = False
finished2_c2 = False
finished3_c2 = False


# Gadgets-------------------------------------------------------------------------------------------------------------//
class Gadgets:
    @staticmethod
    def resize(x, y):
        border_circle = pygame.draw.circle(screen, color_white, (x, y), 50, 1)
        # inner_circle
        draw_circle(color_grey3, x, y, 45)
        # inner_shape
        draw_rect(color_ice, x - 20, y - 20, 40, 40)

        return border_circle

    @staticmethod
    def moon_jump(x, y):
        border_circle = pygame.draw.circle(screen, color_white, (x, y), 50, 1)
        # inner_circle
        draw_circle(color_grey3, x, y, 45)
        # inner_shape
        pygame.draw.circle(screen, (150, 150, 150), (x, y), 30)
        pygame.draw.circle(screen, (130, 130, 130), (x - 15, y - 5), 3)
        pygame.draw.circle(screen, (130, 130, 130), (x - 9, y + 10), 7)
        pygame.draw.circle(screen, (130, 130, 130), (x + 7, y - 10), 10)
        pygame.draw.circle(screen, (130, 130, 130), (x + 13, y + 11), 5)

        return border_circle

    @staticmethod
    def barrier(x, y):
        border_circle = pygame.draw.circle(screen, color_white, (x, y), 50, 1)
        # inner_circle
        draw_circle(color_grey3, x, y, 45)
        # inner shape
        draw_circle((255, 255, 200), x, y, 30)
        pygame.draw.circle(screen, (255, 200, 0), (x, y), 30, 3)
        draw_circle((255, 255, 240), x + 9, y - 3, 6)
        draw_circle((255, 255, 240), x + 10, y - 4, 6)
        draw_circle((255, 255, 240), x + 9, y - 5, 6)
        draw_circle((255, 255, 240), x + 10, y - 5, 6)

        return border_circle

    @staticmethod
    def dash_reloader(x, y):
        border_circle = pygame.draw.circle(screen, color_white, (x, y), 50, 1)
        # inner_circle
        draw_circle(color_grey3, x, y, 45)
        # inner shape
        draw_circle(color_grey2, x, y, 40)
        draw_rect((145, 160, 155), x-26, y, 20, 20)
        draw_rect((165, 180, 175), x - 17, y, 20, 20)
        draw_rect((185, 200, 195), x - 8, y, 20, 20)
        draw_rect(color_ice, x+1, y, 20, 20)

        return border_circle

    @staticmethod
    def the_world(x, y):
        border_circle = pygame.draw.circle(screen, color_white, (x, y), 50, 1)
        # inner_circle
        draw_circle(color_grey3, x, y, 45)
        # inner shape
        draw_rect(color_ice, x-10, y-10, 20, 20)
        pygame.draw.circle(screen, color_grey1, (x, y), 20, 1)
        pygame.draw.circle(screen, color_grey2, (x, y), 28, 1)
        pygame.draw.circle(screen, (220, 220, 220), (x, y), 35, 1)

        return border_circle

    @staticmethod
    def galactic_explosion(x, y):
        border_circle = pygame.draw.circle(screen, color_white, (x, y), 50, 1)
        # inner_circle
        draw_circle(color_grey3, x, y, 45)
        # inner shape
        pygame.draw.circle(screen, (255, 185, 185), (x, y), 35)
        pygame.draw.circle(screen, (255, 127, 127), (x, y), 25)
        pygame.draw.circle(screen, (255, 85, 85), (x, y), 15)
        pygame.draw.circle(screen, (255, 70, 70), (x, y), 15, 1)
        pygame.draw.circle(screen, (255, 110, 110), (x, y), 25, 1)
        pygame.draw.circle(screen, (255, 165, 165), (x, y), 35, 1)
        draw_rect(color_ice, x - 10, y - 10, 20, 20)

        return border_circle


counter_for_galacticExplosion = 0
galacticExplosion_count = 3
galacticExplosion_chance = random.randint(1, 3)
reGalacticExp = False
galacticExplosion_get = False
galacticExplosion = False
galacticExp_timelist = [time]
counter_for_theWorld = 0
theWorld_count = 1
theWorld_chance = random.randint(1, 3)
reTheWorld = False
theWorld_get = False
theWorld = False
theWorld_timeList = [time]
counter_for_dashReload = 0
dashes = 3
dashReload_chance = random.randint(1, 3)
reDashLoader = False
counter_for_barrier = 0
barrier_dt = 0
barrier_time = 10
barrier_chance = random.randint(1, 3)
reBarrier = False
counter_for_moonJump = 0
jumpCounter_moonJump = 0
moonJump_chance = random.randint(1, 3)
reMoonJump = False
counter_for_resize = 0
resize_chance = random.randint(1, 3)
reResize = False
# Game settings-------------------------------------------------------------------------------------------------------//
jump = False
can_jump = True
dash = False
reset = False
jump_Total = []
run = True
moon_jump = False
barrier = False
gravity = 6
# FPS settings--------------------------------------------------------------------------------------------------------//
prev_time = pygame.time.get_ticks()/1000
fps = 144
clock = pygame.time.Clock()

while run:

    dx = 0
    dy = 0
    char_vel = 0
    # display---------------------------------------------------------------------------------------------------------//
    screen.fill(color_grey2)
    particle_group.draw(screen)

    # Score-----------------------------------------------------------------------------------------------------------//
    time = pygame.time.get_ticks() // 1000

    if time_listScore[0] + per_seconds == time:
        time_listScore = [time]
        if theWorld:
            if theWorld_timeList[0] + 5 <= time:
                theWorld = False
        if theWorld is False:
            score += 1
    if 999 > score > 99:
        draw_text(f"Score : {score}", "arial", 60, 1540, 10, color_white)
    if score > 999:
        draw_text(f"Score : {score}", "arial", 60, 1500, 10, color_white)
    if score <= 99:
        draw_text(f"Score : {score}", "arial", 60, 1570, 10, color_white)

    draw_text(f"time : {time}", "arial", 60, 800, 20, color_white)
    # FPS-------------------------------------------------------------------------------------------------------------//
    clock.tick(fps)
    now = pygame.time.get_ticks() / 1000
    dt = now - prev_time
    prev_time = now

    draw_text(f"FPS : {round(clock.get_fps())}", "arial", 60, 10, 10, color_white)
    # Events----------------------------------------------------------------------------------------------------------//
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == PARTICLE_EVENT:
            particle_smoke.add_particle(char_x + char_width, char_y + char_height, char_width/50)
        if event.type == pygame.KEYDOWN:
            if event.key == K_r:
                reset = True
            if can_jump:
                if event.key == K_SPACE or event.key == K_w:
                    jump_Total.append(char_Jspeed)
                    jump = True
                    if moon_jump:
                        jumpCounter_moonJump += 1
            if event.key == pygame.K_l:
                if dashes != 0:
                    dashes -= 1
                    dash = True
            if event.key == pygame.K_j:
                if theWorld_count == 1:
                    theWorld_count -= 1
                    theWorld_get = True
            if event.key == pygame.K_k:
                if galacticExplosion_count > 0:
                    galacticExplosion_count -= 1
                    galacticExplosion = True
        if event.type == pygame.KEYUP:
            pass
    keys = pygame.key.get_pressed()

    # Floor-----------------------------------------------------------------------------------------------------------//
    floor = draw_rect(color_mud, -1000, 800, 5000, 500)

    # Entitys---------------------------------------------------------------------------------------------------------//

    # Character
    character = draw_rect(color_ice, char_x, char_y, char_width, char_height)

    # Columns
    if chance == 0:
        column = draw_rect(color_yellow, col_x, col_y, col_width, col_height)
        column2 = draw_rect(color_yellow, col_x2, col_y2, col_width2, col_height)

    elif chance == 1:
        column5 = draw_rect(color_yellow, col_x5, col_y5, col_width5, col_height)
        column6 = draw_rect(color_yellow, col_x6, col_y6, col_width6, col_height)
        column3 = draw_rect(color_yellow, col_x3, col_y5 - vertical_column_height + 50,
                            vertical_column_width, vertical_column_height)

    elif chance == 2:
        column7 = draw_rect(color_yellow, col_x7, col_y7, col_width7, col_height)
        column8 = draw_rect(color_yellow, col_x8, col_y8, col_width8, col_height)
        column4 = draw_rect(color_yellow, col_x4, col_y8, vertical_column_width, vertical_column_height)

    columns = [column, column2, column3, column4, column5, column6, column7, column8]
    columns_coordinate_x = [col_x, col_x2, col_x3, col_x4, col_x5, col_x6, col_x7, col_x8]

    # Spikes

    if score > 1:
        sp1_y2_n = col_y + col_height
        sp1_y1_n = sp1_y2 - sp1_height
        sp1_y3_n = (sp1_y2 + sp1_y1) / 2
        if sp1_x2 < 50:
            sp1_x2 += 0.75

        spike1 = pygame.draw.polygon(screen, color_grey1, [[sp1_x, sp1_y1], [sp1_x, sp1_y2], [sp1_x2, sp1_y3]])
        if spike_chance == 1 and spike_sting is False:
            if time_listSpk[0] + 4 >= time:
                if theWorld:
                    if theWorld_timeList[0] + 5 <= time:
                        theWorld = False
                if theWorld is False:
                    if sp1_y1 < sp1_y1_n:
                        sp1_y1 += sp_y_speed
                    if sp1_y1 > sp1_y1_n:
                        sp1_y1 -= sp_y_speed
                    if sp1_y2 < sp1_y2_n:
                        sp1_y2 += sp_y_speed
                    if sp1_y2 > sp1_y2_n:
                        sp1_y2 -= sp_y_speed
                    if sp1_y3 < sp1_y3_n:
                        sp1_y3 += sp_y_speed
                    if sp1_y3 > sp1_y3_n:
                        sp1_y3 -= sp_y_speed
            else:
                spike_sting = True
                time_listSpk = [time]
        else:
            if sp1_x2 == 50:
                if theWorld:
                    if theWorld_timeList[0] + 5 <= time:
                        theWorld = False
                if theWorld is False:
                    sp1_x2 -= 0.75
            spike_chance = random.choice(range(1, 200))

        if spike_sting and not spike_rollback:
            if theWorld:
                if theWorld_timeList[0] + 5 <= time:
                    theWorld = False
            if theWorld is False:
                sp1_x2 += 11
                sp1_x += 11

        if sp1_x2 > sp1_width:
            spike_rollback = True
            spike_sting = False

        if spike_rollback:
            if theWorld:
                if theWorld_timeList[0] + 5 <= time:
                    theWorld = False
            if theWorld is False:
                sp1_x2 -= 3
                sp1_x -= 3
            if sp1_x2 < 0:
                spike_rollback = False

        sp2_y2_n = col_y2 + col_height
        sp2_y1_n = sp2_y2 - sp2_height
        sp2_y3_n = (sp2_y2 + sp2_y2) / 2
        if sp2_x2 < 50:
            if theWorld:
                if theWorld_timeList[0] + 5 <= time:
                    theWorld = False
            if theWorld is False:
                sp2_x2 += 0.75

        spike2 = pygame.draw.polygon(screen, color_grey1, [[sp2_x, sp2_y1], [sp2_x, sp2_y2], [sp2_x2, sp2_y3]])
        if spike_chance == 1 and spike_sting2 is False:
            if time_listSpk2[0] + sting_timer >= time:
                if theWorld:
                    if theWorld_timeList[0] + 5 <= time:
                        theWorld = False
                if theWorld is False:
                    if sp2_y1 < sp2_y1_n:
                        sp2_y1 += sp_y_speed
                    if sp2_y1 > sp2_y1_n:
                        sp2_y1 -= sp_y_speed
                    if sp2_y2 < sp2_y2_n:
                        sp2_y2 += sp_y_speed
                    if sp2_y2 > sp2_y2_n:
                        sp2_y2 -= sp_y_speed
                    if sp2_y3 < sp2_y3_n:
                        sp2_y3 += sp_y_speed
                    if sp2_y3 > sp2_y3_n:
                        sp2_y3 -= sp_y_speed
            else:
                spike_sting2 = True
                time_listSpk2 = [time]
        else:
            if sp2_x2 == 50:
                if theWorld:
                    if theWorld_timeList[0] + 5 <= time:
                        theWorld = False
                if theWorld is False:
                    sp2_x2 -= 0.75
            spike_chance = random.choice(range(1, 200))

        if spike_sting2 and not spike_rollback2:
            if theWorld:
                if theWorld_timeList[0] + 5 <= time:
                    theWorld = False
            if theWorld is False:
                sp2_x2 += 11
                sp2_x += 11

        if sp2_x2 > sp2_width:
            spike_rollback2 = True
            spike_sting2 = False

        if spike_rollback2:
            if theWorld:
                if theWorld_timeList[0] + 5 <= time:
                    theWorld = False
            if theWorld is False:
                sp2_x2 -= 3
                sp2_x -= 3
            if sp2_x2 < 0:
                sting_timer = random.randint(3, 7)
                spike_rollback2 = False

        # draw_text(f"spkC = {spike1_chance}", "arial", 60, 100, 600, color_white)
        # draw_text(f"spkS = {spike_sting}", "arial", 60, 100, 800, color_white)
        # draw_text(f"spkR = {spike_rollback}", "arial", 60, 100, 400, color_white)
        # draw_text(f"spkT = {time_listSpk[0]}", "arial", 60, 100, 200, color_white()

    # Gadget settings-------------------------------------------------------------------------------------------------//
    if score >= 0:
        # Gadget timer---------//

        # Resize-----------------------------------//
        if chance == 0 and counter_for_resize > resize_chance:
            Resizer = Gadgets.resize(col_x + col_width/2, col_y - 70)
            if character.colliderect(Resizer):
                if char_vel >= 0:
                    dy -= 100
                char_height = 100
                char_width = 100
                char_Jspeed = 30

                resize_chance = 0
                counter_for_resize = 0
                reResize = True
            if col_x < -col_width:
                resize_chance = 0
                counter_for_resize = 0
                reResize = True
        if reResize:
            resize_chance = random.randint(5, 10)
            reResize = False
        # Moon Jump-------------------------------------//
        if chance == 1 and counter_for_moonJump > moonJump_chance:
            Moon_jump = Gadgets.moon_jump(col_x5 + col_width5/2, col_y5 - 70)
            if character.colliderect(Moon_jump):
                spawn_particle(100, col_x5 + col_width5 / 2, col_y5 - 70, (color_white, color_ice, color_grey1),
                               100)
                moon_jump = True
                moonJump_chance = 0
                counter_for_moonJump = 0
                reMoonJump = True
            if col_x3 < -vertical_column_width:
                moonJump_chance = 0
                counter_for_moonJump = 0
                reMoonJump = True
        if reMoonJump:
            moonJump_chance = random.randint(5, 10)
            reMoonJump = False
        # Barrier---------------------------------------//
        if chance == 2 and counter_for_barrier > barrier_chance:
            Barrier = Gadgets.barrier(col_x7 + col_width7 / 2, col_y7 - 70)
            if character.colliderect(Barrier):
                spawn_particle(100, col_x7 + col_width7 / 2, col_y7 - 70, (color_white, color_ice, color_grey1),
                               100)
                barrier_dt = 0

                barrier = True
                counter_for_barrier = 0
                barrier_chance = 0
                reBarrier = True
            if col_x4 < - vertical_column_width:
                counter_for_barrier = 0
                barrier_chance = 0
                reBarrier = True
        if reBarrier:
            barrier_chance = random.randint(5, 10)
            reBarrier = False

        # Dash_Reloader----------------------------------//
        if chance == 0 and counter_for_dashReload > dashReload_chance:
            dashReload = Gadgets.dash_reloader((col_x + col_width / 2) + 150, col_y - 70)
            if character.colliderect(dashReload):
                spawn_particle(100, col_x2 + col_width2 / 2, col_y2, (color_white, color_ice, color_grey1),
                               100)
                dashes = 3

                counter_for_dashReload = 0
                dashReload_chance = random.randint(5, 10)
                reDashLoader = True
            if col_x2 < -col_width:
                counter_for_dashReload = 0
                dashReload_chance = random.randint(5, 10)
                reDashLoader = True
        if reDashLoader:
            dashReload_chance = random.randint(5, 10)
            reDashLoader = False

        # The World----------------------------------------//
        if chance == 1 and counter_for_theWorld > theWorld_chance:
            theWorld_gadget = Gadgets.the_world(col_x6 + col_width6 / 2, col_y6 - 70)
            if character.colliderect(theWorld_gadget):
                spawn_particle(100, col_x6 + col_width6 / 2, col_y6, (color_white, color_ice, color_grey1),
                               100)
                theWorld_count = 1

                counter_for_theWorld = 0
                theWorld_chance = random.randint(5, 10)
                reTheWorld = True
            if col_x6 < -col_width6:
                counter_for_theWorld = 0
                theWorld_chance = random.randint(5, 10)
                reTheWorld = True
        if reTheWorld:
            theWorld_chance = random.randint(5, 10)
            reTheWorld = False

        # Galactic Explosion-------------------------------//
        if chance == 2 and counter_for_galacticExplosion > galacticExplosion_chance:
            galacticExplosion_gadget = Gadgets.galactic_explosion(col_x8 + col_width8 / 2, col_y8 - 70)
            if character.colliderect(galacticExplosion_gadget):
                spawn_particle(100, col_x8 + col_width8 / 2, col_y8, (color_white, color_ice, color_grey1),
                               100)
                if galacticExplosion_count < 2:
                    galacticExplosion_count += 1

                counter_for_galacticExplosion = 0
                galacticExplosion_chance = random.randint(5, 10)
                reGalacticExp = True
            if col_x8 < -col_width8:
                counter_for_galacticExplosion = 0
                theWorld_chance = random.randint(5, 10)
                reGalacticExp = True
        if reGalacticExp:
            galacticExplosion_chance = random.randint(5, 10)
            reGalacticExp = False
    # Meteors--------------------------------------------//

    m1 = spawn_meteor(color_meteor, m1_x, m1_y, m1_r, m1_r)
    m2 = spawn_meteor(color_meteor, m2_x, m2_y, m2_r, m2_r)
    m3 = spawn_meteor(color_meteor, m3_x, m3_y, m3_r, m3_r)
    meteorList = [m1, m2, m3]

    # Barrier---------------------------------------------------------------------------------------------------------//
    if barrier:
        barrier_countdown = int(barrier_time - barrier_dt)
        draw_text(f"Barrier:{barrier_countdown}", "Arial", 30, 10, 850, color_white)
        barrier_dt += 1 * dt

        pygame.draw.circle(screen, (254, 254, 227), (char_x+(char_height/2), char_y+(char_height/2)), char_height-10)
        border = pygame.draw.circle(screen, (255, 255, 200), (char_x + (char_height / 2), char_y + (char_height / 2)),
                                    char_height-10, 10)

        barrier_surface = pygame.Surface((char_width, char_height))
        barrier_surface.fill(color_ice)
        barrier_surface.set_alpha(250)
        screen.blit(barrier_surface, (char_x, char_y))

        if barrier_dt > barrier_time:
            barrier = False
        for meteor in meteorList:
            if border.colliderect(meteor):
                barrier = False
        if border.colliderect(spike1) or border.colliderect(spike2):
            barrier = False

    # Char smalling animation-----------------------------------------------------------------------------------------//
    char_width -= 0.01
    char_height -= 0.01
    char_Jspeed -= 0.001
    # Meteors spawn---------------------------------------------------------------------------------------------------//

    if m1_x < -20:
        m1_x = random.randint(300, 1700)
        m1_y = random.randint(-100, 0)
        m1_r = random.randint(15, 25)
        m1_s = random.choice(meteor_speedList)
        m1_v = random.choice(meteor_velocityList)
    if m2_x < -20:
        m2_x = random.randint(300, 1700)
        m2_y = random.randint(-100, 0)
        m2_r = random.randint(15, 25)
        m2_s = random.choice(meteor_speedList)
        m2_v = random.choice(meteor_velocityList)
    if m3_x < -20:
        m3_x = random.randint(300, 1700)
        m3_y = random.randint(-100, 0)
        m3_r = random.randint(15, 25)
        m3_s = random.choice(meteor_speedList)
        m3_v = random.choice(meteor_velocityList)

    # Columns movement------------------------------------------------------------------------------------------------//

    if chance == 0:
        if theWorld:
            if theWorld_timeList[0] + 5 <= time:
                theWorld = False
        if theWorld is False:
            col_x -= col_speed
            col_x2 -= col_speed
        if col_x <= -col_width:
            finished1_c = True

        if col_x2 <= -col_width2:
            finished2_c = True

        if finished1_c and finished2_c:
            chance = random.choice(probability)
            col_x = 2000
            col_y = random.randint(600, 750)
            col_width = random.randint(200, 800)
            col_x2 = 2000
            col_y2 = random.randint(300, 450)
            col_width2 = random.randint(200, 800)
            finished1_c = False
            finished2_c = False
            counter_for_resize += 1
            counter_for_moonJump += 1
            counter_for_barrier += 1
            counter_for_dashReload += 1
            counter_for_theWorld += 1
            counter_for_galacticExplosion += 1

    if chance == 1:
        if theWorld:
            if theWorld_timeList[0] + 5 <= time:
                theWorld = False
        if theWorld is False:
            col_x3 -= col_speed
            col_x5 -= col_speed
            col_x6 -= col_speed
            vertical_column_x -= col_speed
        if vertical_column_x < -vertical_column_width:
            finished3_c1 = True
        if col_x5 <= -col_width5:
            finished1_c1 = True
        if col_x6 <= -col_width6:
            finished2_c1 = True
        if finished1_c1 and finished2_c1 and finished3_c1:
            chance = random.choice(probability)
            col_x5 = col_xF
            col_y5 = random.randint(600, 750)
            col_width5 = random.randint(200, 800)
            col_x6 = col_xF
            col_y6 = random.randint(300, 450)
            col_width6 = random.randint(200, 800)
            vertical_column_x = col_xF + col_width6
            col_x3 = col_x5 + col_width5
            finished1_c1 = False
            finished2_c1 = False
            finished3_c1 = False
            counter_for_resize += 1
            counter_for_moonJump += 1
            counter_for_barrier += 1
            counter_for_dashReload += 1
            counter_for_theWorld += 1
            counter_for_galacticExplosion += 1
    if chance == 2:
        if theWorld:
            if theWorld_timeList[0] + 5 <= time:
                theWorld = False
        if theWorld is False:
            col_x4 -= col_speed
            col_x7 -= col_speed
            col_x8 -= col_speed
            vertical_column_x2 -= col_speed
        if vertical_column_x2 < -vertical_column_width:
            finished3_c2 = True
        if col_x7 <= -col_width7:
            finished1_c2 = True
        if col_x8 <= -col_width8:
            finished2_c2 = True
        if finished1_c2 and finished2_c2 and finished3_c2:
            chance = random.choice(probability)
            col_x7 = col_xF
            col_y7 = random.randint(600, 750)
            col_width7 = random.randint(200, 800)
            col_x8 = col_xF
            col_y8 = random.randint(300, 450)
            col_width8 = random.randint(200, 800)
            vertical_column_x2 = col_xF + col_width8
            col_x4 = col_x8 + col_width8
            finished1_c2 = False
            finished2_c2 = False
            finished3_c2 = False
            counter_for_resize += 1
            counter_for_moonJump += 1
            counter_for_barrier += 1
            counter_for_dashReload += 1
            counter_for_theWorld += 1
            counter_for_galacticExplosion += 1
    # Character's movement--------------------------------------------------------------------------------------------//
    if keys[K_d] or keys[K_RIGHT]:
        dx += char_speed
    if keys[K_a] or keys[K_LEFT]:
        dx -= char_speed

    if char_x > 1700:
        char_x = 1700
    elif char_x < -50:
        char_x = -50
    # meteors update--------------------------------------------------------------------------------------------------//
    if theWorld:
        if theWorld_timeList[0] + 5 <= time:
            theWorld = False
    if theWorld is False:
        m1_x -= m1_s + dx/10
        m1_y += m1_v

        m2_x -= m2_s + dx/10
        m2_y += m2_v

        m3_x -= m3_s + dx/10
        m3_y += m3_v

    # Reset(R)--------------------------------------------------------------------------------------------------------//
    if reset:
        char_x = 200
        char_y = 700
        reset = False
    # Jump is a singleshot event, it's key is on up-------------------------------------------------------------------//

    if jump:
        particle_smoke.instant_remove()
        char_vel -= char_Jspeed
        char_Jspeed -= 1
        if char_Jspeed <= -char_Jspeed:
            char_Jspeed = jump_Total[0]
            jump_Total = []
            jump = False

    # Dash (Key is on up)---------------------------------------------------------------------------------------------//
    draw_text(f"Dash:{dashes}", "Arial", 30, 10, 950, color_white)
    if dash and keys[K_a]:
        dx -= 200
        draw_rect((145, 160, 155), char_x + 100, char_y, char_width, char_height)
        draw_rect((165, 180, 175), char_x + 70, char_y, char_width, char_height)
        draw_rect((185, 200, 195), char_x + 40, char_y, char_width, char_height)
        draw_rect((205, 220, 215), char_x + 10, char_y, char_width, char_height)
        draw_rect(color_ice, char_x, char_y, char_width, char_height)
        dash = False
    if dash and keys[K_d]:
        dx += 200
        draw_rect((145, 160, 155), char_x - 100, char_y, char_width, char_height)
        draw_rect((165, 180, 175), char_x - 70, char_y, char_width, char_height)
        draw_rect((185, 200, 195), char_x - 40, char_y, char_width, char_height)
        draw_rect((205, 220, 215), char_x - 10, char_y, char_width, char_height)
        draw_rect(color_ice, char_x, char_y, char_width, char_height)
        dash = False

    # The world-------------------------------------------------------------------------------------------------------//
    if theWorld_get:
        theWorld_timeList = [time]
        theWorld = True
        theWorld_get = False
    draw_text(f"The world : {theWorld_count}", "Arial", 30, 10, 900, color_white)

    # Galactic Explosion----------------------------------------------------------------------------------------------//
    '''Columnlarda bug var bunarı düzeltelim'''
    if galacticExplosion:

        if chance == 0:
            col_x = col_xF
            col_x2 = col_xF
        if chance == 1:
            col_x3 = col_xF
            col_x5 = col_xF
            col_x6 = col_xF
        if chance == 2:
            col_x4 = col_xF
            col_x7 = col_xF
            col_x8 = col_xF
        chance = random.choice(probability)

        m1_x = random.randint(300, 1700)
        m1_y = random.randint(-100, 0)
        m1_r = random.randint(15, 25)
        m1_s = random.choice(meteor_speedList)
        m1_v = random.choice(meteor_velocityList)

        m2_x = random.randint(300, 1700)
        m2_y = random.randint(-100, 0)
        m2_r = random.randint(15, 25)
        m2_s = random.choice(meteor_speedList)
        m2_v = random.choice(meteor_velocityList)

        m3_x = random.randint(300, 1700)
        m3_y = random.randint(-100, 0)
        m3_r = random.randint(15, 25)
        m3_s = random.choice(meteor_speedList)
        m3_v = random.choice(meteor_velocityList)

        sp1_x = -600
        sp1_x2 = 0

        sp2_x = -600
        sp2_x2 = 0

        char_y = 700

        galacticExplosion = False
        galacticExplosion_get = False
    draw_text(f"Galactic Explosion : {galacticExplosion_count}", "Arial", 30, 10, 750, color_white)
    # Gravity---------------------------------------------------------------------------------------------------------//
    if character.colliderect(floor):
        # Friction effect---//
        particle_smoke.draw_particle(screen)
        particle_smoke.remove()
        character.bottom = floor.top
        gravity = 0
        can_jump = True
    else:
        can_jump = False
        if not moon_jump:
            gravity = 4
        if moon_jump and not jumpCounter_moonJump > 10:
            gravity = 2
        if jumpCounter_moonJump > 10:
            moon_jump = False
            jumpCounter_moonJump = 0
        char_vel += gravity
        if char_vel > 30:
            char_vel = 30
    dy += char_vel
    dy += gravity

    # Collusions------------------------------------------------------------------------------------------------------//

    for c in range(len(columns)):
        if columns[c].colliderect(character.x + dx, character.y, char_width, char_height):
            char_speed = 0
            char_x = columns_coordinate_x[c] - 100
        elif columns[c].colliderect(character.x, character.y + dy, char_width, char_height):
            # jumping
            if char_vel < 0:
                particle_smoke.instant_remove()
                dy = columns[c].bottom - character.top
                jump = False
                char_Jspeed = jump_Total[0]
                char_vel = 0
            # landing
            if char_vel > 0:
                # Friction effect---//
                particle_smoke.draw_particle(screen)
                particle_smoke.remove()
                dy = columns[c].top - character.bottom
                can_jump = True
        else:
            char_speed = 5

    # Meteors Collision---//
    entitiyList = [floor, character, column, column2, column3, column4, column5, column6, column7, column8]

    for i in range(len(entitiyList)):
        if meteorList[0].colliderect(entitiyList[i]):
            spawn_exploding_particle(m1_x, m1_y, m1_expRan)
            m1_x = random.randint(300, 1700)
            m1_y = random.randint(-100, 0)
            m1_r = random.randint(15, 25)
            m1_s = random.choice(meteor_speedList)
            m1_v = random.choice(meteor_velocityList)
            m1_expRan = m1_r * const_value
        if meteorList[1].colliderect(entitiyList[i]):
            spawn_exploding_particle(m2_x, m2_y, m2_expRan)
            m2_x = random.randint(300, 1700)
            m2_y = random.randint(-100, 0)
            m2_r = random.randint(15, 25)
            m2_s = random.choice(meteor_speedList)
            m2_v = random.choice(meteor_velocityList)
            m2_expRan = m2_r * const_value
        if meteorList[2].colliderect(entitiyList[i]):
            spawn_exploding_particle(m3_x, m3_y, m3_expRan)
            m3_x = random.randint(300, 1700)
            m3_y = random.randint(-100, 0)
            m3_r = random.randint(15, 25)
            m3_s = random.choice(meteor_speedList)
            m3_v = random.choice(meteor_velocityList)
            m3_expRan = m3_r * const_value

    # Spike collusions---//
    if spike1.colliderect(character) or spike2.colliderect(character):
        pass  # öldürme/can azaltma ekle

    # Coordinate updating---------------------------------------------------------------------------------------------//
    char_y += dy
    char_x += dx

    # Window update---------------------------------------------------------------------------------------------------//
    particle_group.update(dt, screen_width, screen_height)
    pygame.display.update()

pygame.quit()
sys.exit()
