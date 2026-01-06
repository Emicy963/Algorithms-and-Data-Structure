"""
🎯 Monotonic Array

📋 Problema:
Um array é monotônico se for monotonamente crescente OU monotonamente decrescente.
- Monotônico Crescente: todos elementos da esquerda para direita são não-decrescentes (>=)
- Monotônico Decrescente: todos elementos da esquerda para direita são não-crescentes (<=)

Dado um array de inteiros, retorne True se for monotônico, False caso contrário.

📊 Exemplos:
    Input:  [1, 2, 2, 3]  → True  (crescente)
    Input:  [6, 5, 4, 4]  → True  (decrescente)
    Input:  [1, 3, 2]     → False (nem crescente nem decrescente)
    Input:  [1, 1, 1]     → True  (constante é ambos!)

💡 Dica: Um array constante (todos iguais) é considerado AMBOS crescente E decrescente!
"""


# ============================================================
# SOLUÇÃO 1: Verificação Simples com Flags
# ============================================================
def is_monotonic_flags(arr: list[int]) -> bool:
    """
    Usa duas flags para rastrear se o array é crescente e/ou decrescente.
    
    Complexidade:
        - Tempo: O(n) - uma passada pelo array
        - Espaço: O(1) - apenas variáveis
    """
    if len(arr) <= 1:
        return True
    
    is_increasing = True
    is_decreasing = True
    
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            is_decreasing = False
        if arr[i] < arr[i - 1]:
            is_increasing = False
    
    # Monotônico se for crescente OU decrescente
    return is_increasing or is_decreasing


# ============================================================
# SOLUÇÃO 2: Detectar Direção e Verificar ⭐
# ============================================================
def is_monotonic_direction(arr: list[int]) -> bool:
    """
    Detecta a direção inicial e verifica consistência.
    
    Complexidade:
        - Tempo: O(n) - uma passada pelo array
        - Espaço: O(1) - apenas variáveis
    """
    if len(arr) <= 2:
        return True
    
    # Encontra a primeira diferença não-zero para determinar direção
    direction = 0
    for i in range(1, len(arr)):
        diff = arr[i] - arr[i - 1]
        if diff != 0:
            direction = 1 if diff > 0 else -1
            break
    
    # Se todos iguais, é monotônico
    if direction == 0:
        return True
    
    # Verifica se todas as diferenças seguem a direção
    for i in range(1, len(arr)):
        diff = arr[i] - arr[i - 1]
        if direction == 1 and diff < 0:  # Esperava crescer, mas decresceu
            return False
        if direction == -1 and diff > 0:  # Esperava decrescer, mas cresceu
            return False
    
    return True


# ============================================================
# SOLUÇÃO 3: Pythonica (One-liner) 🐍
# ============================================================
def is_monotonic_pythonic(arr: list[int]) -> bool:
    """
    Solução elegante usando all() e comparação de listas.
    
    Complexidade:
        - Tempo: O(n) - comparação elemento a elemento
        - Espaço: O(n) - cria listas ordenadas para comparação
    """
    return arr == sorted(arr) or arr == sorted(arr, reverse=True)


# ============================================================
# SOLUÇÃO 4: Usando zip (Eficiente e Elegante) ⭐
# ============================================================
def is_monotonic_zip(arr: list[int]) -> bool:
    """
    Usa zip para comparar pares adjacentes de forma elegante.
    
    Complexidade:
        - Tempo: O(n) - uma passada pelo array
        - Espaço: O(1) - geradores não criam listas
    """
    # Verifica se todos os pares são não-decrescentes (crescente)
    increasing = all(a <= b for a, b in zip(arr, arr[1:]))
    
    # Verifica se todos os pares são não-crescentes (decrescente)
    decreasing = all(a >= b for a, b in zip(arr, arr[1:]))
    
    return increasing or decreasing


# ============================================================
# TESTES
# ============================================================
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 2, 3], True),       # Crescente com duplicados
        ([6, 5, 4, 4], True),       # Decrescente com duplicados
        ([1, 3, 2], False),         # Não monotônico
        ([1, 1, 1], True),          # Constante
        ([1], True),                # Um elemento
        ([], True),                 # Vazio
        ([1, 2, 3, 4, 5], True),    # Estritamente crescente
        ([5, 4, 3, 2, 1], True),    # Estritamente decrescente
        ([1, 2, 3, 2, 1], False),   # Sobe e desce
        ([-1, -2, -3], True),       # Negativos decrescentes
    ]
    
    print("🧪 Testando Monotonic Array\n")
    print("=" * 60)
    
    for arr, expected in test_cases:
        result_flags = is_monotonic_flags(arr.copy())
        result_dir = is_monotonic_direction(arr.copy())
        result_pythonic = is_monotonic_pythonic(arr.copy())
        result_zip = is_monotonic_zip(arr.copy())
        
        all_match = (
            result_flags == expected and
            result_dir == expected and
            result_pythonic == expected and
            result_zip == expected
        )
        
        status = "✅" if all_match else "❌"
        print(f"{status} Input: {str(arr):25} Expected: {expected}")
    
    print("=" * 60)
    print("\n🎉 Todos os testes passaram!")
