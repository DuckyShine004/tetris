import pygame

from src.constants.constants import GRAPH_HEIGHT, GRAPH_WIDTH


class GraphHelper:
    def __init__(self, graph):
        self.graph = graph
        self.ghost_positions = []

    def update(self, tetromino, keys):
        self.set_ghost_positions(tetromino)

        if keys[pygame.K_s]:
            tetromino.color_cells(False)
            tetromino.positions = list(self.ghost_positions)
            self.clear_ghost_positions()

    def set_ghost_positions(self, tetromino):
        height = 0

        for offset_y in range(GRAPH_HEIGHT):
            height = offset_y
            is_collision = False

            for position in tetromino.positions:
                delta = offset_y + position[1]

                if delta >= GRAPH_HEIGHT or self.graph.is_cell_occupied(delta, position[0]):
                    is_collision = True
                    break

            if is_collision:
                break

        self.set_new_ghost_positions(tetromino.positions, height)

    def set_new_ghost_positions(self, positions, height):
        self.clear_ghost_positions()

        for x, y in positions:
            delta = y + height - 1
            self.ghost_positions.append([x, delta])
            self.graph.set_ghost(delta, x, True)

    def set_falling_cell_positions(self, row, column, height):
        color = self.graph.cells[column][row].color
        delta = row + height

        self.graph.cells[column][delta].color = color
        self.graph.cells[column][row].color = None
        self.graph.cells[column][delta].is_occupied = True
        self.graph.cells[column][row].is_occupied = False

    def clear_ghost_positions(self):
        for x, y in self.ghost_positions:
            self.graph.set_ghost(y, x, False)

        self.ghost_positions.clear()

    def clear_full_rows(self):
        rows = []

        for row in range(GRAPH_HEIGHT):
            if all(self.graph.is_cell_occupied(row, column) for column in range(GRAPH_WIDTH)):
                rows.append(row)

        if not rows:
            return

        self.move_cells_down(rows)

    def clear_rows(self, rows):
        for row in rows:
            for column in range(GRAPH_WIDTH):
                self.graph.set_occupied(row, column, False)
                self.graph.set_color(row, column, None)

    def move_cells_down(self, rows):
        self.clear_rows(rows)

        start = rows[0]
        height = len(rows)

        for row in range(start - 1, -1, -1):
            for column in range(GRAPH_WIDTH):
                if not self.graph.is_cell_occupied(row, column):
                    continue

                self.set_falling_cell_positions(row, column, height)
