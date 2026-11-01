def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    d = [[0.0] * len(a) for z in range(len(a[0]))]
    for i in range(len(a[0])):
        for j in range(len(a)):

            d[i][j] = a[j][i]
    return d 

    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    pass