
import sys
from js import console, document
from pyodide.ffi.wrappers import add_event_listener
# https://jeff.glass/post/pyscript-why-create-proxy/

# Function to find the amount of water that can be trapped within
# a given set of bars in linear time and extra space
# https://www.techiedelight.com/trapping-rain-water-within-given-set-bars/
def trap(bars):

    changes = []

    n = len(bars)
    if n <= 2:
        return 0

    water = 0

    # `left[i]` stores the maximum height of a bar to the left
    # of the current bar
    left = [None] * (n - 1)
    left[0] = -sys.maxsize

    # process bars from left to right
    for i in range(1, n - 1):
        left[i] = max(left[i - 1], bars[i - 1])

    # `right` stores the maximum height of a bar to the right
    # of the current bar
    right = -sys.maxsize

    # process bars from right to left
    for i in reversed(range(1, n - 1)):
        right = max(right, bars[i + 1])

        # check if it is possible to store water in the current bar
        if min(left[i], right) > bars[i]:
            water += min(left[i], right) - bars[i]
            console.log(f"add {min(left[i], right) - bars[i]} water to column {i}")
            changes.append((i, min(left[i], right) - bars[i]))
            # print(changes)

    return water, changes


def wordle_to_matrix(input_text):
    """takes a copied wordle score and returns a list of lists of 1s and 0s"""
    # split the input text into lines
    lines = input_text.split("\n")

    # extract the dimensions of the puzzle
    puzzle_lines = lines[2:]
    rows = len(puzzle_lines)
    cols = len(puzzle_lines[0])

    # initialize 0s matrix
    puzzle = [[0 for _ in range(cols)] for _ in range(rows)]

    # parse the puzzle from the input text
    for n, line in enumerate(puzzle_lines):
        for m, c in enumerate(line):
            if c == "🟩":
                # if the character is green, set the cell to 1
                puzzle[n][m] = 1
            elif c == "🟨":
                # if the character is yellow, set the cell to 2
                puzzle[n][m] = 2

    # for line in puzzle:
    #     print(line)
    return puzzle


def to_elevation_map(puzzle):
    """takes a puzzle matrix and returns a list of heights"""
    elevation_map = []

    # for each column in the puzzle
    for col in range(len(puzzle[0])):
        # iterate from the top row to the bottom row
        for row in range(len(puzzle)):
            if puzzle[row][col] != 0:
                # if the cell is not black, add the height of the cell to the elevation map
                elevation_map.append(len(puzzle) - row)
                break
        else:
            # if the column is entirely black, add a height of 0 to the elevation map
            elevation_map.append(0)

    # return the elevation map as a list of heights
    return elevation_map


def matrix_to_icons(lst):
    icons = {0: "⬛", 1: "🟩", 2: "🟨", 3: "🟦"}
    output = ""
    for sublist in lst:
        for num in sublist:
            output += icons[num]
        output += "\n"
    return output

def fill_zeros(column, value):
    if value in column:
        first_index = column.index(value) 
        for i in range(first_index + 1, len(column)): 
            if column[i] == 0 and column[i-1] == value: 
                column[i] = value 
    return column 

def downfill(m):
    filled_matrix = [row[:] for row in m]

    for i in range(len(filled_matrix[0])):
        column = [filled_matrix[j][i] for j in range(len(filled_matrix))]
        column = fill_zeros(column, 1) # fill zeros below 1
        column = fill_zeros(column, 2) # fill zeros below 2
        for j in range(len(filled_matrix)):
            filled_matrix[j][i] = column[j] # update the matrix with the modified column

    return filled_matrix

def addwater(matrix, changes):
    # Apply changes to the matrix
    for col, num_zeros in changes:
        for i in range(len(matrix) - 1, -1, -1):
            if num_zeros == 0:
                break
            if matrix[i][col] == 0:
                matrix[i][col] = 3
                num_zeros -= 1

    return matrix_to_icons(matrix)


def run_it(*args):

    # Get the user input
    message = document.getElementById("userinput").value
    console.log(message)

    # Create the output element
    output = Element("output")

    # Convert the input message to a matrix of elevation values
    matrix = wordle_to_matrix(message)
    elev_map = to_elevation_map(matrix)

    # Compute the amount of water that can be trapped and the required changes
    water, changes = trap(elev_map)

    # Add water to the matrix according to the required changes
    changed_matrix = addwater(downfill(matrix), changes)

    # Set the output text to display the elevation map, the amount of water, and the changed matrix
    output_text = (
        "\n" + str(changed_matrix) + "\n" + str(water) + " units of water"
    )

    output.element.innerText = output_text

    # document.getElementById("userinput").innerText = changed_matrix

add_event_listener(document.getElementById("btn"), "click", run_it)
add_event_listener(document.getElementById("userinput"), "submit", run_it)


