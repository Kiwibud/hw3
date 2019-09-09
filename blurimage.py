
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
def box(m: list, center: tuple) -> list:
    py, px = center[0], center[1]
    m = m if isinstance(m[py], list) else [m]
    output = []
    for y in range(max(py - 1, 0), min(py + 2, len(m))):
        row = m[y]
        row_len = len(row)
        output.append(row[max(px - 1, 0):min(px + 2, row_len)])
    return output


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
