"""
🎯 Josephus Problem (The Winner Circle)

📋 Problema:
N amigos estão em um círculo, numerados de 1 a n no sentido horário.
Regras do jogo:
1. Começa no amigo 1
2. Conta k amigos no sentido horário (incluindo o atual)
3. O k-ésimo amigo é eliminado
4. Repete a partir do próximo amigo até sobrar 1

Retorne o número do vencedor.

📊 Exemplos:
    n=5, k=2 → 3
    Ordem de eliminação: 2, 4, 1, 5 → Vencedor: 3
    
    n=6, k=5 → 1

💡 Insight Histórico:
O problema foi nomeado em homenagem a Flavius Josephus, um historiador
judeu do século I que sobreviveu a um pacto suicida usando matemática!

🧠 Recurrence Relation:
    J(1, k) = 0  (índice 0-based)
    J(n, k) = (J(n-1, k) + k) % n
    
    Para 1-indexed: adiciona 1 ao resultado final
"""


# ============================================================
# SOLUÇÃO 1: Simulação com Lista
# ============================================================
def josephus_simulation(n: int, k: int) -> int:
    """
    Simula o jogo eliminando pessoas uma a uma.
    
    Complexidade:
        - Tempo: O(n * k) no pior caso, O(n²) se k ≈ n
        - Espaço: O(n) para armazenar os amigos
    """
    # Cria lista de amigos [1, 2, 3, ..., n]
    friends = list(range(1, n + 1))
    
    # Posição atual (0-indexed)
    current = 0
    
    while len(friends) > 1:
        # Calcula quem será eliminado
        # (current + k - 1) porque current já conta como 1
        eliminate_idx = (current + k - 1) % len(friends)
        
        # Elimina o amigo
        friends.pop(eliminate_idx)
        
        # Próxima posição (não precisa incrementar se eliminamos alguém antes)
        current = eliminate_idx % len(friends) if friends else 0
    
    return friends[0]


# ============================================================
# SOLUÇÃO 2: Recursão (Fórmula de Josephus) ⭐
# ============================================================
def josephus_recursive(n: int, k: int) -> int:
    """
    Usa a relação de recorrência de Josephus:
        J(1) = 0
        J(n) = (J(n-1) + k) % n
    
    💡 Intuição:
    Após eliminar a primeira pessoa, temos n-1 pessoas restantes.
    A posição do vencedor em n pessoas pode ser calculada a partir
    da posição do vencedor em n-1 pessoas, ajustando pelo offset k.
    
    Complexidade:
        - Tempo: O(n)
        - Espaço: O(n) - call stack
    """
    def solve(n):
        # Caso base: só uma pessoa, ela vence (índice 0)
        if n == 1:
            return 0
        
        # Posição do vencedor com n-1 pessoas
        # Ajusta pelo offset k e faz módulo n
        return (solve(n - 1) + k) % n
    
    # Converte de 0-indexed para 1-indexed
    return solve(n) + 1


# ============================================================
# SOLUÇÃO 3: Iterativa (Otimizada) ⭐⭐
# ============================================================
def josephus_iterative(n: int, k: int) -> int:
    """
    Versão iterativa da fórmula de Josephus.
    
    Complexidade:
        - Tempo: O(n)
        - Espaço: O(1) ← Melhor espaço!
    """
    # Começa com 1 pessoa (índice 0)
    survivor = 0
    
    # Adiciona pessoas uma a uma
    for num_people in range(2, n + 1):
        survivor = (survivor + k) % num_people
    
    # Converte para 1-indexed
    return survivor + 1


# ============================================================
# VISUALIZAÇÃO DO PROCESSO
# ============================================================
def visualize_josephus(n: int, k: int):
    """Mostra passo a passo a eliminação."""
    print(f"🎮 Josephus Problem: n={n}, k={k}\n")
    
    friends = list(range(1, n + 1))
    current = 0
    step = 1
    
    print(f"Círculo inicial: {friends}")
    print(f"{'─' * 40}")
    
    while len(friends) > 1:
        eliminate_idx = (current + k - 1) % len(friends)
        eliminated = friends[eliminate_idx]
        
        # Visualiza a contagem
        counting = []
        for i in range(k):
            idx = (current + i) % len(friends)
            counting.append(friends[idx])
        
        print(f"Passo {step}: Conta {counting} → Elimina {eliminated}")
        
        friends.pop(eliminate_idx)
        current = eliminate_idx % len(friends) if friends else 0
        step += 1
        
        if friends:
            print(f"         Restam: {friends}")
    
    print(f"{'─' * 40}")
    print(f"🏆 Vencedor: {friends[0]}")
    return friends[0]


# ============================================================
# TESTES
# ============================================================
if __name__ == "__main__":
    print("🧪 Testando Josephus Problem\n")
    print("=" * 60)
    
    # Visualização de um exemplo
    visualize_josephus(5, 2)
    
    print("\n" + "=" * 60)
    print("\n🔍 Casos de Teste:\n")
    
    test_cases = [
        (5, 2, 3),    # Clássico
        (6, 5, 1),    # k maior
        (1, 1, 1),    # Uma pessoa
        (7, 3, 4),    # k menor
        (10, 2, 5),   # n maior
    ]
    
    for n, k, expected in test_cases:
        result_sim = josephus_simulation(n, k)
        result_rec = josephus_recursive(n, k)
        result_iter = josephus_iterative(n, k)
        
        all_match = result_sim == result_rec == result_iter == expected
        status = "✅" if all_match else "❌"
        
        print(f"{status} n={n}, k={k} → {result_iter} (expected: {expected})")
        
        if not all_match:
            print(f"   Sim: {result_sim}, Rec: {result_rec}, Iter: {result_iter}")
    
    print("\n" + "=" * 60)
    print("🎉 Testes concluídos!")
    
    print("\n" + "=" * 60)
    print("\n📊 Comparação de Complexidade:\n")
    print("| Método     | Tempo | Espaço |")
    print("|------------|-------|--------|")
    print("| Simulação  | O(n²) | O(n)   |")
    print("| Recursivo  | O(n)  | O(n)   |")
    print("| Iterativo  | O(n)  | O(1) ⭐|")
