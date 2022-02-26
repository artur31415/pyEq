import pygame


class Equation:
    def __init__(self, grid_position) -> None:
        self.grid_position = grid_position
        self.is_selected = False
        self.walk_pattern = [(-2, 0), (-1, 0), (2, 0), (1, 0), (0, -1), (0, 1)]

    def can_move_to(self, new_grid_position):
        for pattern in self.walk_pattern:
            if new_grid_position == (self.grid_position[0] + pattern[0], self.grid_position[1] + pattern[1]):
                return True
        return False

    def draw_walk_pattern(self, surface, offset_position, resolution):
        new_pos = self.grid_to_cartesian(resolution)
        new_pos = (new_pos[0] + offset_position[0] + resolution / 2, new_pos[1] + offset_position[1] + resolution / 2)

        for pattern in self.walk_pattern:
            current_grid_pos = (self.grid_position[0] + pattern[0], self.grid_position[1] + pattern[1])
            pattern_pos = (new_pos[0] + resolution * pattern[0], new_pos[1] + resolution * pattern[1])
            if current_grid_pos[0] > -1 and current_grid_pos[1] > -1 and current_grid_pos[0] < 8 and current_grid_pos[1] < 8:
                pygame.draw.circle(surface, (100, 0, 255), pattern_pos, resolution / 4)

    def draw(self, surface, offset_position, resolution):
        new_pos = self.grid_to_cartesian(resolution)
        new_pos = (new_pos[0] + offset_position[0] + resolution / 2, new_pos[1] + offset_position[1] + resolution / 2)
        pygame.draw.circle(surface, (0, 100, 255), new_pos, resolution / 3)

    def grid_to_cartesian(self, resolution):
        return (self.grid_position[0] * resolution, self.grid_position[1] * resolution)

    def get_rect(self, resolution):
        return pygame.Rect(self.grid_to_cartesian(resolution), (resolution, resolution))

    def get_rect_with_pos(self, resolution, offset_position):
        new_pos = self.grid_to_cartesian(resolution)
        new_pos = (new_pos[0] + offset_position[0], new_pos[1] + offset_position[1])
        return pygame.Rect(new_pos, (resolution, resolution))