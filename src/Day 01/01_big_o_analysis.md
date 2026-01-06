# 📊 Big O Analysis - Complexity Analysis

## 🎯 Por que precisamos de Análise de Complexidade?

Quando escrevemos código, precisamos saber **quão eficiente** ele é. Dois algoritmos podem resolver o mesmo problema, mas um pode ser **1000x mais rápido** que o outro!

> 💡 **Analogia:** Imagine procurar um nome numa lista telefônica. Você pode ir página por página (lento) ou abrir no meio e decidir se o nome está antes ou depois (rápido). Ambos funcionam, mas a eficiência é muito diferente!

---

## ⏱️ O que é Time Complexity (Complexidade de Tempo)?

É uma forma de medir **quantas operações** um algoritmo executa conforme o tamanho da entrada cresce.

- Não medimos em segundos (isso depende do hardware)
- Medimos em **número de operações** relativas ao tamanho da entrada `n`

---

## 📈 O que é Big O?

**Big O** é a notação matemática que descreve o **pior caso** de crescimento de um algoritmo.

```
O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ) < O(n!)
```

### Complexidades Comuns

| Notação    | Nome         | Exemplo                     |
| ---------- | ------------ | --------------------------- |
| O(1)       | Constante    | Acessar elemento por índice |
| O(log n)   | Logarítmica  | Binary Search               |
| O(n)       | Linear       | Loop simples                |
| O(n log n) | Linearítmica | Merge Sort, Quick Sort      |
| O(n²)      | Quadrática   | Loop aninhado               |
| O(2ⁿ)      | Exponencial  | Fibonacci recursivo         |

---

## 💾 Space Complexity (Complexidade de Espaço)

Mede **quanta memória extra** o algoritmo usa.

```python
# O(1) espaço - só variáveis fixas
def soma(a, b):
    return a + b

# O(n) espaço - cria array proporcional à entrada
def duplicar_array(arr):
    return [x * 2 for x in arr]
```

---

## 🔧 Técnicas para Simplificar Big O

1. **Ignore constantes:** O(2n) → O(n)
2. **Ignore termos menores:** O(n² + n) → O(n²)
3. **Considere o pior caso**
4. **Logaritmos:** Quando dividimos o problema pela metade a cada passo

---

## 📝 Logaritmos Explicados

```
log₂(8) = 3  →  2³ = 8
log₂(16) = 4 →  2⁴ = 16
```

> 🧠 **Dica:** Se você divide o problema pela metade repetidamente, a complexidade é O(log n)

---

## ✅ Resumo do Dia

- Big O descreve a **eficiência** do algoritmo
- Time Complexity = operações executadas
- Space Complexity = memória utilizada
- Sempre considere o **pior caso**
- Logaritmos aparecem quando dividimos pela metade

---

_Dia 1 - DSA 50 Days Challenge 🚀_
