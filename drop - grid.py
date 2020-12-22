from cell import Cell
import random

class Grid:

    def __init__(self, size):
        self.grid = []
        self.game_state = "progress"

        for i in range(0, size + 2):
            row = []
            for j in range(0, size + 2):
                is_wall = False
                cell_type = "unrevealed"
                if i == 0 or j == 0 or i == size + 1 or j == size + 1:
                    cell_type = "revealed"
                else:
                    is_wall = random.randint(0, 10) == 0

                cell = Cell(i, j, cell_type, is_wall)
                row.append(cell)

            self.grid.append(row)

    def count_neighbour_mines(self, row, column):
        count = 0
        for i in range(-1, 2):
            for j in range(-1 , 2):
                if self.grid[row + i][column + j].get_is_wall():
                    count += 1

        return count

    def reveal(self, row, column):
        if self.grid[row][column].get_is_wall():
            self.game_state = "lose"
            self.reveal_all_mines()
        else:
            neighbour_mine_count = self.count_neighbour_mines(row, column)
            if neighbour_mine_count == 0:
                self.grid[row][column].set_cell_type("revealed")
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if self.grid[row + i][column + j].get_cell_type() == "unrevealed":
                            self.reveal(row + i, column + j)
            else:
                self.grid[row][column].set_cell_type(str(neighbour_mine_count))

    def reveal_all_walls(self):
        for i in range(1, len(self.grid) - 1):
            for j in range(1, len(self.grid) - 1):
                if self.grid[i][j].get_is_wall():
                    self.grid[i][j].set_cell_type("wall")

    def handle_click(self, row, column):
        if self.game_state == "progress":
            self.reveal(row, column)

    def draw(self, canvas, resource, image_size):
        for i in range(1, len(self.grid) - 1):
            for j in range(1, len(self.grid) - 1):
                self.grid[i][j].draw(canvas, resource, image_size)