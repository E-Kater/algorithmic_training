def backspaceCompare(S: str, T: str):
    def build(S):
        ans = []
        for c in S:
            if c != '#':
                 ans.append(c)
            elif ans:
                ans.pop()
        return "".join(ans)
    return build(S) == build(T)


if __name__ == '__main__':
    s = input()
    t = input()
    print(backspaceCompare(s,t))