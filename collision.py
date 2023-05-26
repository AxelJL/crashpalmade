import pygame
from player import Player
from ennemy import Ennemy

class Col:
  def __init__(self):
    self.player = Player()
    self.ennemy = Ennemy()
  def check(self):
    rectA = self.player.rect
    rectB = self.ennemy.rect
    return rectA.colliderect(rectB)
 
