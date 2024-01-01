def distance(arr1, arr2):
    """
    Find similarity using the Levenshtein Distance arr1 and arr2
    rows: m: one
    colm: n: two
    """
    m = len(arr1)
    n = len(arr2)

    # initialise
    arr = [[-1 for i in range(n+1)] for j in range(m+1)]
    for i in range(m+1):
        arr[i][0] = i
    for i in range(n+1):
        arr[0][i] = i

    # iterate over taking 2x2 matrix at a time
    for i in range(m):
        for j in range(n):
            values = [arr[i][j], arr[i][j+1], arr[i+1][j], arr[i+1][j+1]]
            min_value = min(values[:-1])
            val = -1
            if arr1[i] == arr2[j]:
                arr[i+1][j+1] = min_value
            else:
                arr[i+1][j+1] = min_value + 1
    
    # distance
    return arr[-1][-1]
