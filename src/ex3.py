from ex1 import add_element_list, show_elements
from ex2 import sum_elements
from random import randint

def vector_avarage(vector: list)->int:
    return (sum_elements(vector)/len(vector))

def main():
    print("===Somador de Números===")
    num=randint(0, 100)
    try:
        for _ in range(num):
            vector = add_element_list(randint(0, 20))
        num_high_avarage = list(map(lambda x: x>vector_avarage(vector), vector))
        print(f'A média dos valores é de {len(vector)} é: {vector_avarage(vector)}')
        print(f'\nOs valores acima dessa média são:')
        show_elements(sorted(num_high_avarage))
    except Exception as err:
        print(f'Erro: {str(err)}')

