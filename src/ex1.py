def add_element_list(elem: int):
    vector: int = list()
    vector.append(elem)
    return vector

def show_elements(vectors: list):
    for i, j in enumerate(vectors, start=1):
        print(f'{i}º {j}')

def main():
    print('===Create Interger Vectors===')
    ask = int(input("Add[1] or show[2]: "))
    if ask==1:
        for i in range(10):
            try:
                print(F'Less {10-i}') if i !=10 else print('Last one!')
                elem: int = int(input('Write a number: '))
                vector = add_element_list(elem)
            except Exception as err:
                print(f'Erro: {str(err)}')
    if ask==2:
        try:
            show_elements(vector) if vector else print("The vector don't hava anyone element!")
        except Exception as err:
            print(f'Error: {err}')

if __name__=='__main__':
    main()
