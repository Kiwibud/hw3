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
    grid = [[1, 2, 0], [4, 0, 5], [7, 3, 9], [0, 8, 0]]
    image = [[168, 168, 170, 172, 174, 158, 154, 170],
             [172, 126, 109, 86, 72, 72, 95, 129],
             [146, 152, 165, 183, 176, 177, 178, 176],
             [181, 153, 80, 57, 79, 57, 29, 23],
             [29, 34, 19, 28, 38, 39, 15, 26],
             [14, 21, 18, 21, 21, 18, 24, 25]]
    print('Testing average_matrix')
    # average_matrix([[]])
    print(f'{average_matrix(grid): .2f}')
    # average_matrix([[5]])
    print('Testing box')
    print(box(grid, (0, 0)))
    print(box(grid, (3, 1)))
    print(box(grid, (2, 1)))
    print('Testing blur image')
    print(blur(image))


def average_matrix(m):
    """
    This function calculates the average value of all the element of
    a nested list (matrix)
    :param m:  the matrix that needs to be calculate the average value
    :return: (float) the average value of the matrix
    """
    # return None if matrix is empty
    if len(m) == 0 or len(m[0]) == 0:
        return None
    else:
        # sum of all values of the matrix
        total = sum([sum(m[i]) for i in range(len(m))])
        # total elements of the matrix
        total_element = len(m) * len(m[0])
        average = total / total_element
        # print(f"{average: .2f}")
        return average


def box(m, center):
    """
    This function get a matrix and a tuple as parameter
    to return the 3x3 submatrix centered about the tuple
    or a submatrix less than 3x3 if the tuple is at the egde
    :param m: matrix
    :param center: the tuple represents the row and column of the center
    :return: the submatrix that has the tuple as center or edge
    """
    # pass all the tests
    # built-in functions: min, max, list slices, and a comprehension
    if len(m) == 1:
        print([m])
    else:
        # max index should be less than the length of array 1 unit
        row_index_max = len(m) - 1
        col_index_max = len(m[0]) - 1
        row, col = center
        # adjust the stop position by adding 1
        col_start = get_range(0, col - 1, col_index_max)
        col_stop = get_range(0, col + 1, col_index_max) + 1
        row_start = get_range(0, row - 1, row_index_max)
        row_stop = get_range(0, row + 1, row_index_max) + 1
        new_m = [m[i][col_start: col_stop] for i in range(row_start, row_stop)]
        # print(new_m)
        return new_m


def get_range(low, center, high):
    """
    This function gets the neighbor position about the center
    :param low: the minimum index of the matrix
    :param center: the index of the neighbor of the center
    :param high: the maximum index of the matrix
    :return: the neighbor position of the center still within the matrix
    """
    return min(max(low, center), high)


def blur(image):
    blur_image = [[0 for col in range(len(image[0]))]
                  for row in range(len(image))]
    for row in range(len(blur_image)):
        for col in range(len(blur_image[row])):
            box_array = box(image, (row, col))
            average_val = round(average_matrix(box_array))
            blur_image[row][col] = average_val
    return blur_image


if __name__ == "__main__":
    main()
