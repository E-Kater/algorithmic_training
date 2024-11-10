def get_cost_by_gram(tpl):
    return tpl[1]["cost_by_gram"]


if __name__ == '__main__':
    N, W = map(int, input().split())
    weight = 0
    total_cost = 0
    cost_by_gramm = {}
    for i in range(1, N + 1):
        ci, wi = map(int, input().split())
        if wi != 0:
            c = ci * W // wi
            cost_by_gramm[i] = {"ci": int(ci), "wi": int(wi), "cost_by_gram": ci / wi}
        else:
            weight += ci
            cost_by_gramm[i] = {"ci": int(ci), "wi": int(wi), "cost_by_gram": int(ci)}
    out = dict(sorted(cost_by_gramm.items(), key=get_cost_by_gram, reverse=True))
    w_used = 0
    for o in out.items():
        c_i = o[1]["ci"]
        w_i = o[1]["wi"]
        if w_i == 0:
            total_cost += c_i
        else:
            w = min(W - w_used, w_i)
            c = c_i * w // w_i
            w_used += w
            total_cost += c
    print(total_cost)
