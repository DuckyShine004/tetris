import pygame

from src.constants.constants import SURFACE_COLOR, WIDTH, HEIGHT, FPS


class App:
    def __init__(self):
        self.surface = pygame.display.set_mode((WIDTH, HEIGHT))
        self.is_running = True

    def run(self):
        clock = pygame.time.Clock()

        while self.is_running:
            self.surface.fill((SURFACE_COLOR))
            self.handle_events()

            pygame.display.flip()
            clock.tick(FPS)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
