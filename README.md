# Xush kelibsiz  
# Matnni kesish (String Slicing)

Uy vazifalari va testlarni avtomatlashtirilgan baholash  
- Ushbu repozitoriyani fork qiling  
- Vazifani yeching  
- To‘g‘ri xabar bilan commit qiling  

# Masalalar  

---

## Slicing01  

  `s` matn o‘zgaruvchisi berilgan. Matnning boshidan to‘rtta belgi qaytarilsin.  

**Misol 1:**  

```Python
Kiritish: a="itmarkaz"  
Natija: "itma"  
```

**Misol 2:**  

```Python
Kiritish: a="code"  
Natija: "code"  
```

**Cheklovlar:**  
  - 4 <= uzunlik(a) <= 10^5  

---

## Slicing02  

  `s` matn o‘zgaruvchisi berilgan. Matnning oxiridan to‘rtta belgi qaytarilsin.  

**Misol 1:**  

```Python
Kiritish: a="itmarkaz"  
Natija: "rkaz"  
```

**Misol 2:**  

```Python
Kiritish: a="python"  
Natija: "thon"  
```

**Cheklovlar:**  
  - 4 <= uzunlik(a) <= 10^5  

---

## Slicing03  

  `s` matn o‘zgaruvchisi berilgan. Matnning boshidan va oxiridan boshqa barcha belgilarni qaytarilsin.  

**Misol 1:**  

```Python
Kiritish: a="itmarkaz"  
Natija: "tmarka"  
```

**Misol 2:**  

```Python
Kiritish: a="hello"  
Natija: "ell"  
```

**Cheklovlar:**  
  - 2 <= uzunlik(a) <= 10^5  

---

## Slicing04  

  `s` matn o‘zgaruvchisi berilgan. Matnning boshidan `n` ta belgi qaytarilsin.  

**Misol 1:**  

```Python
Kiritish: a="itmarkaz", n=3  
Natija: "itm"  
```

**Misol 2:**  

```Python
Kiritish: a="positive", n=2  
Natija: "po"  
```

**Cheklovlar:**  
  - 2 <= uzunlik(a) <= 10^5  
  - 1 <= n <= uzunlik(a)  

---

## Slicing05  

  `s` matn o‘zgaruvchisi berilgan. Matnning oxiridan `n` ta belgi qaytarilsin.  

**Misol 1:**  

```Python
Kiritish: a="itmarkaz", n=3  
Natija: "kaz"  
```

**Misol 2:**  

```Python
Kiritish: a="positive", n=1  
Natija: "e"  
```

**Cheklovlar:**  
  - 2 <= uzunlik(a) <= 10^5  
  - 1 <= n <= uzunlik(a)  

---

## Slicing06  

  `s` matn o‘zgaruvchisi berilgan. Matnning boshidan `n` ta belgi olib tashlanib, qolgan qismi qaytarilsin.  

**Misol 1:**  

```Python
Kiritish: a="itmarkaz", n=3  
Natija: "arkaz"  
```

**Misol 2:**  

```Python
Kiritish: a="apple", n=1  
Natija: "pple"  
```

**Cheklovlar:**  
  - 2 <= uzunlik(a) <= 10^5  
  - 1 <= n <= uzunlik(a)  

---

## Slicing07  

  `s` matn o‘zgaruvchisi berilgan. Matnning oxiridan `n` ta belgi olib tashlanib, qolgan qismi qaytarilsin.  

**Misol 1:**  

```Python
Kiritish: a="itmarkaz", n=3  
Natija: "itmar"  
```

**Misol 2:**  

```Python
Kiritish: a="apple", n=1  
Natija: "appl"  
```

**Cheklovlar:**  
  - 2 <= uzunlik(a) <= 10^5  
  - 1 <= n <= uzunlik(a)  

---

## Slicing08  

  `s` matn o‘zgaruvchisi berilgan. Toq o‘rinlardagi belgilarni qaytarilsin.  

**Misol 1:**  

```Python
Kiritish: a="itmarkaz"  
Natija: "imra"  
```

**Misol 2:**  

```Python
Kiritish: a="apple"  
Natija: "pl"  
```

**Cheklovlar:**  
  - 2 <= uzunlik(a) <= 10^5  

---

## Slicing09  

  `s` matn o‘zgaruvchisi berilgan. Juft o‘rinlardagi belgilarni qaytarilsin.  

**Misol 1:**  

```Python
Kiritish: a="itmarkaz"  
Natija: "trakz"  
```

**Misol 2:**  

```Python
Kiritish: a="apple"  
Natija: "ape"  
```

**Cheklovlar:**  
  - 2 <= uzunlik(a) <= 10^5  

---

## Slicing10  

  `s` matn o‘zgaruvchisi berilgan. `n` dan `k` gacha bo‘lgan indekslardagi belgilarni qaytarilsin.  

**Misol 1:**  

```Python
Kiritish: a="itmarkaz", n=2, k=5  
Natija: "mark"  
```

**Misol 2:**  

```Python
Kiritish: a="apple", n=2, k=2  
Natija: "p"  
```

**Cheklovlar:**  
  - 2 <= uzunlik(a) <= 10^5  
  - 0 <= n <= uzunlik(a)  
  - n <= k <= uzunlik(a)  

---

