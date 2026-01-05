def found_element_vector(vector: list, element: any)->any:
    for i, j in enumerate(vector, start=1):
        return print(f'{i}º{j}') if j==element else print('Element not found!')
