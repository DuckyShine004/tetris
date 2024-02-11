import pygame
from src.graph.graph import Graph

from src.constants.constants import (
    SURFACE_COLOR,
    WIDTH,
    HEIGHT,
    FPS,
    MUSIC_PATH,
)


class App:
    def __init__(self):
        self.surface = pygame.display.set_mode((WIDTH, HEIGHT))
        self.is_running = True

        self.graph = Graph()

    def run(self):
        self.play_music()
        clock = pygame.time.Clock()

        while self.is_running:
            self.surface.fill((SURFACE_COLOR))
            self.handle_events()

            self.update()
            self.render()

            pygame.display.flip()
            clock.tick(FPS)

    def update(self):
        self.graph.update()

    def render(self):
        self.graph.render(self.surface)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

            self.handle_peripherals(event)

    def handle_peripherals(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.is_running = False

    def play_music(self):
        pygame.mixer.music.load(MUSIC_PATH)
        pygame.mixer.music.play(-1)
