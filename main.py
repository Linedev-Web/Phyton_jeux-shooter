import pygame
from game import Game

pygame.init()

pygame.display.set_caption('Top game')
screen = pygame.display.set_mode((1080, 720))

background = pygame.image.load('assets/bg.jpg')

game = Game()

running = True

while running:

    screen.blit(background, (0, -200))

    screen.blit(game.player.image, game.player.rect)

    for projectile in game.player.all_projectile:
        projectile.move()

    game.player.all_projectile.draw(screen)

    pygame.display.flip()

    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")

        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
