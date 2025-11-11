import os
import sys

def write(s):
    sys.stdout.write(s)
    sys.stdout.flush()

def clear_from_matrix_start(line_count_before_matrix):
    # Move cursor up that many lines
    write(f"\033[{line_count_before_matrix}A")
    # Clear from there down
    write("\033[J")

def print_before_matrix():
    lines = [
        "Values in the matrix will show up in blue",
        "Once a value is changed it will turn green",
        "Indexes will appear in red",
        "To change an index enter row and column together (e.g., 12).",
        "",
        "Matrix:"
    ]
    for line in lines:
        print(line)
    return len(lines)  # number of lines printed before matrix

def display_matrix(matrix):
    for i, row in enumerate(matrix, start=1):
        row_str = " ".join(f"[{j},{val}]" for j, val in enumerate(row, start=1))
        print(f"{i}. {row_str}")

# Example
lines_before = print_before_matrix()
matrix = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
display_matrix(matrix)

input("\nPress Enter to clear and redraw...")

clear_from_matrix_start(lines_before)
display_matrix([[0, 2, 2], [2, 0, 2], [2, 2, 0]])
