# 📚 Arrays - Crash Course

## 🎯 O que é um Array?

Um **Array** é uma estrutura de dados que armazena elementos do **mesmo tipo** em posições **contíguas** de memória.

> 💡 **Analogia:** Pense num array como um **trem** 🚂 - cada vagão (índice) guarda um passageiro (valor), e você pode ir diretamente ao vagão 5 sem passar pelos anteriores!

---

## 🔑 Características Principais

| Característica | Descrição                           |
| -------------- | ----------------------------------- |
| **Índice**     | Começa em 0                         |
| **Acesso**     | O(1) - Direto por índice            |
| **Tamanho**    | Fixo (Static) ou Dinâmico (Dynamic) |
| **Memória**    | Contígua                            |

---

## 📦 Static Arrays vs Dynamic Arrays

### Static Arrays (Arrays Estáticos)

- Tamanho **fixo** definido na criação
- Não podem crescer ou encolher
- Usados em linguagens como C, C++, Java (array primitivo)
- Mais eficientes em memória

### Dynamic Arrays (Arrays Dinâmicos)

- Tamanho pode **mudar** durante a execução
- Python `list`, JavaScript `Array`, Java `ArrayList`
- Quando cheio, cria novo array maior e copia elementos → **O(n)**
- Inserção no final precisa de **shifting** (deslocamento) de elementos

---

## ⚡ Big O das Operações em Arrays

Esta é a tabela mais importante para entender a eficiência de cada operação:

| Operação                       | Tempo (T) | Espaço (S) | Explicação                                        |
| ------------------------------ | --------- | ---------- | ------------------------------------------------- |
| **Access** (acesso por índice) | O(1)      | O(1)       | Acesso direto pela fórmula: `base + index * size` |
| **Set** (atribuir valor)       | O(1)      | O(1)       | Mesmo que access, só muda o valor                 |
| **Traverse/Search** (busca)    | O(n)      | O(1)       | Precisa verificar cada elemento                   |
| **Copy**                       | O(n)      | O(n)       | Copia todos os n elementos                        |

### 📥 Inserção (Insert)

| Posição       | Tempo (T) | Espaço (S) | Por quê?                                         |
| ------------- | --------- | ---------- | ------------------------------------------------ |
| **No início** | O(n)      | O(1)       | Precisa deslocar TODOS os elementos para direita |
| **No final**  | O(1)\*    | O(1)       | Só adiciona no fim (amortizado)                  |
| **No meio**   | O(n)      | O(1)       | Precisa deslocar parte dos elementos             |

> ⚠️ \*Amortizado: ocasionalmente O(n) quando array dinâmico precisa realocar

### 🗑️ Remoção (Remove)

| Posição       | Tempo (T) | Espaço (S) | Por quê?                                          |
| ------------- | --------- | ---------- | ------------------------------------------------- |
| **No início** | O(n)      | O(1)       | Precisa deslocar TODOS os elementos para esquerda |
| **No final**  | O(1)      | O(1)       | Só remove o último                                |
| **No meio**   | O(n)      | O(1)       | Precisa deslocar parte dos elementos              |

---

## 🔄 Visualizando o Shifting (Deslocamento)

```
Inserir 'X' no início de [A, B, C]:

Passo 1: [A, B, C, _]     # Abre espaço
Passo 2: [_, A, B, C]     # Desloca todos → O(n)
Passo 3: [X, A, B, C]     # Insere X

Remover 'A' do início de [A, B, C]:

Passo 1: [_, B, C]        # Remove A
Passo 2: [B, C, _]        # Desloca todos ← O(n)
Passo 3: [B, C]           # Array final
```

> 🧠 **Insight:** É por isso que inserir/remover no início é O(n)! Precisamos mover todos os outros elementos.

---

## 🐍 Arrays em Python (Lists)

```python
# Criando arrays
numeros = [1, 2, 3, 4, 5]
vazio = []
misto = [1, "texto", 3.14]  # Python permite tipos mistos

# Acessando elementos - O(1)
primeiro = numeros[0]   # 1
ultimo = numeros[-1]    # 5

# Modificando (Set) - O(1)
numeros[0] = 10         # [10, 2, 3, 4, 5]

# Tamanho - O(1)
tamanho = len(numeros)  # 5
```

---

## 🛠️ Métodos e suas Complexidades

```python
arr = [3, 1, 4, 1, 5, 9]

# ✅ O(1) - Operações rápidas
arr.append(2)           # Adiciona no final
arr.pop()               # Remove do final
arr[0]                  # Acesso por índice

# ⚠️ O(n) - Operações lentas
arr.insert(0, 0)        # Insere no início (shift!)
arr.pop(0)              # Remove do início (shift!)
arr.remove(1)           # Busca + remove (busca é O(n))
5 in arr                # Busca linear

# 📊 O(n log n) - Ordenação
arr.sort()              # Ordena in-place
sorted(arr)             # Retorna nova lista ordenada

# 🔄 O(n) - Operações que percorrem tudo
arr.copy()              # Copia array
arr.reverse()           # Reverte in-place
arr[::-1]               # Retorna nova lista revertida
```

---

## 🎨 Padrões Comuns com Arrays

### Two Pointers (Dois Ponteiros)

```python
# Verificar se array é palíndromo - O(n) tempo, O(1) espaço
def is_palindrome(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        if arr[left] != arr[right]:
            return False
        left += 1
        right -= 1
    return True
```

### Sliding Window (Janela Deslizante)

```python
# Soma máxima de subarray de tamanho k - O(n) tempo
def max_sum_subarray(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum
```

---

## 📊 Resumo Visual das Complexidades

```
┌─────────────────────────────────────────────────────────┐
│                    ARRAY OPERATIONS                      │
├─────────────────────────────────────────────────────────┤
│  Access/Set      │  O(1)  │  ████████████  Excelente!   │
│  Search          │  O(n)  │  ████         Linear        │
│  Insert (end)    │  O(1)  │  ████████████  Excelente!   │
│  Insert (start)  │  O(n)  │  ████         Evitar!       │
│  Remove (end)    │  O(1)  │  ████████████  Excelente!   │
│  Remove (start)  │  O(n)  │  ████         Evitar!       │
└─────────────────────────────────────────────────────────┘
```

---

## ✅ Quando Usar Arrays?

✅ **Use quando:**

- Precisa de acesso rápido por índice → O(1)
- Ordem dos elementos importa
- Tamanho é conhecido ou muda pouco
- Inserções/remoções são principalmente no **final**

❌ **Evite quando:**

- Muitas inserções/remoções no **início ou meio** → use LinkedList
- Tamanho muda muito frequentemente
- Precisa de busca rápida por valor → use Set ou Dict (Hash Table)

---

## 💡 Dicas para Entrevistas

1. **Sempre pergunte:** Array ordenado ou não? (muda a complexidade!)
2. **Two Pointers** resolve muitos problemas de array ordenado
3. **Cuidado com shifting:** inserir/remover no início é O(n)
4. **Prefira append/pop** ao invés de insert(0)/pop(0)
5. **Lembre:** Python lists são dynamic arrays por baixo dos panos

---

_Dia 1 - DSA 55 Days Bootcamp 🚀_
