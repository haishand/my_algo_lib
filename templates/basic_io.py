import sys

# 1. 核心優化：快讀與遞迴深度
input = lambda: sys.stdin.readline().rstrip("\r\n")
sys.setrecursionlimit(200000)


def solve():
    # 這裡寫你的邏輯
    # n = int(input())
    # a = list(map(int, input().split()))
    pass


if __name__ == "__main__":
    # 2. 多組數據處理 (Codeforces 常見格式)
    # t = int(input())
    # for _ in range(t):
    #     solve()

    # 單組數據
    solve()
