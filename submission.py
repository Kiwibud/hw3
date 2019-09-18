# ---------------------------------------------------------------------
# Name: Homework 3
# Purpose: Practice on nested list
# Author: Kiwibud
# ---------------------------------------------------------------------
"""
Practice on nested list

Get the average of the values in the input matrix
Center the input matrix about the input tuple
Gray scale an image using the average and center function
"""


def main():
    m = [[1, 2, 0],
         [4, 0, 5],
         [7, 3, 9],
         [0, 8, 0]]
    print("Testing average_matrix function")
    print(average_matrix(m))
    print(average_matrix([[5]]))
    print(average_matrix([[]]))
    print("Testing box function")
    print(box(m, (0, 0)))
    print(box(m, (2, 1)))
    print(box(m, (3, 1)))
    print(box([[5]], (0, 0)))
    image = [[168, 168, 170, 172, 174, 158, 154, 170],
             [172, 126, 109, 86, 72, 72, 95, 129],
             [146, 152, 165, 183, 176, 177, 178, 176],
             [181, 153, 80, 57, 79, 57, 29, 23],
             [29, 34, 19, 28, 38, 39, 15, 26],
             [14, 21, 18, 21, 21, 18, 24, 25]]
    print("Testing blur function")
    print(image)
    print("After blurring")
    print(blur(image))
    print(m)
    print("After blurring")
    print(blur(m))


def average_matrix(m):
    """
    This function calculates the average value of all the element of
    a nested list (matrix)
    :param m: (nested list) the matrix to calculate the average value
    :return: (float) the average value of the matrix
    """
    row = len(m)
    col = len(m[0])
    total = 0
    if row == 0 or col == 0:
        return None
    else:
        for i in m:
            total += sum(i)
    return total / (row * col)


def box(m: list, center: tuple) -> list:
    """
    This function gets a matrix and a tuple as parameter
    to return the 3x3 submatrix centered about the tuple
    or a submatrix less than 3x3 if the tuple is at the edge
    :param m: (nested list) original matrix
    :param center: (tuple) represents the row and column of the center
    :return: (nested list) the submatrix
    """
    py, px = center[0], center[1]
    m = m if isinstance(m[py], list) else [m]
    output = []
    for y in range(max(py - 1, 0), min(py + 2, len(m))):
        row = m[y]
        row_len = len(row)
        output.append(row[max(px - 1, 0):min(px + 2, row_len)])
    return output


def blur(image):
    """
    This function blurs an image using the box and average function
    :param image:(nested list) image that needs to be blurred
    :return:(nested list) blurred image
    """
    result = [[0 for col in range(len(image[0]))]
              for row in range(len(image))]
    for i in range(len(image)):
        for j in range(len(image[0])):
            submatrix = box(image, (i, j))
            average = round(average_matrix(submatrix))
            result[i][j] = average
    return result


if __name__ == "__main__":
    main()
