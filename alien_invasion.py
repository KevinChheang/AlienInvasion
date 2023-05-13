import sys
import pygame

class AlienInvasion:
    """Overall class to manage game assets and behavi0r."""

    def __init__(self):
        """Initialze the game, and create game resources."""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Make the mose recently drawn screen visible.
            pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()