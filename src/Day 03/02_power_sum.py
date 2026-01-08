"""
🎯 Power Sum (Peculiar Array)

📋 Problema:
Um "peculiar array" é um array onde cada elemento é:
- Um inteiro, OU
- Outro peculiar array (aninhado)

O valor equivalente de um array aninhado é:
(soma dos elementos)^(nível de aninhamento)

📊 Exemplos:
    [2, 3, [4, 1, 2]] = 2 + 3 + (4+1+2)^2
                      = 2 + 3 + 7^2
                      = 2 + 3 + 49
                      = 54
    
    [1, 2, [7, [3, 4], 2]] = 1 + 2 + (7 + (3+4)^3 + 2)^2
                           = 1 + 2 + (7 + 343 + 2)^2
                           = 1 + 2 + 352^2
                           = 1 + 2 + 123904
                           = 123907

💡 Insight:
- Nível 1 (raiz): sem exponenciação
- Nível 2 (primeiro aninhamento): ^2
- Nível 3 (segundo aninhamento): ^3
- E assim por diante...

🧠 Abordagem Recursiva:
1. Percorre cada elemento do array
2. Se for inteiro: adiciona à soma
3. Se for array: calcula recursivamente e eleva à potência do nível
"""

from typing import Union, List

# Tipo para representar o peculiar array
PeculiarArray = List[Union[int, 'PeculiarArray']]


def power_sum(arr: PeculiarArray, depth: int = 1) -> int:
    """
    Calcula a soma de um peculiar array.
    
    Args:
        arr: O peculiar array a ser processado
        depth: Nível de aninhamento atual (1 = raiz)
    
    Returns:
        A soma calculada com as potências aplicadas
    
    Complexidade:
        - Tempo: O(n) onde n é o total de elementos em todos os níveis
        - Espaço: O(d) onde d é a profundidade máxima de aninhamento
    """
    total = 0
    
    for element in arr:
        if isinstance(element, int):
            # Elemento é um inteiro: adiciona diretamente
            total += element
        else:
            # Elemento é um array: calcula recursivamente
            # e eleva à potência do próximo nível
            nested_sum = power_sum(element, depth + 1)
            total += nested_sum
    
    # Se não estamos na raiz, aplicamos a potência
    if depth > 1:
        return total ** depth
    
    return total


def power_sum_v2(arr: PeculiarArray) -> int:
    """
    Versão alternativa com helper function interna.
    """
    def calculate(arr: PeculiarArray, level: int) -> int:
        current_sum = 0
        
        for item in arr:
            if isinstance(item, list):
                # Array aninhado: calcula e eleva ao nível+1
                nested_result = calculate(item, level + 1)
                current_sum += nested_result ** (level + 1)
            else:
                # Número: soma diretamente
                current_sum += item
        
        return current_sum
    
    return calculate(arr, 0)


def power_sum_with_trace(arr: PeculiarArray, depth: int = 1, indent: int = 0) -> int:
    """
    Versão com trace para visualizar o processo.
    """
    prefix = "  " * indent
    print(f"{prefix}Processando nível {depth}: {arr}")
    
    total = 0
    
    for element in arr:
        if isinstance(element, int):
            print(f"{prefix}  + {element} (inteiro)")
            total += element
        else:
            print(f"{prefix}  + array aninhado:")
            nested_sum = power_sum_with_trace(element, depth + 1, indent + 2)
            result = nested_sum if depth == 0 else nested_sum
            print(f"{prefix}  = soma interna: {nested_sum}")
            total += nested_sum
    
    if depth > 1:
        powered = total ** depth
        print(f"{prefix}Soma {total}^{depth} = {powered}")
        return powered
    
    print(f"{prefix}Soma total: {total}")
    return total


# ============================================================
# TESTES
# ============================================================
if __name__ == "__main__":
    print("🔢 Power Sum (Peculiar Array)\n")
    print("=" * 60)
    
    # Casos de teste
    test_cases = [
        # (input, expected, description)
        ([1, 2, 3], 6, "Sem aninhamento"),
        ([2, 3, [4, 1, 2]], 54, "Um nível de aninhamento"),
        # [2, 3, [4, 1, 2]] = 2 + 3 + (4+1+2)^2 = 2 + 3 + 49 = 54
        
        ([[1, 2], 3], 12, "Array no início"),
        # [[1, 2], 3] = (1+2)^2 + 3 = 9 + 3 = 12
        
        ([1, [2, [3]]], 83, "Dois níveis de aninhamento"),
        # [1, [2, [3]]] = 1 + (2 + 3^3)^2 = 1 + (2 + 27)^2 = 1 + 29^2 = 1 + 841 = 842
        # WAIT: let me recalculate
        # depth=1: [1, [2, [3]]]
        #   - 1 é int: soma += 1
        #   - [2, [3]] é array, calcula com depth=2
        #     depth=2: [2, [3]]
        #       - 2 é int: soma += 2
        #       - [3] é array, calcula com depth=3
        #         depth=3: [3]
        #           - 3 é int: soma = 3
        #           retorna 3^3 = 27
        #       soma = 2 + 27 = 29
        #       retorna 29^2 = 841
        #   soma = 1 + 841 = 842
        # Hmm o expected está errado, vou corrigir
    ]
    
    # Corrigindo expected values
    test_cases = [
        ([1, 2, 3], 6, "Sem aninhamento"),
        ([2, 3, [4, 1, 2]], 54, "Um nível: 2+3+(4+1+2)²"),
        ([[1, 2], 3], 12, "Array no início: (1+2)²+3"),
        ([1, [2, [3]]], 842, "Dois níveis aninhados"),
    ]
    
    print("🔍 Casos de Teste:\n")
    
    for arr, expected, desc in test_cases:
        result = power_sum(arr)
        result_v2 = power_sum_v2(arr)
        
        status = "✅" if result == expected else "❌"
        print(f"{status} {desc}")
        print(f"   Input:    {arr}")
        print(f"   Expected: {expected}")
        print(f"   Got:      {result}")
        if result != result_v2:
            print(f"   ⚠️ V2:    {result_v2}")
        print()
    
    print("=" * 60)
    print("\n🔬 Trace do exemplo [2, 3, [4, 1, 2]]:\n")
    power_sum_with_trace([2, 3, [4, 1, 2]])
    
    print("\n" + "=" * 60)
    print("\n🔬 Trace do exemplo [1, [2, [3]]]:\n")
    power_sum_with_trace([1, [2, [3]]])
    
    print("\n" + "=" * 60)
    print("🎉 Testes concluídos!")
