quantum_a = 7 ** 5
quantum_m = 2 ** 31 - 1


def analyze_fast(n, m, q0):
    a = [0] * m
    m_div2 = m // 2
    min_val = -m_div2
    q = q0
    for i in range(n):
        x = q % m - m_div2
        a[x - min_val] += 1
        q = ((q * quantum_a) % quantum_m)
    res = 0
    k = 1
    for i in range(m):
        res += (i + min_val) * ((k + (k + a[i] - 1)) * a[i]) // 2
        k += a[i]
    return res


if __name__ == '__main__':
    N, M, q0 = map(int, input().split())
    print(analyze_fast(N, M, q0))
