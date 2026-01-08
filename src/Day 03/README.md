# 📅 Day 03 - Recursion Continued

> _"Dividir para conquistar - a essência de toda recursão."_ 🗼

## 🎯 Objetivos do Dia

- [x] Continuar estudando Recursão
- [x] Resolver: Tower of Hanoi
- [x] Resolver: Power Sum (Peculiar Array)

---

## 📚 Conteúdo

| Arquivo                                        | Descrição                      |
| ---------------------------------------------- | ------------------------------ |
| [01_tower_of_hanoi.py](./01_tower_of_hanoi.py) | Clássico Tower of Hanoi        |
| [02_power_sum.py](./02_power_sum.py)           | Power Sum com arrays aninhados |

---

## 🧩 Problemas Resolvidos

### 1️⃣ Tower of Hanoi

**Problema:** Mover N discos do rod A para rod C, usando B como auxiliar.

**Regras:**

- Só move 1 disco por vez
- Disco maior não pode ficar em cima de menor

| N discos | Movimentos |
| -------- | ---------- |
| 1        | 1          |
| 2        | 3          |
| 3        | 7          |
| n        | 2ⁿ - 1     |

**Algoritmo:**

```
hanoi(n, A→C):
  1. hanoi(n-1, A→B)    # Move n-1 para auxiliar
  2. Move disco n: A→C  # Move o maior
  3. hanoi(n-1, B→C)    # Move n-1 para destino
```

| Complexidade | Valor |
| ------------ | ----- |
| Tempo        | O(2ⁿ) |
| Espaço       | O(n)  |

---

### 2️⃣ Power Sum (Peculiar Array)

**Problema:** Soma de array onde elementos aninhados são elevados à potência do nível.

**Exemplos:**

```
[2, 3, [4, 1, 2]] = 2 + 3 + (4+1+2)² = 54
[1, [2, [3]]] = 1 + (2 + 3³)² = 1 + 29² = 842
```

| Complexidade | Valor               |
| ------------ | ------------------- |
| Tempo        | O(n)                |
| Espaço       | O(d) - profundidade |

---

## 💡 Principais Aprendizados

1. **Tower of Hanoi** é o exemplo clássico de "dividir para conquistar"
2. A fórmula **2ⁿ - 1** aparece frequentemente em problemas recursivos
3. **Recursão com profundidade** requer passar o nível como parâmetro
4. Arrays aninhados podem ser processados **recursivamente**

---

## 🚀 Como Executar

```bash
# Tower of Hanoi
python 01_tower_of_hanoi.py

# Power Sum
python 02_power_sum.py
```

---

_Parte do [DSA 55 Days Bootcamp](../../README.md) 🚀_
