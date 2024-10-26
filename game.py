import pygame
pygame.init()
playing=True
screen=pygame.display.set_mode([500,500])
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load('rocket.png')
        self.image=pygame.transform.scale(pygame.image.load('rocket.png'),(80,100))
        self.rect=self.image.get_rect()
    def update(self,k):
        if k[pygame.K_UP]:
            self.rect.move_ip(0,-5)
        if k[pygame.K_DOWN]:
            self.rect.move_ip(0,10)
        if k[pygame.K_LEFT]:
            self.rect.move_ip(-5,0)
        if k[pygame.K_RIGHT]:
            self.rect.move_ip(10,0)
        if self.rect.left <0:
            self.rect.left=0
        if self.rect.right >500:
            self.rect.right=500
        if self.rect.top <0:
            self.rect.top=0
        if self.rect.bottom >500:
            self.rect.bottom=500

sprites=pygame.sprite.Group()
ship=Player()
sprites.add(ship)

while playing==True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            playing=False
    key=pygame.key.get_pressed()
    ship.update(key)
    screen.blit(pygame.image.load('background.png'),(0,0))
    sprites.draw(screen)
    pygame.display.update()




    
