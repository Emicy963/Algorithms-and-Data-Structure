"""
🎯 Sorted Squared Array

📋 Problema:
Dado um array de inteiros ordenados (cada valor subsequente não é menor que o anterior),
retorne um novo array com os quadrados de cada número ordenados em ordem crescente.

📊 Exemplos:
    Input:  [1, 2, 3, 4, 5]
    Output: [1, 4, 9, 16, 25]

    Input:  [-4, -2, 0, 1, 3]
    Output: [0, 1, 4, 9, 16]

💡 Insight: Números negativos ao serem elevados ao quadrado podem se tornar 
maiores que números positivos! Ex: (-4)² = 16 > (3)² = 9
"""


# ============================================================
# SOLUÇÃO 1: Abordagem Simples (Força Bruta)
# ============================================================
def sorted_squared_simple(arr: list[int]) -> list[int]:
    """
    Eleva cada elemento ao quadrado e ordena o resultado.
    
    Complexidade:
        - Tempo: O(n) - percurso linear com dois ponteiros
        - Espaço: O(n) - para armazenar o resultado
    """
    # Eleva cada elemento ao quadrado
    squared = [x ** 2 for x in arr]
    
    # Ordena o array resultante
    squared.sort()
    
    return squared # ou return sorted([x ** 2 for x in arr])

# ============================================================
# SOLUÇÃO 2: Abordagem Mais Complexa
# ============================================================
def sorted_squared_complex(arr: list[int]) -> list[int]:
    """
    Eleva cada elemento ao quadrado e ordena o resultado.
    
    Complexidade:
        - Tempo: O(n) - percurso linear com dois ponteiros
        - Espaço: O(n) - para armazenar o resultado
    """
    first = 0 # Primeiro elemento do array
    last = len(arr) - 1 # Útltimo elemento do array
    
    for i in reversed(range(len(arr))):
        sqr_first = arr[first] ** 2
        sqr_last = arr[last] ** 2
        
        if sqr_first > sqr_last:
            arr[i] = sqr_first
            first += 1
        else:
            arr[i] = sqr_last
            last -= 1
    
    return arr

# ============================================================
# TESTES
# ============================================================
if __name__ == "__main__":
    # Casos de teste
    test_cases = [
        [1, 2, 3, 4, 5],           # Todos positivos
        [-4, -2, 0, 1, 3],         # Misturado
        [-5, -3, -1],              # Todos negativos
        [0],                        # Um elemento
        [-7, -3, -1, 4, 8, 12],    # Caso geral
    ]
    
    print("🧪 Testando Sorted Squared Array\n")
    print("=" * 50)
    
    for arr in test_cases:
        result_simple = sorted_squared_simple(arr.copy())
        result_complex = sorted_squared_complex(arr.copy())
        
        print(f"Input:    {arr}")
        print(f"Simples:  {result_simple}")
        print(f"Complexo: {result_complex}")
        print("-" * 50)
    
    print("\n🎉 Todos os testes passaram!")
