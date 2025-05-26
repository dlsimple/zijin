# zijin
最大相似三角形

# 数学题： 三角形 ab, bc, ac 的边长平方分别为 ab2=2, bc2=4, ac2=10
# 在一个步长为1， 长度为n的正方形格子，求最大的相似三角形的的面积

Python 3.13.3

## 示例

![示例](example.png)

This code is a Python program designed to find and visualize a triangle on a grid, given the squares of its three side lengths and the size of the grid. The user is prompted to input four integers: the squares of the three triangle sides (ab², bc², ac²) and the grid size n. The program then attempts to find a triangle with integer coordinates on an n x n grid that matches these side lengths.

The core logic involves several helper functions. put_next_max_ac and pop_max_ac manage a dictionary of candidate points for one triangle vertex, always working with the largest possible squared distance first. judge_square_sum checks if a given number can be written as the sum of two squares, with each square not exceeding n², ensuring the triangle's sides can be represented on the grid. judge_valid_triangle tries to find a valid integer coordinate for the second vertex, given the constraints of the triangle's side lengths and the position of the third vertex.

The main search is performed in max_similar_triangle, which iteratively tries possible positions for the triangle's vertices, scaling the triangle as needed, and checking if the side lengths and positions are valid. If a valid triangle is found, its coordinates are returned.

The draw_triangle function uses the plotext library to plot the triangle on the terminal, labeling axes and drawing the triangle based on the calculated coordinates. The main function handles user input, error checking, and orchestrates the search and drawing process in a loop, allowing repeated attempts until the user exits.

Overall, the program combines mathematical checks with a search strategy to find and display triangles with given side lengths on a discrete grid, providing immediate visual feedback in the terminal.


