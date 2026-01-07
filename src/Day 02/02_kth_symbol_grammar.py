"""
🎯 K-th Symbol in Grammar

📋 Problema:
Construímos uma tabela de n linhas (1-indexed).
- Linha 1: "0"
- Cada linha subsequente: substituímos 0→01 e 1→10

Exemplo:
    Row 1: 0
    Row 2: 01
    Row 3: 0110
    Row 4: 01101001

Dado n e k, retorne o k-ésimo símbolo (1-indexed) na n-ésima linha.

📊 Exemplos:
    n=1, k=1 → 0
    n=2, k=1 → 0
    n=2, k=2 → 1
    n=3, k=3 → 1

💡 Insight Chave:
- Cada linha tem 2^(n-1) elementos
- A primeira metade é igual à linha anterior
- A segunda metade é o COMPLEMENTO da linha anterior (0↔1)
"""


# ============================================================
# SOLUÇÃO 1: Força Bruta (Gerar toda a string)
# ============================================================
def kth_symbol_brute_force(n: int, k: int) -> int:
    """
    Gera a string completa e retorna o k-ésimo caractere.
    
    ⚠️ PROBLEMA: Memória explode! Row n tem 2^(n-1) caracteres
    Para n=30, são 2^29 = 536 milhões de caracteres!
    
    Complexidade:
        - Tempo: O(2^n)
        - Espaço: O(2^n)
    """
    if n == 1:
        return 0
    
    row = "0"
    for _ in range(n - 1):
        new_row = ""
        for char in row:
            if char == "0":
                new_row += "01"
            else:
                new_row += "10"
        row = new_row
    
    return int(row[k - 1])


# ============================================================
# SOLUÇÃO 2: Recursão com Padrão (Otimizada) ⭐
# ============================================================
def kth_symbol_recursive(n: int, k: int) -> int:
    """
    Usa o padrão: primeira metade = linha anterior, segunda metade = complemento da linha anterior
    
    Recurrence Relation:
    - Se k está na primeira metade: kthGrammar(n, k) = kthGrammar(n-1, k)
    - Se k está na segunda metade: kthGrammar(n, k) = 1 - kthGrammar(n-1, k - mid)
    
    Complexidade:
        - Tempo: O(n) - uma chamada por linha
        - Espaço: O(n) - profundidade da call stack
    """
    # Caso base: primeira linha sempre é "0"
    if n == 1:
        return 0
    
    # Quantidade de elementos na linha n
    length = 2 ** (n - 1)
    mid = length // 2
    
    if k <= mid:
        # k está na PRIMEIRA metade → igual à linha anterior
        return kth_symbol_recursive(n - 1, k)
    else:
        # k está na SEGUNDA metade → complemento da posição correspondente
        return 1 - kth_symbol_recursive(n - 1, k - mid)


# ============================================================
# SOLUÇÃO 3: Contar Bits (Matemática Pura) ⭐⭐
# ============================================================
def kth_symbol_bit_count(n: int, k: int) -> int:
    """
    Observação matemática:
    O k-ésimo símbolo é 0 se (k-1) tem número PAR de bits 1,
    e é 1 se (k-1) tem número ÍMPAR de bits 1.
    
    Isso porque cada "1" no binário de (k-1) representa
    uma vez que fomos para a segunda metade (complemento).
    
    Complexidade:
        - Tempo: O(log k) - contar bits
        - Espaço: O(1)
    """
    # Conta quantos bits 1 existem em (k-1)
    ones = bin(k - 1).count('1')
    
    # Se número de 1s é par → retorna 0, senão → retorna 1
    return ones % 2


# ============================================================
# VISUALIZAÇÃO DO PADRÃO
# ============================================================
def visualize_pattern(max_n: int = 5):
    """Mostra o padrão das primeiras linhas."""
    print("📊 Visualização do Padrão:\n")
    print("Row 1: 0")
    
    row = "0"
    for n in range(2, max_n + 1):
        new_row = ""
        for char in row:
            new_row += "01" if char == "0" else "10"
        row = new_row
        
        mid = len(row) // 2
        first_half = row[:mid]
        second_half = row[mid:]
        
        print(f"Row {n}: {first_half} | {second_half}")
        print(f"       {''.join(str(1-int(c)) for c in first_half)}   (complemento)")
    
    print("\n💡 Note: Segunda metade = complemento da primeira!")


# ============================================================
# TESTES
# ============================================================
if __name__ == "__main__":
    print("🧪 Testando K-th Symbol in Grammar\n")
    print("=" * 60)
    
    # Visualiza o padrão primeiro
    visualize_pattern(5)
    
    print("\n" + "=" * 60)
    print("\n🔍 Casos de Teste:\n")
    
    test_cases = [
        (1, 1, 0),   # Row 1: "0"
        (2, 1, 0),   # Row 2: "01"
        (2, 2, 1),   # Row 2: "01"
        (3, 1, 0),   # Row 3: "0110"
        (3, 3, 1),   # Row 3: "0110"
        (4, 5, 1),   # Row 4: "01101001"
    ]
    
    for n, k, expected in test_cases:
        result_recursive = kth_symbol_recursive(n, k)
        result_bit = kth_symbol_bit_count(n, k)
        
        status = "✅" if result_recursive == expected else "❌"
        print(f"{status} n={n}, k={k} → {result_recursive} (expected: {expected})")
        
        if result_recursive != result_bit:
            print(f"   ⚠️ Bit count deu diferente: {result_bit}")
    
    print("\n" + "=" * 60)
    print("🎉 Testes concluídos!")
