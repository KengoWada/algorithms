def linear_search(arr, value):
    for i in range(0, len(arr)):
        if arr[i] == value:
            return i

    return -1


# Solution inspired by Dharanendra L V. from https://www.geeksforgeeks.org/linear-search/
def advanced_linear_search(arr, value):
    array_length = len(arr)
    right = array_length - 1

    for i in range(0, right, 1):

        if arr[i] == value:
            return i

        if arr[right] == value:
            return right

        right -= 1

    return -1


if __name__ == '__main__':

    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    x = 5
    y = 12

    # Linear Search
    print(linear_search(arr, x))
    print(linear_search(arr, y))

    # Adavanced Linear Search
    print(advanced_linear_search(arr, x))
    print(advanced_linear_search(arr, y))
