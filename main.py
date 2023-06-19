import pygame

pygame.init()
win = pygame.display.set_mode((420, 720))
pygame.display.set_caption("Ninja")

player = pygame.image.load("image/player.png")
bg = pygame.image.load("image/bg.png")
platform = pygame.image.load("image/platform.png")

x = 50
y = 50
selfX = x
selfY = y
speed = 5
FPS = 60

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super.__init__()
        self.image = pygame.image.load('image/player.png')
        self.rect = self.image.get_rect()
        self.change_x = 0
        self.change_y = 0


        self.level = None

    def update(self):
        self.calc_gravity()
        self.rect.x += self.change_x


class Level(object):
    def __init__(self):
        self.platforms = pygame.sprite.Group()
        self.player = player

        self.background = None

    def update(self):
        screen.blit(bg, (0, 0))

        self.platforms.draw(s)

WHITE = (255, 255, 255)

clock = pygame.time.Clock()
run = True
while(run):
    clock.tick(FPS)
    win.blit(bg, (0, 0))
    win.blit(platform, (150, 570))
    win.blit(player, (x, y))
    font = pygame.font.Font(None, 20)

    text = font.render("Координаты: ", True, WHITE)
    text2 = font.render("X: ", True, WHITE)
    text3 = font.render(str(selfX), True, WHITE)
    text4 = font.render("Y: ", True, WHITE)
    text5 = font.render(str(selfY), True, WHITE)

    win.blit(text, [20, 20])
    win.blit(text2, [110, 20])
    win.blit(text3, [130, 20])
    win.blit(text4, [155, 20])
    win.blit(text5, [175, 20])
    pygame.display.update()



    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= speed
        selfX -= speed
    elif keys[pygame.K_RIGHT]:
        x += speed
        selfX += speed
    elif keys[pygame.K_UP]:
        y -= speed
        selfY -= speed
    elif keys[pygame.K_DOWN]:
        y += speed
        selfY += speed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()