import sys
sys.setrecursionlimit(2025)

def f(n):
    if n==1:
        return 1
    if n>1:
        return n*f(n-1)

print(f(2023)/f(2020))