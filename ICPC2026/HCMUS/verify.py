import re
import os
import subprocess

with open("icpc_hcmus_2026_problems.md", "r", encoding="utf-8") as f:
    content = f.read()

problems = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]

for p in problems:
    print(f"--- Checking Problem {p} ---")
    
    # Extract problem section
    pattern = rf"## Problem {p}:.*?(?=## Problem |$)"
    match = re.search(pattern, content, re.DOTALL)
    if not match:
        print(f"[{p}] Could not find problem section.")
        continue
    
    p_text = match.group(0)
    
    # Extract Sample Inputs and Outputs
    inputs = re.findall(r"### Sample Input.*?\n```\n(.*?)\n```", p_text, re.DOTALL)
    outputs = re.findall(r"### Sample Output.*?\n```\n(.*?)\n```", p_text, re.DOTALL)
    
    if not inputs:
        # Some might just say "Sample Input" without number
        pass
        
    if len(inputs) != len(outputs):
        print(f"[{p}] Mismatch in number of inputs ({len(inputs)}) and outputs ({len(outputs)}).")
    
    # Compile
    cpp_file = f"{p}/{p}.cpp"
    if not os.path.exists(cpp_file):
        print(f"[{p}] {cpp_file} not found.")
        continue
        
    compile_cmd = ["g++", "-O2", "-Wall", "-Wextra", "-fsanitize=address,undefined", "-std=c++20", cpp_file, "-o", f"run_{p}"]
    comp_res = subprocess.run(compile_cmd, capture_output=True, text=True)
    
    if comp_res.returncode != 0:
        print(f"[{p}] Compilation FAILED!")
        print(comp_res.stderr)
        continue
    
    # Run tests
    all_passed = True
    for i, (inp, out) in enumerate(zip(inputs, outputs)):
        inp = inp.strip() + "\n"
        expected = out.strip()
        
        try:
            run_res = subprocess.run([f"./run_{p}"], input=inp, capture_output=True, text=True, timeout=3.0)
            actual = run_res.stdout.strip()
            
            if run_res.returncode != 0:
                print(f"[{p}] Test {i+1} FAILED (Runtime Error/Crash)")
                print(run_res.stderr)
                all_passed = False
                continue
                
            if actual == expected:
                print(f"[{p}] Test {i+1} PASSED")
            else:
                # Check line by line or whitespace agnostic
                def norm(s):
                    return " ".join(s.split())
                if norm(actual) == norm(expected):
                    print(f"[{p}] Test {i+1} PASSED (with whitespace differences)")
                else:
                    print(f"[{p}] Test {i+1} FAILED (Wrong Answer)")
                    print(f"Expected:\n{expected}\nActual:\n{actual}")
                    all_passed = False
                    
        except subprocess.TimeoutExpired:
            print(f"[{p}] Test {i+1} FAILED (Time Limit Exceeded)")
            all_passed = False
            
    if all_passed:
        print(f"[{p}] ALL TESTS PASSED.")
    print()

