import pygame


class Ore:
    def __init__(self, position, gold_multiplier) -> None:
        self.grid_position = position
        self.width_ratio = 2
        self.gold_multiplier = gold_multiplier
        
    def to_gold(self):
        return 1 * self.gold_multiplier

    def draw(self, surface, offset_position, resolution):
        cartesian_position = self.get_rect_with_pos(resolution, offset_position)
        top_p = (cartesian_position[0] + resolution / (2 * self.width_ratio), cartesian_position[1])
        bottom_left_p = (cartesian_position[0], cartesian_position[1] + resolution / (self.width_ratio))
        bottom_right_p = (cartesian_position[0] + 2 * resolution / (2 * self.width_ratio), cartesian_position[1] + resolution / (self.width_ratio))
        #pygame.draw.rect(surface, (50, 0, 100), self.get_rect_with_pos(resolution, offset_position))
        pygame.draw.polygon(surface, (100, 50, 100),[top_p, bottom_left_p, bottom_right_p])

    def grid_to_cartesian(self, resolution):
        square_ofset = resolution / (2 * self.width_ratio)
        return (self.grid_position[0] * resolution + square_ofset, self.grid_position[1] * resolution + square_ofset)

    def get_rect(self, resolution):
        return pygame.Rect(self.grid_to_cartesian(resolution), (resolution, resolution))

    def get_rect_with_pos(self, resolution, offset_position):
        new_pos = self.grid_to_cartesian(resolution)
        new_pos = (offset_position[0] + new_pos[0], offset_position[1] + new_pos[1])
        return pygame.Rect(new_pos, (resolution / self.width_ratio, resolution / self.width_ratio))