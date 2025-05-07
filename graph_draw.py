import math
import tkinter as tk

def draw_graph(canvas, positions, adj_matrix, directed=True):
    n = len(positions)
    radius = 15
    offset = 10

    for i in range(n):
        xi, yi = positions[i]
        canvas.create_oval(xi - radius, yi - radius, xi + radius, yi + radius, fill="white", outline="black")
        canvas.create_text(xi, yi, text=str(i))

    for i in range(n):
        for j in range(n):
            if adj_matrix[i][j] == 1 and i != j:
                xi, yi = positions[i]
                xj, yj = positions[j]

                dx = xj - xi
                dy = yj - yi
                dist = math.hypot(dx, dy)
                if dist == 0:
                    continue

                dx /= dist
                dy /= dist

                start_x = xi + dx * radius
                start_y = yi + dy * radius
                end_x = xj - dx * radius
                end_y = yj - dy * radius

                is_back_edge = adj_matrix[j][i] == 1

                if directed:
                    if is_back_edge:
                        ctrl_x = (start_x + end_x) / 2 - dy * offset
                        ctrl_y = (start_y + end_y) / 2 + dx * offset
                        canvas.create_line(start_x, start_y, ctrl_x, ctrl_y, end_x, end_y,
                                           arrow=tk.LAST, smooth=True, fill="blue")
                    else:
                        canvas.create_line(start_x, start_y, end_x, end_y, arrow=tk.LAST, fill="blue")
                else:
                    canvas.create_line(start_x, start_y, end_x, end_y, fill="black")