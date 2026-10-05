import sys
from collections import Counter


def main() -> None:
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    a = [int(x) for x in input_data[1 : n + 1]]

    MOD = 1_000_000_007
    freq = Counter(a)

    total_pairs = 0
    for k in freq.values():
        if k > 1:
            total_pairs = (total_pairs + k * (k - 1) // 2) % MOD

    print(total_pairs)


if __name__ == "__main__":
    main()
