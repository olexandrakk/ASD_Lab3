def calculate_positions(n, canvas_width, canvas_height):
    positions = []
    center_x = canvas_width // 2
    center_y = canvas_height // 2
    positions.append((center_x, center_y))  # Вершина 0

    margin = 100
    positions.append((margin, margin))  # 1
    positions.append((center_x, margin))  # 2
    positions.append((canvas_width - margin, margin))  # 3
    positions.append((canvas_width - margin, center_y))  # 4
    positions.append((canvas_width - margin, canvas_height - margin))  # 5
    positions.append((center_x, canvas_height - margin))  # 6
    positions.append((margin, canvas_height - margin))  # 7
    positions.append((margin, center_y))  # 8

    return positions