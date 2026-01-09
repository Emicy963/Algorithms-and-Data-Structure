# 🔙 Backtracking - Fundamentos

## 🎯 O que é Backtracking?

**Backtracking** é uma técnica algorítmica que constrói soluções **incrementalmente** e **abandona** (backtrack) uma solução assim que determina que não pode levar a uma solução válida.

> 💡 **Analogia:** Imagine um labirinto 🏰 - você explora um caminho, e quando encontra um beco sem saída, **volta** e tenta outro caminho. Isso é backtracking!

---

## 🆚 Backtracking vs Recursão

| Aspecto          | Recursão                         | Backtracking                     |
| ---------------- | -------------------------------- | -------------------------------- |
| **Objetivo**     | Dividir problema em subproblemas | Explorar todas as possibilidades |
| **Estrutura**    | Chama a si mesma                 | Recursão + desfaz escolhas       |
| **Resultado**    | Uma solução                      | Múltiplas soluções (ou a melhor) |
| **Quando parar** | Caso base                        | Caso base + condições de poda    |

```python
# RECURSÃO simples
def fatorial(n):
    if n <= 1:
        return 1
    return n * fatorial(n - 1)

# BACKTRACKING
def permutacoes(nums, caminho, resultado):
    if len(caminho) == len(nums):
        resultado.append(caminho[:])  # Encontrou solução
        return

    for num in nums:
        if num in caminho:
            continue  # PODA - ignora inválidos

        caminho.append(num)           # ESCOLHA
        permutacoes(nums, caminho, resultado)
        caminho.pop()                 # BACKTRACK - desfaz escolha
```

---

## ⚙️ Como Backtracking Funciona?

### Os 3 Passos Essenciais:

```
1. ESCOLHA (Choose)    → Toma uma decisão
2. EXPLORA (Explore)   → Recursa para explorar essa escolha
3. DESFAZ (Unchoose)   → Backtrack - desfaz a escolha
```

```python
def backtrack(estado_atual):
    if é_solução(estado_atual):
        salvar_solução(estado_atual)
        return

    for escolha in escolhas_possíveis:
        if é_válida(escolha):
            fazer_escolha(escolha)      # 1. ESCOLHA
            backtrack(estado_atual)      # 2. EXPLORA
            desfazer_escolha(escolha)    # 3. DESFAZ (backtrack)
```

---

## 📦 Pass by Reference / Change Inplace

⚠️ **Cuidado importante em Python!**

```python
# ❌ ERRADO - passa a mesma referência
resultado.append(caminho)  # Todos apontam pro mesmo objeto!

# ✅ CERTO - cria uma cópia
resultado.append(caminho[:])     # Slicing cria cópia
resultado.append(caminho.copy()) # Método copy
resultado.append(list(caminho))  # Construtor
```

**Visualização do problema:**

```python
caminho = [1, 2, 3]
resultado = []
resultado.append(caminho)  # resultado = [[1,2,3]]
caminho.pop()
caminho.append(4)
# resultado agora é = [[1,2,4]] 😱 Mudou!
```

---

## 📋 Blueprint para Resolver com Backtracking

```python
def solve(problem):
    resultado = []

    def backtrack(candidato):
        # 1. Caso base - encontrou solução?
        if é_solução_completa(candidato):
            resultado.append(candidato[:])  # Salva CÓPIA
            return

        # 2. Gera todas as escolhas possíveis
        for próxima_escolha in gerar_escolhas():

            # 3. Poda - verifica se escolha é válida
            if não_é_válida(próxima_escolha):
                continue

            # 4. Faz a escolha
            fazer_escolha(candidato, próxima_escolha)

            # 5. Recursa
            backtrack(candidato)

            # 6. Desfaz a escolha (BACKTRACK!)
            desfazer_escolha(candidato, próxima_escolha)

    backtrack(estado_inicial)
    return resultado
```

---

## 🎯 Quando Usar Backtracking?

✅ **Use quando:**

- Precisa encontrar **todas** as soluções possíveis
- Problema é de **combinação/permutação**
- Problema pode ser modelado como **árvore de decisões**
- Existe **restrição** que permite podar ramos inválidos

### Problemas Clássicos:

| Problema        | Tipo                          |
| --------------- | ----------------------------- |
| Permutações     | Arranjo de elementos          |
| Subsets         | Combinação de elementos       |
| N-Queens        | Posicionamento com restrições |
| Sudoku Solver   | Preencher com restrições      |
| Word Search     | Busca em grid                 |
| Combination Sum | Soma com restrições           |

---

## 🌳 Visualização: Árvore de Decisões

Para permutações de `[1, 2, 3]`:

```
                    []
           /        |        \
         [1]       [2]       [3]
        /   \     /   \     /   \
     [1,2] [1,3] [2,1] [2,3] [3,1] [3,2]
       |     |     |     |     |     |
   [1,2,3][1,3,2][2,1,3][2,3,1][3,1,2][3,2,1]
```

Cada caminho da raiz até uma folha = uma permutação válida!

---

## ⚡ Complexidade

Para problemas de permutação:

- **Tempo:** O(n! × n) - n! permutações, cada uma leva O(n) para copiar
- **Espaço:** O(n) para a call stack + O(n! × n) para armazenar resultados

---

## 💡 Dicas para Entrevistas

1. **Identifique o padrão:** É permutação, combinação ou subset?
2. **Desenhe a árvore** de decisões primeiro
3. **Identifique as restrições** para poda
4. **Lembre da cópia:** `resultado.append(caminho[:])`
5. **Duplicados?** Ordene e pule elementos iguais consecutivos

---

_Dia 4 - DSA 55 Days Bootcamp 🚀_
