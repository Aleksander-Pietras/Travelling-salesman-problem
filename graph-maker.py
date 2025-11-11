''' This program will hold a function that will create a graph.
The function will create both: adjecnacy matrix and distance matrix'''
from validation_for_inputs import *
import sys

BLUE = "\033[94m"
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"



''' The display functions
Responsible for redrawing the matrix'''
def write(s):
    sys.stdout.write(s)
    sys.stdout.flush()

def clear_from_matrix_start(lines):
    write(f"\033[{lines}A")
    write("\033[J")



''' The graph functions
Responsible for mathematics'''
def make_graph (size:int = 1):
    adjacency_matrix = make_adjacency_matrix(size)

def text():
    print(f"\nValues in the matrix will show up in {BLUE}blue{RESET}")
    print(f"Once a value is changed it will turn {GREEN}green{RESET}")
    print(f"Indexes will appear in {RED}red{RESET}")
    print("To change an index enter the row number followed by the column number such as 12, row 1 column 2.")
    print("\nThis is what the current matrix looks like:")

def make_changes_to_a_matrix (matrix: list, size: int):
    text() # Stores the chunky text away to make working on code easier

    copy_of_matrix = matrix.copy()

    for i, row in enumerate(copy_of_matrix, start=1):

        for j, cell in enumerate(row, start=1):
            copy_of_matrix[i - 1][j - 1] = [f"{RED}{j}{RESET}", f"{BLUE}{cell}{RESET}"]

    for i, row in enumerate(copy_of_matrix, start=1):

        row_str = " ".join(f"[{col_id}, {val}]" for col_id, val in row)
        print(f"{RED}{i}{RESET}. {row_str}")

    row_index, column_index = valid_index("Enter an index you wish to change", 0, int(f"{size}{size}"))
    
    # More intuative for human to start at 1, BUT index needs to be shifted
    row_index, column_index = row_index - 1, column_index - 1
    copy_of_matrix[row_index][column_index][1] = f"{GREEN}{copy_of_matrix[row_index][column_index][1]}{RESET}" # As the copy of the matrix is a 3D matrix
    
    clear_from_matrix_start()




def make_adjacency_matrix (size:int) -> list:
    adjacency_matrix = []
    blank_matrix = valid_bool("Would you like a blank adjacency matrix")

    for row in range(size):
        temp_col = []
        for col in range(size):
            if row == col or blank_matrix:
                temp_col.append(0)
            else:
                temp_col.append(1)

        adjacency_matrix.append(temp_col)

    print(adjacency_matrix)

    changes = valid_bool("Would you like to make changes to the matrix")
    changes = "yes" # temp for debugging purpose

    if changes:
        adjacency_matrix = make_changes_to_a_matrix(adjacency_matrix, size)
        return adjacency_matrix
    else:
        return adjacency_matrix






make_graph(5)


