import pygame


class Player(pygame.sprite.Sprite):

  def __init__(self):
    super().__init__()
    self.image = pygame.image.load("resources/voiture.png").convert_alpha()
    self.rect = self.image.get_rect(center=(400,700))
    self.rect_x = 100
    self.velocity = 8
    self.health = 60
    self.max_heal = self.health
    self.attack = 20
    self.rectangle = pygame.Rect(self.rect.x,self.rect.y,70,123)



  def move_droite(self):
    if self.rect.x < 700:
      self.rect.x += self.velocity

  def move_gauche(self):
    if self.rect.x > 20:
      self.rect.x -= self.velocity
      
  def draw(self,win):
    self.rectangle = pygame.Rect(self.rect.x,self.rect.y,70,123)
    pygame.draw.rect(win,(0,0,0),self.rectangle,1)

  def update_health_bar(self, surface):
    bar_color = (71,209,71)
    back_bar_color = (230,0,0)
    bar_pos = [self.rect.x + 5, self.rect.y + self.rect.height,self.health, 5]
    back_bar_pos = [self.rect.x + 5,self.rect.y + self.rect.height, self.max_heal,5]

    pygame.draw.rect(surface, back_bar_color, back_bar_pos)
    pygame.draw.rect(surface, bar_color, bar_pos)

  def damage(self):
    self.health -= self.attack
    
