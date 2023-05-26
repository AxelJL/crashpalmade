import pygame
from random import randint,choice

class Ennemy(pygame.sprite.Sprite):

  def __init__(self):
    
    def pick_ennemy():
      liste_ennemi = ["resources/voiture_rouge.png","resources/voiture_verte.png","resources/voiture_orange.png","resources/voiture_noir.png","resources/voiture_jaune.png","resources/voiture_grise.png","resources/voiture_bleu.png","resources/voiture_bleu_ciel.png"]
      return choice(liste_ennemi)
    
    super().__init__()
    self.velocity = 2
    self.image = pygame.image.load(pick_ennemy()).convert_alpha()
    self.image = pygame.transform.scale(self.image, (80, 120))
    self.image = pygame.transform.flip(self.image, False, True)
    self.rect = self.image.get_rect()
    x_hitbox = randint(0,675)
    y_hitbox = 0
    self.rect.x = x_hitbox
    self.rect.y = y_hitbox
    self.position_x = randint(0,675)
    self.position_y = 0
    self.rectangle = pygame.Rect(self.position_x,self.position_y,80,120)

  
  def update_acc(self,acceleration):
    self.velocity += acceleration
    return self.velocity

  
  def update_hit(self,win,vel):
    self.rectangle = pygame.Rect(self.rect.x,self.rect.y+self.velocity,80,120)
    self.rect.y += vel      
    if self.rect.y >= 920:
      self.rect.x = randint(0,675)
      self.rect.y = 0
    

