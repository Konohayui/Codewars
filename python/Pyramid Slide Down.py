def longest_slide_down(pyramid):
    # TODO: write some code...
    for row in range(len(pyramid) - 1, 0, -1):
        for col in range(0, row):
            pyramid[row - 1][col] += max(pyramid[row][col], pyramid[row][col + 1])
    return pyramid[0][0]
