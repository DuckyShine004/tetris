import pygame


class Image:
    def __init__(self, **kwargs):
        self.id = kwargs.get("id", "")
        self.image = pygame.image.load(kwargs["image"])
        self.image = pygame.transform.scale(self.image, kwargs["size"])

        if kwargs["topleft"]:
            self.rect = self.image.get_rect(topleft=kwargs["position"])
        else:
            self.rect = self.image.get_rect(center=kwargs["position"])

        self.z_buffer = kwargs["z-buffer"]

    def render(self, surface):
        surface.blit(self.image, self.rect)
