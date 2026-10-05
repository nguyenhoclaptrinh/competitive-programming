# ICPC 2024 Northern Provincial - Problem L: EQPAIR

- **Problem Link:** [VNOI - icpc24_mb_l](https://oj.vnoi.info/problem/icpc24_mb_l)
- **Time Limit:** 0.5s
- **Memory Limit:** 256 MB

---

## Problem Statement

Given a sequence of $n$ integers $a_1, a_2, \dots, a_n$. Count the number $Q$ of pairs of indices $(i, j)$ such that:
$$1 \le i < j \le n \quad \text{and} \quad a_i = a_j$$

## Input

- Line 1: A positive integer $n$ ($1 \le n \le 100\,000$).
- Line 2: $n$ integers $a_1, a_2, \dots, a_n$ ($1 \le a_i \le 1\,000\,000$).

## Output

- Print $Q \pmod{10^9 + 7}$.

---

## Examples

### Sample 1

**Input:**
```text
6
1 2 2 1 3 1
```

**Output:**
```text
4
```

**Explanation:**
The 4 pairs are:
1. $(1, 4)$ where $a_1 = a_4 = 1$
2. $(1, 6)$ where $a_1 = a_6 = 1$
3. $(2, 3)$ where $a_2 = a_3 = 2$
4. $(4, 6)$ where $a_4 = a_6 = 1$

---

## Approach & Complexity

- Count the occurrence frequency of each number using a direct frequency array of size $\max(a_i) + 1 \le 1\,000\,001$.
- If an element appears $k$ times, the number of valid pairs formed is $\frac{k \times (k - 1)}{2}$.
- Sum up $\frac{k \times (k - 1)}{2} \pmod{10^9 + 7}$ across all distinct values.
- **Time Complexity:** $O(n + \max(a_i))$
- **Space Complexity:** $O(\max(a_i))$
