import pygame, sys
from pygame.locals import QUIT
from game import Game
from random import randint,choice


fenetre = pygame.display.set_mode((1000, 725), pygame.FULLSCREEN)
pygame.display.set_caption('Crash Palmade')

#Initialisation
pygame.init()
p = pygame
game = Game()
jouer = True
compt = 0
compt_score = 0
y_background = 0
acceleration_fond = 0
clock = pygame.time.Clock()
voit = 0
l = game.nvelle_voiture()




#Image
img_fond = p.image.load("resources/fond.png")
fond = img_fond.convert()


img_feu_vert = p.image.load("resources/feu_vert.png").convert_alpha()
img_feu_vert = p.transform.scale(img_feu_vert,(150,250))
img_feu_orange = p.image.load("resources/feu_orange.png")
img_feu_orange = p.transform.scale(img_feu_orange, (150,250))
img_feu_rouge = p.image.load("resources/feu_rouge.png")
img_feu_rouge = p.transform.scale(img_feu_rouge, (150,250))
pierrepalmadephotofin = p.image.load("resources/pierrepalmadephotofin.jpg")
pierrepalmadephotofin = p.transform.scale(pierrepalmadephotofin, (147,250))
fond_loading = p.image.load("resources/fond_start.jpg").convert_alpha()
fond_loading = p.transform.scale(fond_loading, (450,160))


#Texte
font = p.font.SysFont(None, 20)
font3 = p.font.SysFont(None, 40)
mess1 = font.render("Viens te crasher avec Pierre Palmade !!!",1,(0,255,0))
mess2 = font.render("Made with heart by Diego & Alex & Hector <3",1,(0,255,0))
mess_score = font.render("Les Meillieurs score : ",1,(0,255,255))



#MUSIQUE de fond
mus_dep = p.mixer.Sound("resources/musiquedepart.mp3")
mus = p.mixer.Sound("resources/Dumaya.mp3")
epique = p.mixer.Sound("resources/fortuna.mp3")
moteur1 = p.mixer.Sound("resources/vroum1.mp3")
moteur2 = p.mixer.Sound("resources/vroum2.mp3")
moteur3 = p.mixer.Sound("resources/vroum3.mp3")
m = [moteur1, moteur2,moteur3]
ecraser = p.mixer.Sound("resources/allonsecraser.mp3")
plus = p.mixer.Sound("resources/encoreplus.mp3")
mus.play(loops=-1)


def draw_text(text, font, color, surface, x,y):
  textobj = font.render(text, 1, color)
  textrect = textobj.get_rect()
  textrect.topleft = (x,y)
  surface.blit(textobj, textrect)



#Boucle Jouer
while jouer:

  
  y_background += 1 + acceleration_fond

  

  if y_background < 619:
    fenetre.blit(fond, (0, y_background))
    fenetre.blit(fond, (0, y_background - 619))
  else:
    y_background = 0
    fenetre.blit(fond, (0, y_background))
    
  if game.isPlaying == True:
    if compt%2 == 0:
      mus.stop()
      ecraser.play()
      p.time.wait(2500)
      mus_dep.play()
      fenetre.blit(img_feu_rouge, (325,300))
      p.display.flip()
      pygame.time.wait(1013)
      fenetre.blit(img_feu_orange, (325,302))
      p.display.flip()
      p.time.wait(977)
      fenetre.blit(img_feu_vert, (330,302))
      p.display.flip()
      p.time.wait(2539)
      r = choice(m)
      r.play()
      p.time.wait(3000)
      compt+= 1
      mus.play(loops=-1)
    else:
      game.update(fenetre)
      game.player.draw(fenetre)
      game.player.update_health_bar(fenetre)
      game.score += 1
      p.display.flip()
      if voit == 0 and game.score <= 2500:
        plus.play()
        fenetre.blit(l[0].image,l[0].rect)
        p.display.flip()
        if game.player.rectangle.colliderect(game.ennemy1.rectangle) == True:
          game.player.damage()
          game.ennemy1.rect.y = 0
          game.ennemy1.rect.x = randint(0,675)
          game.ennemy1.position_y = 0
          game.ennemy1.position_x = game.ennemy1.rect.x
        if game.score >= 2450:
          voit += 1
      elif voit == 1 and game.score <= 5000:
        plus.play()
        fenetre.blit(l[0].image,l[0].rect)
        fenetre.blit(l[1].image,l[1].rect)
        p.display.flip()
        if game.player.rectangle.colliderect(game.ennemy1.rectangle) == True or game.player.rectangle.colliderect(game.ennemy2.rectangle) == True:
          game.player.damage()
          game.ennemy1.rect.y = 0
          game.ennemy1.rect.x = randint(0,675)
          game.ennemy1.position_y = 0
          game.ennemy1.position_x = game.ennemy1.rect.x
          if game.ennemy1.position_y >= 200:
            game.ennemy2.rect.y = 0
            game.ennemy2.rect.x = randint(0,675)
            game.ennemy2.position_y = 0
            game.ennemy2.position_x = game.ennemy1.rect.x
        if game.score >= 4950:
          voit += 1
      elif voit == 2 and game.score > 5000:
        plus.play()
        fenetre.blit(l[0].image,l[0].rect)
        fenetre.blit(l[1].image,l[1].rect)
        fenetre.blit(l[2].image,l[2].rect)
        p.display.flip()
        if game.player.rectangle.colliderect(game.ennemy1.rectangle) == True or game.player.rectangle.colliderect(game.ennemy2.rectangle) == True or game.player.rectangle.colliderect(game.ennemy3.rectangle) == True:
          game.player.damage()
          game.ennemy1.rect.y = 0
          game.ennemy1.rect.x = randint(0,675)
          game.ennemy1.position_y = 0
          game.ennemy1.position_x = game.ennemy1.rect.x
          if game.ennemy1.position_y >= 200:
            game.ennemy2.rect.y = 0
            game.ennemy2.rect.x = randint(0,675)
            game.ennemy2.position_y = 0
            game.ennemy2.position_x = game.ennemy1.rect.x
          if game.ennemy1.position_y >= 200 and game.ennemy2.position_y >= 120:
            game.ennemy3.rect.y = 0
            game.ennemy3.rect.x = randint(0,675)
            game.ennemy3.position_y = 0
            game.ennemy3.position_x = game.ennemy1.rect.x
      if game.player.health == 60:
        game.player.rect.y = 600
      elif game.player.health == 40:
        game.player.rect.y = 500
      elif game.player.health == 20:
        game.player.rect.y = 400
      elif game.player.health == 0:
        game.isPlaying = False
        compt_score += 1
        game.player.health = 60
        ancien_score = game.score
        game.score = 0
        game.ennemy1.velocity = 2
        y_background = 0
        voit = 0
        acceleration_fond = 0
        epique.stop()
        mus.stop()
      if game.score >= 7500:
        mus.stop()
        epique.play(loops=-1)
      
        
      
      if acceleration_fond > 20:
        acceleration_fond = 14
      if acceleration_fond < 11:
        acceleration_fond += 0.001
    
  else:
    if compt%2 == 1:
      mess_score_ancien = font3.render(f"Votre score précédent était de :  {ancien_score}",1,(255,0,0))
      fenetre.blit(mess_score_ancien,(150,200))
    fenetre.blit(mess1, (280,300))
    fenetre.blit(mess2, (260,550))
    fenetre.blit(fond_loading, (180,350))   
    p.display.flip()
    


  clock.tick(45)
  #Evenement 
  for event in pygame.event.get():
    if event.type == p.QUIT:
      jouer = False
      p.quit()
    elif event.type == p.KEYDOWN:
      game.pressed[event.key] = True
      if game.pressed.get(p.K_ESCAPE):
        p.quit()
      if game.pressed.get(p.K_SPACE):
        if game.isPlaying == False and compt % 2 == 1:
          game.isPlaying = True
          compt += 1
        elif game.isPlaying == False:
          game.isPlaying = True
        else:
          exit_btn = p.image.load("resources/exit_btn.png")
          exit_btn = p.transform.scale(exit_btn, (220,250))
          fenetre.blit(exit_btn, (325,300))
          p.display.flip()
          pygame.time.wait(5000)
    elif event.type == p.KEYUP:
      game.pressed[event.key] = False
  if game.pressed.get(p.K_RIGHT) and game.player.rect_x + game.player.rect.width < fenetre.get_width():
    game.player.move_droite()
  if game.pressed.get(p.K_LEFT) and game.player.rect_x > 0:
    game.player.move_gauche()
  if game.ennemy1.rect.colliderect(game.player) or game.ennemy2.rect.colliderect(game.player) or game.ennemy3.rect.colliderect(game.player):
    pygame.QUIT
