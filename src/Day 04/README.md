# 📅 Day 04 - Backtracking: Permutations

> _"Backtracking é a arte de explorar todas as possibilidades, descartando as inválidas cedo."_ 🔙

## 🎯 Objetivos do Dia

- [x] Aprender fundamentos de Backtracking
- [x] Entender a diferença entre Recursão e Backtracking
- [x] Resolver: Permutations (elementos distintos)
- [x] Resolver: Permutations II (com duplicados)

---

## 📚 Conteúdo

| Arquivo                                                              | Descrição                          |
| -------------------------------------------------------------------- | ---------------------------------- |
| [01_backtracking_fundamentals.md](./01_backtracking_fundamentals.md) | Teoria de Backtracking             |
| [02_permutations.py](./02_permutations.py)                           | Permutações de elementos distintos |
| [03_permutations_2.py](./03_permutations_2.py)                       | Permutações com duplicados         |

---

## 🧩 Conceitos Chave

### 📋 Blueprint do Backtracking

```python
def backtrack(candidato):
    if é_solução(candidato):
        salvar(candidato[:])
        return

    for escolha in escolhas:
        fazer_escolha(escolha)      # Choose
        backtrack(candidato)         # Explore
        desfazer_escolha(escolha)   # Unchoose
```

### ⚠️ Armadilha Comum

```python
# ❌ ERRADO - referência
resultado.append(caminho)

# ✅ CERTO - cópia
resultado.append(caminho[:])
```

---

## 🧩 Problemas Resolvidos

### 1️⃣ Permutations

**Problema:** Gerar todas as permutações de elementos DISTINTOS.

| Abordagem        | Descrição                        |
| ---------------- | -------------------------------- |
| Set tracking     | Usa set para rastrear usados     |
| Swap in-place ⭐ | Troca elementos sem espaço extra |

| Complexidade | Valor     |
| ------------ | --------- |
| Tempo        | O(n! × n) |
| Espaço       | O(n)      |

---

### 2️⃣ Permutations II

**Problema:** Gerar permutações ÚNICAS quando há duplicados.

**Truque:** Ordena + Poda

```python
if i > 0 and nums[i] == nums[i-1] and not usado[i-1]:
    continue  # Pula duplicado
```

| Abordagem      | Descrição                        |
| -------------- | -------------------------------- |
| Array usado ⭐ | Ordena + poda duplicados         |
| Counter        | Conta ocorrências de cada número |

---

## 💡 Principais Aprendizados

1. **Backtracking = Recursão + Desfazer escolhas**
2. **Sempre faça cópia** ao salvar resultado
3. **Duplicados?** Ordene e pule consecutivos iguais
4. **Swap** é mais eficiente em espaço
5. **Visualize a árvore** de decisões antes de codificar

---

## 🚀 Como Executar

```bash
# Permutations
python 02_permutations.py

# Permutations II
python 03_permutations_2.py
```

---

_Parte do [DSA 55 Days Bootcamp](../../README.md) 🚀_
