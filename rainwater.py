import streamlit as st

# def trap(height: List[int]) -> int:
#     if not height:
#         return 0

#     l, r = 0, len(height) - 1
#     leftMax, rightMax = height[l], height[r]
#     res = 0
#     while l < r:
#         if leftMax < rightMax:
#             l += 1
#             leftMax = max(leftMax, height[l])
#             res += leftMax - height[l]
#         else:
#             r -= 1
#             rightMax = max(rightMax, height[r])
#             res += rightMax - height[r]
#     return res

def trap(height):
    stack = []
    water = 0
    i = 0
    water_coords = []
    
    # iterate through the list of heights
    while i < len(height):
        # if the stack is empty or the current height is less than or equal to the previous height
        if len(stack) == 0 or height[stack[-1]] >= height[i]:
            # push the current index to the stack and move to the next index
            stack.append(i)
            i += 1
        else:
            # if the current height is greater than the previous height
            # pop the top index from the stack and calculate the amount of water trapped
            x = stack[-1]
            stack.pop()
            if len(stack) != 0:
                # calculate the distance between the two walls
                dist = i - stack[-1] - 1
                # calculate the height of the smaller wall
                temp = min(height[stack[-1]], height[i])
                # calculate the amount of water trapped
                water += dist * (temp - height[x])
                water_coords.append(water)
    st.code(water_coords)

    
    # return the total amount of water trapped
    return water

# test the function
assert trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6


def wordle_array(input_text):
    # split the input text into lines
    lines = input_text.split("\n")

    # extract the dimensions of the puzzle
    puzzle_lines = lines[2:]
    rows = len(puzzle_lines)
    cols = len(puzzle_lines[0])

    # create a 2D array to represent the puzzle, initialized to all 0s
    puzzle = [[0 for _ in range(cols)] for _ in range(rows)]

    # parse the puzzle from the input text
    for n, line in enumerate(puzzle_lines):
        for m, c in enumerate(line):
            if c != "⬛":
                # if the character is not black, set the corresponding cell to 1
                puzzle[n][m] = 1

    # return the puzzle as a list of lists
    return puzzle


def to_elevation_map(puzzle):
    elevation_map = []
    
    # for each column in the puzzle
    for col in range(len(puzzle[0])):
        # iterate from the top row to the bottom row
        for row in range(len(puzzle)):
            if puzzle[row][col] == 1:
                # if the cell is not black, add the height of the cell to the elevation map
                elevation_map.append(len(puzzle) - row)
                break
        else:
            # if the column is entirely black, add a height of 0 to the elevation map
            elevation_map.append(0)
    
    # return the elevation map as a list of heights
    return elevation_map

def calculate(input_text):
    st.write(trap(to_elevation_map(wordle_array(input_text))))


input_text = st.text_area('Paste your Wordle Score',"""Wordle 620 4/6

🟨⬛⬛⬛🟩
🟨⬛⬛⬛🟩
🟩🟩⬛🟩🟩
🟩🟩🟩🟩🟩""",200)

st.button("go",calculate(input_text))

# st.write(calculate(input_text))
for line in input_text.split("\n"):
    st.write(line)

# for line in wordle_array(input_text):
#     st.code(line)

st.code(to_elevation_map(wordle_array(input_text)))

# example usage

# input_text = """Wordle 620 4/6

# 🟨⬛⬛⬛🟩
# 🟨⬛⬛⬛🟩
# 🟩🟩⬛🟩🟩
# 🟩🟩🟩🟩🟩"""

# # parse the puzzle from the input text, convert it to an elevation map, and compute the amount of trapped water
# print(trap(to_elevation_map(wordle_array(input_text))))
