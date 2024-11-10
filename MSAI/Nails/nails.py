def minimum_thread_length(N, nails):
    nails.sort()
    dp = [0]*N
    if N == 2:
        return nails[1] - nails[0]
    dp[1] = nails[1] - nails[0]
    dp[2] = nails[2] - nails[0]
    for i in range(3, N):
        dp[i] = min(dp[i - 1], dp[i - 2]) + nails[i] - nails[i - 1]
    return dp[N-1]


# Example usage
if __name__ == "__main__":
    n = int(input().strip())
    coordinates = list(map(int, input().split()))
    result = minimum_thread_length(n, coordinates)
    print(result)
