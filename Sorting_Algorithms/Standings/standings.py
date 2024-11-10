def selectionSort(array):
    size = len(array)
    for ind in range(size):
        max_index = ind
        for j in range(ind+1, size):

            # select the max element in every iteration
            if array[j]["score"] > array[max_index]["score"]:
                max_index = j
            if array[j]["score"] == array[max_index]["score"]:
                if array[j]["id"] < array[max_index]["id"]:
                    (array[j], array[max_index]) = (array[max_index], array[j])
        # swapping the elements to sort the array
        (array[ind], array[max_index]) = (array[max_index], array[ind])
    return array


if __name__ == '__main__':
    N = int(input())
    team = {}
    for i in range(0, N):
        id, score, name = input().split()
        team[i] = {"id": int(id), "score": int(score), "name": name}
    out = selectionSort(team)
    limit = 0
    for o in out.items():
        if limit < 3:
            print(o[1]["name"])
            limit += 1
        else:
            break
    ids = [i["id"] for i in out.values()]
    print(' '.join(map(str, ids)))
