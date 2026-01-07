# 📅 Day 02 - Recursion Fundamentals

> _"Para entender recursão, primeiro você precisa entender recursão."_ 🔄

## 🎯 Objetivos do Dia

- [x] Aprender os fundamentos de Recursão
- [x] Entender Recursion Tree e Call Stack
- [x] Comparar Recursion vs Iteration
- [x] Resolver: K-th Symbol in Grammar
- [x] Resolver: Josephus Problem

---

## 📚 Conteúdo

| Arquivo                                                        | Descrição                   |
| -------------------------------------------------------------- | --------------------------- |
| [01_recursion_fundamentals.md](./01_recursion_fundamentals.md) | Teoria completa de recursão |
| [02_kth_symbol_grammar.py](./02_kth_symbol_grammar.py)         | K-th Symbol in Grammar      |
| [03_josephus_problem.py](./03_josephus_problem.py)             | Josephus Problem            |

---

## 🧩 Conceitos Chave

### 🔑 Os 3 Componentes da Recursão

1. **Base Case** - Condição de parada
2. **Recursive Call** - Função chama a si mesma
3. **Smaller Problem** - Cada chamada resolve problema menor

### 🦘 Leap of Faith

> Confie que a chamada recursiva vai funcionar!

---

## 🧩 Problemas Resolvidos

### 1️⃣ K-th Symbol in Grammar

**Problema:** Dado padrão onde `0→01` e `1→10`, encontre o k-ésimo símbolo na n-ésima linha.

| Abordagem            | Tempo    | Espaço |
| -------------------- | -------- | ------ |
| Brute Force          | O(2ⁿ)    | O(2ⁿ)  |
| Recursive Pattern ⭐ | O(n)     | O(n)   |
| Bit Counting ⭐⭐    | O(log k) | O(1)   |

**Insight:** A segunda metade é o complemento da primeira!

### 2️⃣ Josephus Problem

**Problema:** N pessoas em círculo, a cada k contagens uma é eliminada. Quem sobrevive?

| Abordagem    | Tempo | Espaço |
| ------------ | ----- | ------ |
| Simulação    | O(n²) | O(n)   |
| Recursivo    | O(n)  | O(n)   |
| Iterativo ⭐ | O(n)  | O(1)   |

**Fórmula:** `J(n) = (J(n-1) + k) % n`

---

## 💡 Principais Aprendizados

1. **Caso base** é crucial - sem ele, Stack Overflow!
2. **Leap of Faith** - confie na recursão para subproblemas
3. **Visualize** a árvore de recursão antes de codificar
4. **Iterativo** geralmente usa menos memória
5. **Padrões matemáticos** podem simplificar recursões complexas

---

## 🚀 Como Executar

```bash
# Testar K-th Symbol in Grammar
python 02_kth_symbol_grammar.py

# Testar Josephus Problem
python 03_josephus_problem.py
```

---

_Parte do [DSA 55 Days Bootcamp](../../README.md) 🚀_
