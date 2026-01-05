from random import randint
from ex1 import add_element_list

def sum_elements(vector: list):
    return sum(vector)

def main():
    print("===Somador de Números===")
    num=randint(0, 100)
    try:
        for _ in range(num):
            vector = add_element_list(randint(0, 100))
        print(f'A soma dos inteiros: {vector} é: {sum_elements(vector)}')
    except Exception as err:
        print(f'Erro: {str(err)}')
