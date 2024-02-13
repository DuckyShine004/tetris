"""This module defines the lifecycle of the application."""

import pygame

from src.ui.ui import UI

from src.graph.graph import Graph


from src.constants.constants import (
    SURFACE_COLOR,
    UI_PATH,
    WIDTH,
    HEIGHT,
    FPS,
    MUSIC_PATH,
)


class App:
    """The App class holds the main application loop. It handles updating
    and rendering components. This module defines the lifecycle of the
    application.

    Attributes:
        graph (TYPE): The graph object.
        is_running (bool): Is the application running.
        surface (pygame.Surface): The display surface.
        ui (UI): The UI object.
    """

    def __init__(self) -> None:
        """Initializes the App module."""

        self.surface: pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
        self.is_running: bool = True

        self.ui: UI = UI(UI_PATH)
        self.graph: Graph = Graph(self.ui)

    def run(self) -> None:
        """The main application loop."""

        self.play_music()
        clock = pygame.time.Clock()

        while self.is_running:
            self.surface.fill((SURFACE_COLOR))
            self.handle_events()

            self.update()
            self.render()

            pygame.display.flip()
            clock.tick(FPS)

    def update(self) -> None:
        """Updates the application."""

        self.ui.update()
        self.graph.update()

    def render(self) -> None:
        """Render application components."""

        self.ui.render(self.surface)
        self.graph.render(self.surface)

    def handle_events(self) -> None:
        """Handle pygame events."""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

            self.handle_peripherals(event)

    def handle_peripherals(self, event: pygame.event.Event) -> None:
        """Handle peripheral events.

        Args:
            event (pygame.event.Event): The current pygame event
        """

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.is_running = False

    def play_music(self) -> None:
        """Plays the application music loop."""

        pygame.mixer.music.load(MUSIC_PATH)
        pygame.mixer.music.play(-1)
