from cell import Cell
from maze import Maze
from convert import Feasibility
import numpy as np
from PIL import Image, ImageDraw, ImageFont

margin = 80
cell_side = 100
line_thickness = 10


def draw_cell(cell, image, color="black", count=0, wide=5, method="grid"):
    # Cell coordinates on the image calculated from its (x, y) coordinates,
    # cell side length (100 pt), image margin (90 pt) and line thickness (10 pt).
    x = margin + line_thickness + cell.x * cell_side
    y = margin + line_thickness + cell.y * cell_side

    lines = [(x - cell_side / 2, y - cell_side / 2), (x + cell_side / 2, y - cell_side / 2)], \
            [(x - cell_side / 2, y + cell_side / 2), (x + cell_side / 2, y + cell_side / 2)], \
            [(x + cell_side / 2, y - cell_side / 2), (x + cell_side / 2, y + cell_side / 2)], \
            [(x - cell_side / 2, y - cell_side / 2), (x - cell_side / 2, y + cell_side / 2)]

    shown_walls = [i for (i, v) in zip(lines, cell.walls.values()) if v]
    for wall in shown_walls:
        image.line(wall, fill=color, width=wide)
    if cell.status == 'Start' or cell.status == 'End':
        try:
            font = ImageFont.truetype("Arial Unicode.ttf", 18)
            image.text((x - 25, y - 10), cell.status.upper(), (255, 0, 0), font=font)
        except OSError:
            font = ImageFont.load_default()
            image.text((x - 25, y - 10), cell.status.upper(), (255, 0, 0), font=font)
    else:
        if method == "grid":
            try:
                font = ImageFont.truetype("Arial Unicode.ttf", 18)
                image.text((x - 35, y - 35), str(count), fill="#D3D3D3", font=font)
            except OSError:
                font = ImageFont.load_default()
                image.text((x - 35, y - 35), str(count), fill="#D3D3D3", font=font)


def draw_grid(image, x_cells, y_cells):
    cells_ = {}
    count = 0
    for i in range(x_cells):
        for j in range(y_cells):
            cell_name = count
            count += 1
            cells_[cell_name] = Cell(i, j)
    for num, cel in cells_.items():
        draw_cell(cel, image, "lightgray", num)


def draw_image(maze_img, cells):
    # maze_img = ImageDraw.Draw(image)
    draw_grid(maze_img, cells.shape[0], cells.shape[1])
    for cell in cells.flatten():
        draw_cell(cell, maze_img, method="not_grid")
    # draw_agent(cells.flatten()[0], maze_img)
    # image.save(filename)


def draw_agent(cell, image, color="blue"):
    x = margin + line_thickness + cell.x * cell_side
    y = margin + line_thickness + cell.y * cell_side
    image.ellipse((x - cell_side / 3, y - cell_side / 3, x + cell_side / 3, y + cell_side / 3), fill=color)


def make_movie(width, height, maze, feasibility, path, filename="maze_path.gif"):
    images = []
    for position in path:
        # cell = np.where(feasibility.numbered_grid=path)
        ind1 = np.where(feasibility.numbered_grid == position)[0][0]
        ind2 = np.where(feasibility.numbered_grid == position)[1][0]
        cell = maze.maze_grid[ind1, ind2]

        im = Image.new('RGB', (width, height), (255, 255, 255))
        draw = ImageDraw.Draw(im)
        draw_image(draw, maze.maze_grid)
        draw_agent(cell, draw)
        images.append(im)

    images[0].save(filename, save_all=True, append_images=images[1:], optimize=False, duration=400, loop=0)

if __name__ == '__main__':
    # dimension1 = int(input('Enter x dimension: '))
    # dimension2 = int(input('Enter y dimension: '))
    # start_x = int(input('Enter x coordinate of the start: '))
    # start_y = int(input('Enter y coordinate of the start: '))

    dimension1 = 5
    dimension2 = 5
    start_x = 1
    start_y = 1

    # margin = 80
    # cell_side = 100
    # line_thickness = 10
    # maze = Maze(dimension1, dimension2)
    # maze = Maze(dimension1, dimension2, [start_x, start_y])
    #
    # width, height = (margin + cell_side * dim for dim in maze.maze_grid.shape)
    # img = Image.new("RGB", (width, height), (255, 255, 255))
    # draw_image(img, "maze.png", maze.maze_grid)

    maze = Maze(dimension1, dimension2, [start_x, start_y])
    width, height = (margin + cell_side * dim for dim in maze.maze_grid.shape)

    feasibility = Feasibility(maze)
    path = [6, 11, 10, 15, 16, 21, 20]

    make_movie(width, height, maze, feasibility, path)



