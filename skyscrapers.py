"""
https://github.com/Adeon18/skyscrapers
"""


def read_input(path: str) -> list:
    """
    Read game board file from path.
    Return list of str.

    >>> read_input("check.txt")
    ['***21**', '452453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***']
    """
    with open(path, 'r') as file:
        output_lst = (file.read().split('\n'))
        output_lst = output_lst[:-1]
    
    return output_lst


def left_to_right_check(input_line: str, pivot: int):
    """
    Check row-wise visibility from left to right.
    Return True if number of building from the left-most hint is visible looking to the right,
    False otherwise.

    input_line - representing board row.
    pivot - number on the left-most hint of the input_line.

    >>> left_to_right_check("412453*", 4)
    True
    >>> left_to_right_check("452453*", 5)
    False
    """
    row = input_line
    max_num = 0
    for i, num in enumerate(row):
        if num == '*':
            continue
        if int(num) > max_num:
            max_num = int(num) 
            if i == pivot:
                return True
        elif int(num) <= max_num:
            if i == pivot:
                return False


def check_not_finished_board(board: list):
    """
    Check if skyscraper board is not finished, i.e., '?' present on the game board.

    Return True if finished, False otherwise.

    >>> check_not_finished_board(['***21**', '4?????*', '4?????*', '*?????5', '*?????*', '*?????*', '*2*1***'])
    False
    >>> check_not_finished_board(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_not_finished_board(['***21**', '412453*', '423145*', '*5?3215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    for row in board:
        if '?' in row:
            return False
    return True


# def check_uniqueness_in_rows(board: list):
#     """
#     Check buildings of unique height in each row.

#     Return True if buildings in a row have unique length, False otherwise.

#     >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
#     True
#     >>> check_uniqueness_in_rows(['***21**', '452453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
#     False
#     >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*553215', '*35214*', '*41532*', '*2*1***'])
#     False
#     """
#     pass


# def check_horizontal_visibility(board: list):
#     """
#     Check row-wise visibility (left-right and vice versa)

#     Return True if all horizontal hints are satisfiable,
#      i.e., for line 412453* , hint is 4, and 1245 are the four buildings
#       that could be observed from the hint looking to the right.

#     >>> check_horizontal_visibility(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
#     True
#     >>> check_horizontal_visibility(['***21**', '452453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
#     False
#     >>> check_horizontal_visibility(['***21**', '452413*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
#     False
#     """
#     pass


# def check_columns(board: list):
#     """
#     Check column-wise compliance of the board for uniqueness (buildings of unique height) and visibility (top-bottom and vice versa).

#     Same as for horizontal cases, but aggregated in one function for vertical case, i.e. columns.

#     >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
#     True
#     >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41232*', '*2*1***'])
#     False
#     >>> check_columns(['***21**', '412553*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
#     False
#     """
#     pass


# def check_skyscrapers(input_path: str):
#     """
#     Main function to check the status of skyscraper game board.
#     Return True if the board status is compliant with the rules,
#     False otherwise.

#     >>> check_skyscrapers("check.txt")
#     True
#     """
#     pass


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
    #print(read_input('check.txt'))
    #print(check_skyscrapers("check.txt"))