# 📅 Day 01 - Arrays & Big O Analysis

> _"Toda jornada de mil milhas começa com o primeiro passo."_ - Lao Tzu

## 🎯 Objetivos do Dia

- [x] Aprender Análise de Complexidade (Big O)
- [x] Entender a estrutura de dados Array
- [x] Resolver: Sorted Squared Array
- [x] Resolver: Monotonic Array

---

## 📚 Conteúdo

| Arquivo                                                    | Descrição                               |
| ---------------------------------------------------------- | --------------------------------------- |
| [01_big_o_analysis.md](./01_big_o_analysis.md)             | Análise de complexidade e notação Big O |
| [02_arrays.md](./02_arrays.md)                             | Crash course sobre Arrays               |
| [03_sorted_squared_array.py](./03_sorted_squared_array.py) | Solução do problema Sorted Squared      |
| [04_monotonic_array.py](./04_monotonic_array.py)           | Solução do problema Monotonic Array     |

---

## 🧩 Problemas Resolvidos

### 1️⃣ Sorted Squared Array

**Problema:** Dado um array ordenado, retorne um novo array com os quadrados ordenados.

| Abordagem       | Tempo      | Espaço |
| --------------- | ---------- | ------ |
| Força Bruta     | O(n log n) | O(n)   |
| Two Pointers ⭐ | O(n)       | O(n)   |

### 2️⃣ Monotonic Array

**Problema:** Verificar se um array é monotonicamente crescente ou decrescente.

| Abordagem           | Tempo | Espaço |
| ------------------- | ----- | ------ |
| Flags               | O(n)  | O(1)   |
| Direction Detection | O(n)  | O(1)   |
| Pythonic            | O(n)  | O(n)   |
| Zip ⭐              | O(n)  | O(1)   |

---

## 💡 Principais Aprendizados

1. **Big O** nos ajuda a comparar algoritmos independente do hardware
2. **Two Pointers** é um padrão poderoso para arrays ordenados
3. Arrays negativos elevados ao quadrado podem inverter a ordem
4. Python tem formas elegantes de resolver problemas com `zip()` e `all()`

---

## 🚀 Como Executar

```bash
# Testar Sorted Squared Array
python 03_sorted_squared_array.py

# Testar Monotonic Array
python 04_monotonic_array.py
```

---

_Parte do [DSA 50 Days Challenge](../README.md) 🚀_
