#!/usr/bin/env python3

input_file = "1.txt.example"

def solve(in_file):

    list_a, list_b = [], []
    with open(in_file, "r") as f:
        for line in f:
            a, b = line.split("   ")
            list_a.append(int(a.strip()))
            list_b.append(int(b.strip()))
    list_a = sorted(list_a, reverse=True)
    list_b = sorted(list_b, reverse=True)
    total = 0
    for item in list_a:
        total += (item * len(list(filter(lambda x: x==item, list_b))))
    print(total)
            



if __name__ == "__main__":
    solve(input_file)
