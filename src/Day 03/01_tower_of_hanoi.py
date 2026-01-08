"""
🎯 Tower of Hanoi

📋 Problema:
Temos 3 hastes (rods) e N discos. O objetivo é mover toda a pilha do rod 1 para o rod 3.

Regras:
1. Só pode mover 1 disco por vez
2. Um disco maior NÃO pode ficar em cima de um menor
3. Discos começam no rod 1, devem terminar no rod 3

📊 Exemplos:
    N=1: Move disco 1 de A para C
         Total: 1 movimento
    
    N=2: Move disco 1 de A para B
         Move disco 2 de A para C
         Move disco 1 de B para C
         Total: 3 movimentos
    
    N=3: Total: 7 movimentos

💡 Fórmula: Movimentos = 2^n - 1

🧠 Intuição Recursiva:
Para mover n discos de A para C usando B como auxiliar:
1. Move n-1 discos de A para B (usando C como auxiliar)
2. Move o disco n (maior) de A para C
3. Move n-1 discos de B para C (usando A como auxiliar)
"""


def tower_of_hanoi(n: int, source: str = 'A', auxiliary: str = 'B', destination: str = 'C') -> int:
    """
    Resolve Tower of Hanoi e imprime todos os movimentos.
    
    Args:
        n: Número de discos
        source: Haste de origem (padrão 'A')
        auxiliary: Haste auxiliar (padrão 'B')
        destination: Haste de destino (padrão 'C')
    
    Returns:
        Total de movimentos realizados
    
    Complexidade:
        - Tempo: O(2^n) - cada disco dobra o trabalho
        - Espaço: O(n) - profundidade da call stack
    """
    # Caso base: apenas 1 disco
    if n == 1:
        print(f"Move disco 1 de {source} para {destination}")
        return 1
    
    moves = 0
    
    # Passo 1: Move n-1 discos de source para auxiliary
    moves += tower_of_hanoi(n - 1, source, destination, auxiliary)
    
    # Passo 2: Move o disco n (maior) de source para destination
    print(f"Move disco {n} de {source} para {destination}")
    moves += 1
    
    # Passo 3: Move n-1 discos de auxiliary para destination
    moves += tower_of_hanoi(n - 1, auxiliary, source, destination)
    
    return moves


def tower_of_hanoi_with_state(n: int) -> int:
    """
    Versão que mostra o estado das hastes após cada movimento.
    """
    # Estado inicial: todos os discos em A
    rods = {
        'A': list(range(n, 0, -1)),  # [n, n-1, ..., 2, 1]
        'B': [],
        'C': []
    }
    moves = 0
    
    def print_state():
        print(f"  A: {rods['A']}")
        print(f"  B: {rods['B']}")
        print(f"  C: {rods['C']}")
        print()
    
    def move(num_disks, source, aux, dest):
        nonlocal moves
        
        if num_disks == 1:
            # Move o disco do topo
            disk = rods[source].pop()
            rods[dest].append(disk)
            moves += 1
            print(f"Passo {moves}: Move disco {disk} de {source} para {dest}")
            print_state()
            return
        
        # Recursão
        move(num_disks - 1, source, dest, aux)
        move(1, source, aux, dest)
        move(num_disks - 1, aux, source, dest)
    
    print("Estado inicial:")
    print_state()
    
    move(n, 'A', 'B', 'C')
    
    return moves


def hanoi_moves_only(n: int) -> int:
    """
    Retorna apenas o número de movimentos (sem prints).
    Usa a fórmula: 2^n - 1
    
    Complexidade: O(1)
    """
    return (2 ** n) - 1


# ============================================================
# VISUALIZAÇÃO - Árvore de Recursão
# ============================================================
def visualize_recursion_tree(n: int, source: str = 'A', aux: str = 'B', dest: str = 'C', depth: int = 0):
    """Mostra a árvore de chamadas recursivas."""
    indent = "  " * depth
    
    if n == 1:
        print(f"{indent}└─ hanoi(1, {source}→{dest}) = Move disco 1")
        return
    
    print(f"{indent}┌─ hanoi({n}, {source}→{dest})")
    visualize_recursion_tree(n - 1, source, dest, aux, depth + 1)
    print(f"{indent}│  Move disco {n} de {source} para {dest}")
    visualize_recursion_tree(n - 1, aux, source, dest, depth + 1)


# ============================================================
# TESTES
# ============================================================
if __name__ == "__main__":
    print("🗼 Tower of Hanoi\n")
    print("=" * 60)
    
    # Teste com 3 discos mostrando estado
    print("\n📍 Exemplo com N=3 (mostrando estado):\n")
    total = tower_of_hanoi_with_state(3)
    print(f"✅ Total de movimentos: {total}")
    print(f"📐 Fórmula 2^n - 1 = {hanoi_moves_only(3)}")
    
    print("\n" + "=" * 60)
    print("\n🌳 Árvore de Recursão para N=3:\n")
    visualize_recursion_tree(3)
    
    print("\n" + "=" * 60)
    print("\n📊 Tabela de Movimentos:\n")
    print("| N discos | Movimentos (2^n - 1) |")
    print("|----------|----------------------|")
    for n in range(1, 11):
        print(f"|    {n:2}    |      {hanoi_moves_only(n):7}         |")
    
    print("\n" + "=" * 60)
    print("🎉 Testes concluídos!")
