def valid_bool(question: str) -> bool:
    """Ask a yes/no question and return True or False."""
    while True:
        answer = input(f"{question} (yes/no): ").strip().lower()
        if answer in ("yes", "y"):
            return True
        elif answer in ("no", "n"):
            return False
        else:
            print("Please answer 'yes' or 'no'.")

def valid_int(question: str) -> int:
    """Ask for an integer and keep asking until valid."""
    while True:
        try:
            value = input(f"{question}: ").strip()
            int(value)
            return value
        except ValueError:
            print("Please enter a valid integer.")

def valid_range(question: str, min_val: int, max_val: int) -> int:
    """Ask for an integer within a specific range.
    Internally uses valid_int() for integer validation.
    """
    while True:
        value = valid_int(f"{question} (between {min_val} and {max_val})")
        if min_val <= int(value) <= max_val:
            return value
        print(f"Value must be between {min_val} and {max_val}.")

def instruction_text_for_valid_index():
    print("Error: icorrect input format")
    print("Ensure that the input is in a valid format, which includes 0 as characters")

    clarify = valid_bool("Would you like to see examples of correct inputs?")
    if clarify:
        print("If you wish to select row 1, column 4.")
        print("Enter 14, as your input")
        print("\nIf you wish to select row 12, column 20.")
        print("Enter 1420, as your input")
        print("\nIf you wish to select row 1, column 51.")
        print("Enter: 0151, as your input")
        print("\nIf you wish to select row 178, column 2.")
        print("Enter: 178002, as your input")

def valid_index(question: str, min_val: int, max_val: int, size: int) -> int:
    """Not Implemented yet"""
    while True:
        index = valid_range(question, min_val, max_val)
        if len(index) % 2 != 0:
            instruction_text_for_valid_index() # Triggeres error statement and makes the user retry

        else: 
            pass

            



    row_index, column_index = [int(x) for x in index]
