def swap(list, x, y):
    tmp = list[x]
    list[x] = list[y]
    list[y] = tmp

def Percentile(scores, percentile_rank):
    n = 0

    for i in scores:
        minValue = i
        minIndex = n
        nextN = n + 1

        for j in scores[n + 1:]:
            if j < minValue:
                minIndex = nextN
                minValue = j
            nextN += 1

        swap(scores, n, minIndex)

	if 100.0 * (n + 1) / len(scores) >= percentile_rank:
            return i

        n += 1

def main():
    print Percentile([55, 57, 66, 77, 88], 60)


if __name__ == '__main__':
    main()
