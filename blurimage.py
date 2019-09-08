
import copy


def main():
    m = [[1, 2, 0],
        [4, 0, 5],
        [7, 3, 9],
        [0, 8, 0]]
    print(average_matrix(m))
    print(average_matrix([[5]]))
    print(average_matrix([[]]))
    print(box(m, (0, 0)))
    print(box(m, (2, 1)))
    print(box(m, (3, 1)))
    # print(box([5], (0, 0)))
    image = [[168, 168, 170, 172, 174, 158, 154, 170],
             [172, 126, 109, 86, 72, 72, 95, 129],
             [146, 152, 165, 183, 176, 177, 178, 176],
             [181, 153, 80, 57, 79, 57, 29, 23],
             [29, 34, 19, 28, 38, 39, 15, 26],
             [14, 21, 18, 21, 21, 18, 24, 25]]
    print(blur(image))
    print(image)
    print(blur(m))
    print(m)


# user sum and len and a comprehension
def average_matrix(m):
    """

    :param m:
    :return:
    """
    row = len(m)
    col = len(m[0])
    total = 0
    if row == 0 or col == 0:
        return None
    else:
        for i in m:
            total += sum(i)
        return total / (row*col)


# min, max, list slice, list comprehension
# def box(m, center):
#     """

#     :param m:
#     :param center:
#     :return:
#     """
#     grid = []
#     if len(m) == 0:
#         return None
#     if len(m) == 1:
#         i, j = 0, 0
#     else:
#         i = center[0]
#         j = center[1]
#     if j-1 >= 0:
#         # check if row 1 of the box exist
#         if i-1 >= 0:
#             # check for right limit
#             g1 = m[i-1][j-1:j+2] if j+1 < len(m[0]) else m[i-1][j-1:j+1]
#             grid.append(g1)  # append row 1
#         g2 = m[i][j-1:j+2] if j+1 < len(m[0]) else m[i][j-1:j+1]
#         grid.append(g2)  # append row 2
#         if i+1 < len(m):
#             g3 = m[i+1][j-1:j+2] if j+1 < len(m[0]) else m[i+1][j-1:j+1]
#             grid.append(g3)  # append row 3
#     else:
#         if i-1 >= 0:
#             g1 = m[i-1][j:j+2] if j+1 < len(m[0]) else m[i-1][j:j+1]
#             grid.append(g1)
#         g2 = m[i][j:j+2] if j+1 < len(m[0]) else m[i][j:j+1]
#         grid.append(g2)
#         if i+1 < len(m):
#             g3 = m[i+1][j:j+2] if j+1 < len(m[0]) else m[i+1][j:j+1]
#             grid.append(g3)

#     return grid


# min, max, list slice, list comprehension
def box(m: list, center: tuple) -> list:
    py, px = center[0], center[1]
    m = m if isinstance(m[py], list) else [m]
    output = []
    for y in range(max(py - 1, 0), min(py + 2, len(m))):
        row = m[y]
        row_len = len(row)
        output.append(row[max(px - 1, 0):min(px + 2, row_len)])
    return output


def box2(m, center):
    y, x = center[0], center[1]  # Prof stated these are always valid
    m = m if type(m[y]) == list else [m]  # Wrap single-array as 2D.
    output = []
    # Ternary operators -- handling out of bounds checking.
    range_y = 1 + (y if y >= len(m) - 1 else y + 1)
    for y in range(0 if y <= 0 else y - 1, range_y):
        output.append(get_row2(m, x, y))
    return output


# Retrieves up to three elements from a center point within a row.
def get_row2(matrix: list, x: int, y: int) -> list:
    row = []
    # No need to check bounds here -- already done in 'box()'
    range_x = 1 + (x if x >= len(matrix[y]) - 1 else x + 1)
    for x in range(0 if x <= 0 else x - 1, range_x):
        row.append(matrix[y][x])
    return row


# return integer, invoke average and box function
# returns a nested list representing the blurred image.
def blur(image):
    """

    :param image:
    :return:
    """
    result = copy.deepcopy(image)
    for i in range(len(image)):
        for j in range(len(image[0])):
            submatrix = box(image, (i, j))
            average = round(average_matrix(submatrix))
            result[i][j] = average
    return result


if __name__ == "__main__":
    main()
