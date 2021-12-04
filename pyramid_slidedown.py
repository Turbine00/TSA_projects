# returns maximum sum of numbers sliding down the pyramid
input_pyramid = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]


def longest_slide_down(pyramid):
    for i in range(len(pyramid)-1):
        for m in range(len(pyramid[-i-2])):
            if pyramid[-i-1][m+1] >= pyramid[-i-1][m]:
                pyramid[-i-2][m] = pyramid[-i-1][m+1] + pyramid[-i-2][m]
            else:
                pyramid[-i - 2][m] = pyramid[-i-1][m] + pyramid[-i-2][m]

    return pyramid[0][0]


print(longest_slide_down(input_pyramid))
