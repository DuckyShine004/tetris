import pygame


class Container:
    def __init__(self, **kwargs):
        self.id = kwargs.get("id", "")
        self.rect = pygame.Rect(*kwargs["position"], *kwargs["size"])
        self.color = kwargs["color"]
        self.border = kwargs.get("border", [])
        self.z_buffer = kwargs["z-buffer"]

        print(self.rect.center)

    def render(self, surface):
        if not self.border:
            pygame.draw.rect(surface, self.color, self.rect)
            return

        pygame.draw.rect(surface, self.color, self.rect, *self.border)
