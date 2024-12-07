from pygame import *


window = display.set_mode((700, 500))
background = transform.scale(image.load("galaxy.jpg"), (700, 500))

mixer.init()
mixer.music.load('space.ogg')
mixer.music.set_volume(0.5)
mixer.music.play()

class GameSprite():
    def __init__(self, player_image, player_x, player_y, speed):
        self.image = transform.scale(image.load(player_image), (65 ,65))

        self.speed = speed 

        self.rect = self.image.get_rect()
        self.rect.x = player_x 
        self.rect.y = player_y


    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Rocket(GameSprite):
    def moce(self):

        keys = key.get_pressed()
        if keys[K_a] and self.rect.x < 0:
            self.rect.x -= self.speed

        if keys_pressed[k_d] and self.rect.x < 635:
            self.rect.y += self.speed


class UFO(GameSprite):
    def move(self):
        self.rect.x += self.speed 

        if self.rect.y > 435:
            self.rect.y = 0
            self.rect.x = radint(0, 635)
            self.speed = randint(6, 15)

rocket = Rocket("rocket.png")
enemy = Ufo("ufo.png", 65, 65 ,7)

monsters = sprite.Group()
for i in range(10):
    ufo = UFO("ufo.png", 200, 10, 6)
    monsters.add(ufo)


game = True
clock = time.clock()
FPS = 60
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.blit(background, (0, 0))

    rocket.draw()
    rocket.draw()

    monsters.draw(window)
    monster.update
    clock.tick(FPS)
    display.update()
