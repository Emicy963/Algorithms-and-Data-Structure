"""
🎯 Permutations

📋 Problema:
Dado um array nums de inteiros DISTINTOS, retorne todas as permutações possíveis.

📊 Exemplos:
    Input: [1, 2, 3]
    Output: [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
    
    Input: [0, 1]
    Output: [[0,1], [1,0]]
    
    Input: [1]
    Output: [[1]]

💡 Insight:
- Total de permutações = n!
- Cada posição pode ter n, n-1, n-2, ... 1 escolhas
- Usamos backtracking para explorar todas as possibilidades

🌳 Árvore de Decisões para [1,2,3]:
                    []
           /        |        \
         [1]       [2]       [3]
        /   \     /   \     /   \
     [1,2] [1,3] [2,1] [2,3] [3,1] [3,2]
       |     |     |     |     |     |
   [1,2,3][1,3,2][2,1,3][2,3,1][3,1,2][3,2,1]
"""

from typing import List


# ============================================================
# SOLUÇÃO 1: Backtracking com Set para tracking
# ============================================================
def permute_with_set(nums: List[int]) -> List[List[int]]:
    """
    Usa um set para rastrear elementos já usados.
    
    Complexidade:
        - Tempo: O(n! × n) - n! permutações, O(n) para copiar cada
        - Espaço: O(n) - profundidade da recursão + set
    """
    resultado = []
    usado = set()
    
    def backtrack(caminho: List[int]):
        # Caso base: permutação completa
        if len(caminho) == len(nums):
            resultado.append(caminho[:])  # IMPORTANTE: cópia!
            return
        
        for num in nums:
            if num in usado:
                continue  # Pula elementos já usados
            
            # ESCOLHA
            caminho.append(num)
            usado.add(num)
            
            # EXPLORA
            backtrack(caminho)
            
            # DESFAZ (backtrack)
            caminho.pop()
            usado.remove(num)
    
    backtrack([])
    return resultado


# ============================================================
# SOLUÇÃO 2: Backtracking com Swap (in-place) ⭐
# ============================================================
def permute_swap(nums: List[int]) -> List[List[int]]:
    """
    Usa swap para gerar permutações in-place.
    Mais eficiente em espaço, não precisa de set.
    
    Ideia: fixa cada elemento na posição atual e recursa no resto.
    
    Complexidade:
        - Tempo: O(n! × n)
        - Espaço: O(n) - apenas a call stack
    """
    resultado = []
    
    def backtrack(start: int):
        # Caso base: processamos todas as posições
        if start == len(nums):
            resultado.append(nums[:])
            return
        
        for i in range(start, len(nums)):
            # ESCOLHA: coloca nums[i] na posição start
            nums[start], nums[i] = nums[i], nums[start]
            
            # EXPLORA: fixa a posição start e recursa
            backtrack(start + 1)
            
            # DESFAZ: restaura o array original
            nums[start], nums[i] = nums[i], nums[start]
    
    backtrack(0)
    return resultado


# ============================================================
# SOLUÇÃO 3: Usando itertools (Pythonica)
# ============================================================
from itertools import permutations as itertools_permutations

def permute_itertools(nums: List[int]) -> List[List[int]]:
    """
    Solução usando biblioteca padrão do Python.
    Ótima para produção, mas não para entrevistas!
    """
    return [list(p) for p in itertools_permutations(nums)]


# ============================================================
# VISUALIZAÇÃO
# ============================================================
def permute_with_trace(nums: List[int]) -> List[List[int]]:
    """Versão com trace para visualizar o processo."""
    resultado = []
    usado = set()
    
    def backtrack(caminho: List[int], depth: int = 0):
        indent = "  " * depth
        print(f"{indent}→ caminho={caminho}, usado={usado}")
        
        if len(caminho) == len(nums):
            print(f"{indent}✅ Encontrou: {caminho}")
            resultado.append(caminho[:])
            return
        
        for num in nums:
            if num in usado:
                print(f"{indent}  ⏭️ Pulando {num} (já usado)")
                continue
            
            print(f"{indent}  + Escolhe {num}")
            caminho.append(num)
            usado.add(num)
            
            backtrack(caminho, depth + 1)
            
            print(f"{indent}  - Backtrack: remove {num}")
            caminho.pop()
            usado.remove(num)
    
    backtrack([])
    return resultado


# ============================================================
# TESTES
# ============================================================
if __name__ == "__main__":
    print("🔄 Permutations\n")
    print("=" * 60)
    
    # Teste básico
    nums = [1, 2, 3]
    print(f"Input: {nums}")
    print(f"Expected: 3! = 6 permutações\n")
    
    result1 = permute_with_set(nums)
    result2 = permute_swap(nums[:])  # Passa cópia pq modifica in-place
    result3 = permute_itertools(nums)
    
    print("Resultados:")
    for perm in result1:
        print(f"  {perm}")
    
    print(f"\n✅ Set method: {len(result1)} permutações")
    print(f"✅ Swap method: {len(result2)} permutações")
    print(f"✅ Itertools: {len(result3)} permutações")
    
    # Verifica se são iguais (ordem pode diferir)
    assert sorted(map(tuple, result1)) == sorted(map(tuple, result2))
    assert sorted(map(tuple, result1)) == sorted(map(tuple, result3))
    
    print("\n" + "=" * 60)
    print("\n🔬 Trace para [1, 2]:\n")
    permute_with_trace([1, 2])
    
    print("\n" + "=" * 60)
    print("\n📊 Tabela de Permutações:\n")
    print("| n | Permutações (n!) |")
    print("|---|------------------|")
    for n in range(1, 9):
        import math
        print(f"| {n} | {math.factorial(n):14} |")
    
    print("\n" + "=" * 60)
    print("🎉 Testes concluídos!")
