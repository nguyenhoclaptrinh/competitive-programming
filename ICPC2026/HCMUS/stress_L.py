import random
import subprocess

def solve_naive(d):
    c0 = d[0] + d[3] + d[6] + d[9]
    c1 = d[1] + d[4] + d[7]
    c2 = d[2] + d[5] + d[8]
    
    # We want to maximize: c0 + x + y + z
    # such that:
    # x <= c1, x <= c2 (pairs of 1 and 2)
    # y * 3 <= c1 - x
    # z * 3 <= c2 - x
    
    max_ans = 0
    for x in range(min(c1, c2) + 1):
        rem1 = c1 - x
        rem2 = c2 - x
        y = rem1 // 3
        z = rem2 // 3
        max_ans = max(max_ans, c0 + x + y + z)
        
    return max_ans

subprocess.run(["g++", "-O2", "L/L.cpp", "-o", "run_L"])

print("Stress testing Problem L (Lucky Numbers)...")
passed = 0
tests = 500
for t in range(tests):
    d = [random.randint(0, 50) for _ in range(10)]
    naive_ans = solve_naive(d)
    
    inp = " ".join(map(str, d)) + "\n"
    res = subprocess.run(["./run_L"], input=inp, capture_output=True, text=True)
    opt_ans = int(res.stdout.strip())
    
    if naive_ans == opt_ans:
        passed += 1
    else:
        print(f"FAILED on test {t+1}")
        print("Input:", inp)
        print("Naive:", naive_ans, "Opt:", opt_ans)
        break

if passed == tests:
    print(f"All {tests} random small tests PASSED!")
