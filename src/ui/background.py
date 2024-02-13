import pygame


class Background:
    def __init__(self, **kwargs):
        self.id = kwargs.get("id", "")
        self.image = pygame.image.load(kwargs["image"])
        self.image = pygame.transform.smoothscale(self.image, (720, 1080))
        self.rect = self.image.get_rect(topleft=kwargs["position"])

    def render(self, surface):
        surface.blit(self.image, self.rect)
