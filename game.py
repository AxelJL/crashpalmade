import pygame
from player import Player
from ennemy import Ennemy

class Game:

  def __init__(self):
    self.isPlaying = False #chek si le jeu a commencé
    self.player = Player()
    self.ennemy1 = Ennemy()
    self.ennemy2 = Ennemy()
    self.ennemy3 = Ennemy()
    self.pressed = {}
    self.score = 0

    #liste ennemy
    self.all_ennemy = pygame.sprite.Group()
    self.spawn_ennemy()

  def game_over(self):
    self.all_ennemy = pygame.sprite.Group()
    self.score = 0

    

  def update(self, fenetre):
    font = pygame.font.SysFont('Arial',25,True)
    score_a_afficher = font.render(f"Score : {self.score}",1,(255,255,255))
    fenetre.blit(score_a_afficher, (20,20))
    fenetre.blit(self.player.image, self.player.rect)
    if self.score <= 2500:
      self.ennemy1.update_hit(fenetre,self.ennemy1.update_acc(0.002))
      if self.score == 2500:
        self.ennemy2.velocity = self.ennemy1.velocity
    elif self.score > 2500 and self.score <= 5000:
      if self.score == 5000:
        self.ennemy3.velocity = self.ennemy1.velocity
      self.ennemy1.update_hit(fenetre,self.ennemy1.update_acc(0.004))
      self.ennemy2.update_hit(fenetre,self.ennemy2.update_acc(0.004))
    else:
      self.ennemy1.update_hit(fenetre,self.ennemy1.update_acc(0.005))
      self.ennemy2.update_hit(fenetre,self.ennemy2.update_acc(0.005))
      self.ennemy3.update_hit(fenetre,self.ennemy3.update_acc(0.005))

    
  def spawn_ennemy(self):
    ennemy = Ennemy()
    self.all_ennemy.add(ennemy)
  def nvelle_voiture(self):
    return [self.ennemy1,self.ennemy2,self.ennemy3]
