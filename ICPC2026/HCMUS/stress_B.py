import random
import subprocess
import os

def solve_naive(N, items):
    # items is list of (e, q)
    # We want to find max K
    # Filter items with q >= 4
    valid = [(e, q) for e, q in items if q >= 4]
    
    max_k = 0
    
    def backtrack(day, used):
        nonlocal max_k
        max_k = max(max_k, day - 1)
        
        # Try to form a meal for 'day'
        for i in range(len(valid)):
            if used & (1 << i): continue
            for j in range(i + 1, len(valid)):
                if used & (1 << j): continue
                
                ei, qi = valid[i]
                ej, qj = valid[j]
                
                if ei >= day and ej >= day and qi + qj >= 9:
                    # Valid meal
                    backtrack(day + 1, used | (1 << i) | (1 << j))

    backtrack(1, 0)
    return max_k

# Compile optimal solution
subprocess.run(["g++", "-O2", "B/B.cpp", "-o", "run_B"])

tests = 200
passed = 0

print("Stress testing Problem B (Freezer)...")
for t in range(tests):
    N = random.randint(1, 10)
    items = []
    for _ in range(N):
        e = random.randint(1, 10)
        q = random.randint(1, 10)
        items.append((e, q))
        
    naive_ans = solve_naive(N, items)
    
    # Run optimal
    inp = f"{N}\n"
    for e, q in items:
        inp += f"{e} {q}\n"
        
    res = subprocess.run(["./run_B"], input=inp, capture_output=True, text=True)
    opt_ans = int(res.stdout.split()[0])
    
    if naive_ans == opt_ans:
        passed += 1
    else:
        print(f"FAILED on test {t+1}")
        print("Input:")
        print(inp)
        print(f"Naive: {naive_ans}, Optimal: {opt_ans}")
        break

if passed == tests:
    print(f"All {tests} random small tests PASSED!")
