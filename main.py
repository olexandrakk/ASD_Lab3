import tkinter as tk
from graph_matrix import generate_adj_matrix, make_undirected
from positions import calculate_positions
from graph_draw import draw_graph

def main():
    seed = 4408
    n = 9

    dir_matrix = generate_adj_matrix(n, seed)
    undir_matrix = make_undirected(dir_matrix)

    print("Матриця суміжності напрямленого графа:")
    for row in dir_matrix:
        print(' '.join(map(str, row)))
    print("\nМатриця суміжності ненапрямленого графа:")
    for row in undir_matrix:
        print(' '.join(map(str, row)))

    root = tk.Tk()
    root.title("Лабораторна робота 3. Графи")

    canvas_width = 800
    canvas_height = 600

    frame_dir = tk.Frame(root)
    frame_dir.pack(side=tk.LEFT, padx=10, pady=10)
    label_dir = tk.Label(frame_dir, text="Напрямлений граф")
    label_dir.pack()
    canvas_dir = tk.Canvas(frame_dir, width=canvas_width, height=canvas_height, bg="white")
    canvas_dir.pack()

    frame_undir = tk.Frame(root)
    frame_undir.pack(side=tk.RIGHT, padx=10, pady=10)
    label_undir = tk.Label(frame_undir, text="Ненапрямлений граф")
    label_undir.pack()
    canvas_undir = tk.Canvas(frame_undir, width=canvas_width, height=canvas_height, bg="white")
    canvas_undir.pack()

    positions = calculate_positions(n, canvas_width, canvas_height)

    draw_graph(canvas_dir, positions, dir_matrix, directed=True)
    draw_graph(canvas_undir, positions, undir_matrix, directed=False)

    root.mainloop()

if __name__ == "__main__":
    main()