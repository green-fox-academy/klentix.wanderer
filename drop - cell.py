class Cell:

    def __init__(self, row, column, cell_type, is_wall):
        self.row = row
        self.column = column
        self.cell_type = cell_type
        self.is_wall = is_wall

    def get_is_wall(self):
        return self.is_wall

    def get_cell_type(self):
        return self.cell_type

    def set_cell_type(self, cell_type):
        self.cell_type = cell_type

    def draw(self, canvas, resource, image_size):
        canvas.create_image(self.row * image_size - image_size + (image_size / 2), self.column * image_size - image_size + (image_size / 2), image=resource.get_image(self.cell_type))
