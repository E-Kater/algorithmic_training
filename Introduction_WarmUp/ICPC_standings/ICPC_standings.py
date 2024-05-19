
def main():
    n = int(input())
    in_data = list[dict]()
    res = dict[list[dict]]()

    for i in range(0, n):
        team, score, penalty = input().split()
        score1 = int(score)
        d = {"team": team, "score": score1, "penalty": int(penalty)}
        in_data.append(d)
        if score1 in res:
            res[score1].append(d)
        else:
            res[score1] = [d]

    s = dict(sorted(res.items(), reverse=True))
    for k in s.keys():
        d = s[k]
        d1 = sorted(d, key=lambda e: (e['penalty'], e['team']))
        print(k, ' '.join([li["team"] for li in d1]))




if __name__ == '__main__':
    main()
