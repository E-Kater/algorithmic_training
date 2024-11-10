def knapsack(W, N, weights, costs):
    # Initialize DP table with all zeros
    dp = [[0] * (W + 1) for _ in range(N + 1)]

    # Build the DP table
    for i in range(1, N + 1):
        for w in range(W + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + costs[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    # Maximum profit
    max_profit = dp[N][W]

    # Backtracking to find the selected items
    selected_items = []
    w = W
    for i in range(N, 0, -1):
        if dp[i][w] != dp[i - 1][w]:  # This means item i was included
            selected_items.append(i)  # Append the 1-based index
            w -= weights[i - 1]

    selected_items.reverse()  # Reverse to get the items in order

    return max_profit, selected_items


if __name__ == '__main__':
    # Read input
    W, N = map(int, input().split())  # Knapsack capacity and number of items
    weights = list(map(int, input().split()))  # Weights of the items
    costs = list(map(int, input().split()))  # Costs of the items

    # Solve the knapsack problem
    max_profit, selected_items = knapsack(W, N, weights, costs)

    # Output the result
    print(max_profit)
    print(len(selected_items))
    print(" ".join(map(str, selected_items)))
