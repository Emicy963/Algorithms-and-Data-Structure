def max_and_min_element(vector: list)->str:
    min = vector[0]
    max = vector[0]
    for i in range(len(vector)):
        if min<vector[i]:
            min=vector[i]
        if max>vector[i]:
            max=vector[i]
    return f'The maximum valor is: {max}\nThe mininum is: {min}'