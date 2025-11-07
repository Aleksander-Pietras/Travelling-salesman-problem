''' This program will hold a function that will create a graph.
The function will create both: adjecnacy matrix and distance matrix'''

BLUE = "\033[94m"
GREEN = "\033[92m"
RESET = "\033[0m"



def make_graph (size:int = 1):
    adjacency_matrix = make_adjacency_matrix(size)


def make_adjacency_matrix (size:int) -> list:
    adjacency_matrix = []
    #blank_matrix = input("Would you like a blank adjacency matrix: ").lower()

    for row in range(size):
        temp_col = []
        for col in range(size):
            if row == col:
                temp_col.append(0)
            else:
                temp_col.append(1)

        adjacency_matrix.append(temp_col)

    print(adjacency_matrix)

    valid_choice = False

    while valid_choice is False:
        #change = input("Would you like to make changes to the adjacency matrix: ").lower()
        change = "yes" # temp for debugging purpose

        if change == "yes":
            adjacency_matrix = make_changes_to_a_matrix(adjacency_matrix)
            valid_choice = True
            return adjacency_matrix
        
        elif change == "no":
            valid_choice = True
            return adjacency_matrix
        
        else:
            valid_choice = False
            print("Plese answer either 'yes' or 'no'.")

def make_changes_to_a_matrix (matrix: list):
    print(f"\nValues in the matrix will show up in {BLUE}blue{RESET}")
    print(f"Once a value is changed it will turn {GREEN}green{RESET}")
    print("\nThis is what the current matrix looks like:")

    copy_of_matrix = matrix.copy()

    for i, row in enumerate(copy_of_matrix, start=1):
        col_id = []

        print(f"{i}. {row}")

        for cell_id in range(1, len(row) + 1):
            pass



        #print(cell_numbers)



make_graph(5)
