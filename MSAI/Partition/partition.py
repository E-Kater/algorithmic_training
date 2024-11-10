def can_partition(n, costs):
    total_sum = sum(costs)

    # If the total sum is odd, it's not possible to divide it equally
    if total_sum % 2 != 0:
        return "NO"

    target = total_sum // 2

    # DP array to track possible sums
    dp = [False] * (target + 1)
    dp[0] = True  # We can always form sum 0 by not selecting any elements

    # Loop through each cost
    for cost in costs:
        # Update the DP array in reverse order to avoid overwriting results
        for j in range(target, cost - 1, -1):
            dp[j] = dp[j] or dp[j - cost]

    # If dp[target] is True, we can partition the set into two parts with equal sum
    return "YES" if dp[target] else "NO"

if __name__ == '__main__':
    # Read input
    n = int(input())  # Number of golden bars
    costs = list(map(int, input().split()))  # Costs of the bars

    # Output the result
    print(can_partition(n, costs))
