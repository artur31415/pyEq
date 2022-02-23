from turtle import position

import pygame


class Slot:
    def __init__(self, grid_position, color) -> None:
        self.grid_position = grid_position
        self.color = color

    def draw(self, surface, offset_position, resolution):
        pygame.draw.rect(surface, self.color, self.get_rect_with_pos(resolution, offset_position))

    def grid_to_cartesian(self, resolution):
        return (self.grid_position[0] * resolution, self.grid_position[1] * resolution)

    def get_rect(self, resolution):
        return pygame.Rect(self.grid_to_cartesian(resolution), (resolution, resolution))

    def get_rect_with_pos(self, resolution, offset_position):
        new_pos = self.grid_to_cartesian(resolution)
        new_pos = (offset_position[0] + new_pos[0], offset_position[1] + new_pos[1])
        return pygame.Rect(new_pos, (resolution, resolution))