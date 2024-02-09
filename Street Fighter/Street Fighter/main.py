import pygame
import sys

pygame.init()

clock = pygame.time.Clock()
fps = 60

# window

screen = pygame.display.set_mode((960, 560))
pygame.display.set_caption('Street Fighter')

bg_img = pygame.image.load('SF/stage.jpg').convert_alpha()


# Fighter class

class Fighter1:

    def __init__(self, x, y, name):

        self.x = x
        self.y = y
        self.name = name
        self.animation_list = []
        self.frame = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()
        self.move_right = False
        self.move_left = False

        # Idle animation
        temp_list = []
        for i in range(4):
            img = pygame.image.load(f'SF/{self.name}/idle/{i}.png')
            img = pygame.transform.scale(img, (img.get_width() * 4, img.get_height() * 4))
            temp_list.append(img)

        self.animation_list.append(temp_list)

        # Light punch animation
        temp_list = []
        for i in range(3):
            img = pygame.image.load(f'SF/{self.name}/lpunch/{i}.png')
            img = pygame.transform.scale(img, (img.get_width() * 4, img.get_height() * 4))
            temp_list.append(img)

        self.animation_list.append(temp_list)

        # Medium punch animation
        temp_list = []
        for i in range(5):
            img = pygame.image.load(f'SF/{self.name}/mpunch/{i}.png')
            img = pygame.transform.scale(img, (img.get_width() * 4, img.get_height() * 4))
            temp_list.append(img)

        self.animation_list.append(temp_list)

        # Light kick animation
        temp_list = []
        for i in range(3):
            img = pygame.image.load(f'SF/{self.name}/lkick/{i}.png')
            img = pygame.transform.scale(img, (img.get_width() * 4, img.get_height() * 4))
            temp_list.append(img)

        self.animation_list.append(temp_list)

        # Heavy kick animation
        temp_list = []
        for i in range(5):
            img = pygame.image.load(f'SF/{self.name}/hkick/{i}.png')
            img = pygame.transform.scale(img, (img.get_width() * 4, img.get_height() * 4))
            temp_list.append(img)

        self.animation_list.append(temp_list)

        # Walk animation
        temp_list = []
        for i in range(5):
            img = pygame.image.load(f'SF/{self.name}/walk/{i}.png')
            img = pygame.transform.scale(img, (img.get_width() * 4, img.get_height() * 4))
            temp_list.append(img)

        self.animation_list.append(temp_list)

    ##########################################################################################################

        self.image = self.animation_list[self.action][self.frame]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    # Movements

    # idle function
    def idle(self):
        self.frame = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()

    # Light punch function
    def light_punch(self):
        self.frame = 0
        self.action = 1
        self.update_time = pygame.time.get_ticks()

    # Medium punch function
    def medium_punch(self):
        self.frame = 0
        self.action = 2
        self.update_time = pygame.time.get_ticks()

    # Light kick function
    def light_kick(self):
        self.frame = 0
        self.action = 3
        self.update_time = pygame.time.get_ticks()

    # Heavy kick function
    def heavy_kick(self):
        self.frame = 0
        self.action = 4
        self.update_time = pygame.time.get_ticks()

    # Walk function
    def walk_ani(self):
        self.frame = 0
        self.action = 5
        self.update_time = pygame.time.get_ticks()

    # update image

    def update(self):
        animation_time = 100
        self.image = self.animation_list[self.action][self.frame]

        if pygame.time.get_ticks() - self.update_time > animation_time:
            self.update_time = pygame.time.get_ticks()
            self.frame += 1
        if self.frame >= len(self.animation_list[self.action]):
            self.frame = 0
            self.action = 0
            self.update_time = pygame.time.get_ticks()
        if self.move_right and self.rect.x <= 620:
            self.rect.x += 3
        if self.move_left and self.rect.x > 50:
            self.rect.x -= 3

    def draw(self):
        screen.blit(self.image, self.rect)

    def check_events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.light_punch()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.medium_punch()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    self.light_kick()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.heavy_kick()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.move_left = True
                    self.walk_ani()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.move_right = True
                    self.walk_ani()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.move_left = False

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.move_right = False

            if event.type == pygame.KEYDOWN:
                if self.rect.x > 580 and event.key == pygame.K_q:
                    ken.hurt()
                if self.rect.x > 580 and event.key == pygame.K_w:
                    ken.hurt()
                if self.rect.x > 580 and event.key == pygame.K_e:
                    ken.hurt()
                if self.rect.x > 580 and event.key == pygame.K_r:
                    ken.hurt()

###################################################################################################################


class Fighter2:

    def __init__(self, x, y, name):

        self.name = name
        self.animation_list = []
        self.frame = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()

        # Idle animation
        t_list = []
        for i in range(4):
            img = pygame.image.load(f'SF/{self.name}/idle/{i}.png')
            img = pygame.transform.scale(img, (img.get_width() * 4, img.get_height() * 4))
            t_list.append(img)

        self.animation_list.append(t_list)

        # Hurt animation
        t_list = []
        for i in range(5):
            img = pygame.image.load(f'SF/{self.name}/hurt/{i}.png')
            img = pygame.transform.scale(img, (img.get_width() * 4, img.get_height() * 4))
            t_list.append(img)

        self.animation_list.append(t_list)

    ###############################################################

        self.image = self.animation_list[self.action][self.frame]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    # Movements

    # idle function
    def idle(self):
        self.frame = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()

    # hurt function
    def hurt(self):
        self.frame = 0
        self.action = 1
        self.update_time = pygame.time.get_ticks()

    # update image

    def update(self):
        animation_time = 100
        self.image = self.animation_list[self.action][self.frame]

        if pygame.time.get_ticks() - self.update_time > animation_time:
            self.update_time = pygame.time.get_ticks()
            self.frame += 1
        if self.frame >= len(self.animation_list[self.action]):
            self.frame = 0
            self.action = 0
            self.update_time = pygame.time.get_ticks()

    def draw(self):
        screen.blit(self.image, self.rect)

###################################################################################################################


j = 800
k = 370
w = 200
h = 370
ryu = Fighter1(w, h, 'ryu')
ken = Fighter2(j, k, 'ken')

# main game loop


while True:

    clock.tick(fps)
    ryu.check_events()
    screen.blit(bg_img, (-170, -160))
    ryu.update()
    ken.update()
    ken.draw()
    ryu.draw()

    pygame.display.update()