import pygame


class Equation:
    def __init__(self, grid_position) -> None:
        self.grid_position = grid_position

    def draw(self, surface, offset_position, resolution):
        new_pos = self.grid_to_cartesian(resolution)
        new_pos = (new_pos[0] + offset_position[0] + resolution / 2, new_pos[1] + offset_position[1] + resolution / 2)
        pygame.draw.circle(surface, (0, 0, 255), new_pos, resolution / 3)

    def grid_to_cartesian(self, resolution):
        return (self.grid_position[0] * resolution, self.grid_position[1] * resolution)

    def get_rect(self, resolution):
        return pygame.Rect(self.grid_to_cartesian(resolution), (resolution / 3, resolution / 3))