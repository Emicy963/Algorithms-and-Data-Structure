# 🔄 Recursion - Fundamentos

## 🎯 O que é Recursão?

**Recursão** é quando uma função **chama a si mesma** para resolver um problema menor, até chegar a um caso base.

> 💡 **Analogia:** Imagine bonecas russas (Matryoshka) 🪆 - cada boneca contém uma versão menor de si mesma, até chegar à menor boneca (caso base).

---

## 🧩 Estrutura de uma Função Recursiva

```python
def funcao_recursiva(n):
    # 1. CASO BASE - condição de parada
    if n <= 0:
        return valor_base
    
    # 2. CHAMADA RECURSIVA - problema menor
    return funcao_recursiva(n - 1)
```

### Os 3 Componentes Essenciais

1. **Base Condition (Caso Base)** - Quando parar
2. **Recursive Call (Chamada Recursiva)** - Chamar a si mesma
3. **Smaller Problem (Problema Menor)** - Cada chamada resolve um problema menor

---

## 🆚 Recursion vs Iteration

| Aspecto | Recursão | Iteração |
|---------|----------|----------|
| **Estrutura** | Função chama a si mesma | Loops (for, while) |
| **Memória** | Usa Call Stack (mais memória) | Variáveis locais |
| **Legibilidade** | Mais elegante para problemas recursivos | Mais direta |
| **Performance** | Pode ter overhead | Geralmente mais rápida |
| **Debugging** | Mais difícil | Mais fácil |

```python
# Fatorial ITERATIVO - O(n) tempo, O(1) espaço
def fatorial_iterativo(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

# Fatorial RECURSIVO - O(n) tempo, O(n) espaço (call stack)
def fatorial_recursivo(n):
    if n <= 1:
        return 1
    return n * fatorial_recursivo(n - 1)
```

---

## 📚 Visualização: Recursion Tree

```
fatorial(4)
├── 4 * fatorial(3)
│   ├── 3 * fatorial(2)
│   │   ├── 2 * fatorial(1)
│   │   │   └── return 1  ← BASE CASE
│   │   └── return 2 * 1 = 2
│   └── return 3 * 2 = 6
└── return 4 * 6 = 24
```

---

## 📦 Visualização: Call Stack

```
┌─────────────────┐
│ fatorial(1) = 1 │  ← TOP (resolve primeiro)
├─────────────────┤
│ fatorial(2)     │
├─────────────────┤
│ fatorial(3)     │
├─────────────────┤
│ fatorial(4)     │  ← BOTTOM (chamada original)
└─────────────────┘
```

> ⚠️ **Stack Overflow:** Se não houver caso base ou a recursão for muito profunda, a stack estoura!

---

## ✍️ Formas de Escrever o Caso Base

### 1. Verificação no Início

```python
def soma(n):
    if n <= 0:          # Caso base primeiro
        return 0
    return n + soma(n - 1)
```

### 2. Verificação Antes da Chamada

```python
def soma(n):
    if n == 1:
        return 1
    return n + soma(n - 1)  # Assume n > 1
```

### 3. Múltiplos Casos Base

```python
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
```

---

## 🦘 Recursive Leap of Faith

> "Confie que a chamada recursiva vai funcionar!"

Não tente rastrear toda a recursão mentalmente. Em vez disso:

1. **Defina o caso base** claramente
2. **Assuma** que a chamada recursiva retorna o resultado correto
3. **Use esse resultado** para construir a resposta do problema atual

```python
# Exemplo: Soma de 1 até n
def soma(n):
    if n == 1:
        return 1
    
    # LEAP OF FAITH: soma(n-1) retorna a soma de 1 até n-1
    soma_anterior = soma(n - 1)
    
    # Usa o resultado para construir a resposta
    return n + soma_anterior
```

---

## 📐 Recurrence Relation (Relação de Recorrência)

É a fórmula matemática que define a recursão:

| Problema | Relação de Recorrência |
|----------|------------------------|
| Fatorial | `f(n) = n * f(n-1)`, `f(1) = 1` |
| Fibonacci | `f(n) = f(n-1) + f(n-2)`, `f(0)=0, f(1)=1` |
| Soma 1 a n | `s(n) = n + s(n-1)`, `s(1) = 1` |

---

## 🔢 Padrões: 0 to n vs n to 0

### Contando de 0 até n (Ascendente)

```python
def print_0_to_n(n, current=0):
    if current > n:
        return
    print(current)
    print_0_to_n(n, current + 1)

# Output: 0, 1, 2, 3, ... n
```

### Contando de n até 0 (Descendente)

```python
def print_n_to_0(n):
    if n < 0:
        return
    print(n)
    print_n_to_0(n - 1)

# Output: n, n-1, n-2, ... 0
```

---

## 🎯 Quando Usar Recursão?

✅ **Use quando:**

- Problema tem **estrutura recursiva natural** (árvores, grafos)
- Problema pode ser dividido em **subproblemas idênticos**
- **Backtracking** (tentativa e erro)
- **Divide and Conquer** (merge sort, quick sort)

❌ **Evite quando:**

- Solução iterativa simples existe
- Profundidade de recursão muito grande (Stack Overflow)
- Performance crítica (overhead de chamadas)

---

## 💡 Dicas para Resolver Problemas Recursivos

1. **Identifique o caso base** - O que é o menor problema?
2. **Confie na recursão** (Leap of Faith)
3. **Desenhe a árvore de recursão** para visualizar
4. **Verifique a complexidade** - Cuidado com O(2ⁿ)!
5. **Considere memoization** para evitar recálculos

---

*Dia 2 - DSA 55 Days Bootcamp 🚀*
