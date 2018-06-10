def __subsets(array):
    if len(array) == 0:
        return [[]]

    if len(array) == 1:
        return [[], [array[0]]]

    current = array[0]
    rest = __subsets(array[1:])
    final = [[current]]
    final.extend(rest)
    for lst in rest[:]:
        if lst == [] or lst == [current]:
            continue
        temp = lst[:]
        temp.append(current)
        final.append(sorted(temp))
    return final


def subsets(array):
    return sorted(__subsets(array))

def main():
    print subsets([15, 20, 12, 19, 4])

if __name__ == "__main__":
    main()
