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
    # print(box([5], (0, 0))) #Crash the program


# user sum and len and a comprehension
def average_matrix(m):
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
def box(m, center):
    grid = []
    if len(m) == 0:
        return None
    if len(m) == 1:
        i, j = 0, 0
    else:
        i = center[0]
        j = center[1]
    if j-1 >= 0:
        # check if row 1 of the box exist
        if i-1 >= 0:
            # check for right limit
            g1 = m[i-1][j-1:j+2] if j+1 < len(m[0]) else m[i-1][j-1:j+1]
            grid.append(g1)  # append row 1
        g2 = m[i][j-1:j+2] if j+1 < len(m[0]) else m[i][j-1:j+1]
        grid.append(g2)  # append row 2
        if i+1 < len(m):
            g3 = m[i+1][j-1:j+2] if j+1 < len(m[0]) else m[i+1][j-1:j+1]
            grid.append(g3)  # append row 3
    else:
        if i-1 >= 0:
            g1 = m[i-1][j:j+2] if j+1 < len(m[0]) else m[i-1][j:j+1]
            grid.append(g1)
        g2 = m[i][j:j+2] if j+1 < len(m[0]) else m[i][j:j+1]
        grid.append(g2)
        if i+1 < len(m):
            g3 = m[i+1][j:j+2] if j+1 < len(m[0]) else m[i+1][j:j+1]
            grid.append(g3)

    return grid


# return integer, invoke average and box function
# returns a nested list representing the blurred image.
def blur(image):
    print()


if __name__ == "__main__":
    main()
